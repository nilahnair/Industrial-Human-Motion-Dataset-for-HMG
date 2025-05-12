import pandas as pd
import numpy as np
import torch
from scipy.spatial.transform import Rotation as R

# Load CSV (skip header rows)
csv_path = "L01_S01_R01.csv" #taking a file from LARa V4 dataset as example
with open(csv_path, 'r') as f:
    lines = f.readlines()

headers = lines[3].strip().split(',')
data_lines = lines[5:]
from io import StringIO
df = pd.read_csv(StringIO(''.join(data_lines)), header=None)
df.columns = headers

# Define your joint mapping: mocap name → SMPL-X index
# You can refine this depending on available joints
smplx_joint_names = [
    "pelvis", "left_hip", "right_hip", "spine1", "left_knee", "right_knee",
    "spine2", "left_ankle", "right_ankle", "spine3", "left_foot", "right_foot",
    "neck", "left_collar", "right_collar", "head", "left_shoulder", "right_shoulder",
    "left_elbow", "right_elbow", "left_wrist", "right_wrist"
]

# Placeholder mapping: update to match your CSV segment names!
csv_joint_prefixes = {
    "pelvis": "Subject01:Root",
    "left_hip": "Subject01:LeftHip",
    "right_hip": "Subject01:RightHip",
    "spine1": "Subject01:Spine1",
    "spine2": "Subject01:Spine2",
    "spine3": "Subject01:Spine3",
    "neck": "Subject01:Neck",
    "head": "Subject01:Head",
    "left_knee": "Subject01:LeftKnee",
    "right_knee": "Subject01:RightKnee",
    "left_ankle": "Subject01:LeftAnkle",
    "right_ankle": "Subject01:RightAnkle",
    "left_foot": "Subject01:LeftFoot",
    "right_foot": "Subject01:RightFoot",
    "left_collar": "Subject01:LeftCollar",
    "right_collar": "Subject01:RightCollar",
    "left_shoulder": "Subject01:LeftShoulder",
    "right_shoulder": "Subject01:RightShoulder",
    "left_elbow": "Subject01:LeftElbow",
    "right_elbow": "Subject01:RightElbow",
    "left_wrist": "Subject01:LeftWrist",
    "right_wrist": "Subject01:RightWrist"
}

# Choose a frame to convert (e.g., first frame)
frame = df.iloc[0]

# Store axis-angle rotations
axis_angles = []

for joint in smplx_joint_names:
    prefix = csv_joint_prefixes.get(joint)
    if prefix is None:
        axis_angles.append(torch.zeros(3))  # fallback
        continue
    try:
        rx = frame[f"{prefix}:RX"]
        ry = frame[f"{prefix}:RY"]
        rz = frame[f"{prefix}:RZ"]
        rot = R.from_euler('xyz', [rx, ry, rz], degrees=True)
        aa = torch.from_numpy(rot.as_rotvec())  # axis-angle
    except Exception:
        aa = torch.zeros(3)
    axis_angles.append(aa)

# Convert to SMPL-X format
body_pose = torch.stack(axis_angles[1:22]).reshape(1, -1)  # 21 joints
global_orient = axis_angles[0].reshape(1, 3)               # Root
transl = torch.tensor([
    frame[f"{csv_joint_prefixes['pelvis']}:TX"],
    frame[f"{csv_joint_prefixes['pelvis']}:TY"],
    frame[f"{csv_joint_prefixes['pelvis']}:TZ"]
]).reshape(1, 3) / 1000.0  # Convert mm to meters

# Optional: betas can be zeros
betas = torch.zeros(1, 10)

# Pack into dictionary
smplx_params = {
    "body_pose": body_pose,
    "global_orient": global_orient,
    "betas": betas,
    "transl": transl
}

# Save to disk
torch.save(smplx_params, "smplx_frame0.pt")
print("Saved SMPL-X parameters for frame 0.")
