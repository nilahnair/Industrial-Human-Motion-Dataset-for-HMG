import torch
import json
import numpy as np
from scipy.spatial.transform import Rotation as R

# === Load SMPL-X parameters (from earlier step) ===
smplx_params = torch.load("smplx_frame0.pt")

# === Helper functions ===

def smpl_to_unity_translation(transl):
    """SMPL to Unity: flip Z axis (Right-Handed to Left-Handed)."""
    return transl * torch.tensor([1.0, 1.0, -1.0])

def convert_axis_angle_to_unity(axis_angle):
    """Convert a single axis-angle vector from SMPL to Unity space."""
    r = R.from_rotvec(axis_angle)
    rotmat = r.as_matrix()
    
    # Flip Z (3rd col and row) to switch forward direction
    rotmat[:, 2] *= -1
    rotmat[2, :] *= -1
    
    unity_rot = R.from_matrix(rotmat)
    return unity_rot.as_rotvec()

# === Convert all parameters ===

# Convert root translation
transl_unity = smpl_to_unity_translation(smplx_params["transl"][0])

# Convert global orientation
global_orient_unity = convert_axis_angle_to_unity(smplx_params["global_orient"][0].numpy())

# Convert body pose
body_pose_unity = []
for i in range(smplx_params["body_pose"].shape[1] // 3):
    aa = smplx_params["body_pose"][0, i*3:(i+1)*3].numpy()
    body_pose_unity.append(convert_axis_angle_to_unity(aa))
body_pose_unity = np.stack(body_pose_unity)

# Optional shape params (unchanged)
betas = smplx_params["betas"][0].numpy()

# === Save as Unity-compatible JSON ===

unity_data = {
    "global_orient": global_orient_unity.tolist(),
    "body_pose": body_pose_unity.tolist(),
    "transl": transl_unity.tolist(),
    "betas": betas.tolist()
}

with open("smplx_frame0_unity.json", "w") as f:
    json.dump(unity_data, f, indent=2)

print("Saved Unity-compatible SMPL-X pose to 'smplx_frame0_unity.json'")
