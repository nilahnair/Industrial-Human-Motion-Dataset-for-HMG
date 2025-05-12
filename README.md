# Industrial-Human-Motion-Dataset-for-HMG

## Introduction
This page aims to be a discussion and information sharing platform between the Human Motion Generation Community and Dataset Creators (both Academic and Industrial). This initiative was started based on the understanding that Generative Artificial Intelligence (GenAI) can benefit simulation environments. However, GenAI is data-intensive and requires appropriately annotated data for fruitful generation. When considering dataset creation, currently, different dataset creators follow different file formats and publishing methods, which may restrict the feasibility of using the data seamlessly for human motion generation. Consequently, there needs to be a communication channel between the dataset creators and the AI community to share their requirements, technology and applications. For example, the industry could benefit from human motion generation in their simulation environment. Still, as of now, the activities of daily living human motion generation are insufficient, as industrial terminologies and motions are not available in daily activities. So, if the industrial dataset creators were to provide data to the GenAI community, further research can be performed specifically in industrial scenarios. With the correct formats, research can be further accelerated. Thus, it benefits both parties as a first step in this direction. Here, you see preliminary information collected and to be further refined by the community, specifically for human motion generation. 

![Image generated from MotionGPT for the prompt, 'A person pushing a cart' The generated snippet was of a person performing cartwheel, while the preferred motion would have been a person pushing a cart, for example, a shopping cart.](https://github.com/nilahnair/Industrial-Human-Motion-Dataset-for-HMG/blob/main/images/cart.png)

The above image is a sample showing the need for more datasets from the industry for human motion generation. The image is from a video snippet generated from MotionGPT [GitHub](https://github.com/OpenMotionLab/MotionGPT/tree/main/mGPT). The prompt was 'A person pushing a cart'. The expectation was that the generated snippet would be of a person pushing something similar to a shopping cart. However, the generated image was of a person performing a cartwheel.

Our work, **Recommendation on Human Motion Generation Datasets for Industrial Simulations**, provides a framework for dataset creators and recommendations on their dataset formatting that would sufficiently help them create a dataset that can be more easily used in human motion generation. The work understands that strict standardisation of methods is difficult to follow given the frequent technological changes. However, the work provides the dataset creators with an understanding of where all standardisation is required and what information is mandatory for further development. The framework is shown below: 

![Framework for dataset creation cycle.](https://github.com/nilahnair/Industrial-Human-Motion-Dataset-for-HMG/blob/main/images/Flowchat_revised.png)

## To Get Started

The following surveys were found to be suitable for obtaining a good overview:

For **Human Motion Generation** see: Human Motion Generation: A Survey [Paper](https://arxiv.org/pdf/2307.10894)

For **Human Motion Synthesis** see: A Survey on Deep Learning for Skeleton-Based Human Animation [Paper](https://arxiv.org/pdf/2110.06901)

For **Human Motion Analysis Review** see: Online human motion analysis in industrial context: A review [Paper](https://www.sciencedirect.com/science/article/pii/S0952197624000083) 

For understanding **SMPL-X: Skinned Multi-Person Linear - eXpressive Model** see: [Website](https://smpl-x.is.tue.mpg.de/) 

For an example on **Annotation Framework on video data** see: Motion-X: A Large-scale 3D expressive Whole-body Human Motion Dataset [Paper](https://proceedings.neurips.cc/paper_files/paper/2023/file/4f8e27f6036c1d8b4a66b5b3a947dd7b-Paper-Datasets_and_Benchmarks.pdf)

For **Multi-modal Motion Generation** see: Large Motion Model for Unified Multi-Modal Motion Generation [Paper](https://arxiv.org/html/2404.01284v1)

## Human Motion Generation Datasets

**SMPL data collection:** Archive of Human Capture As surface Shapes [Website](https://amass.is.tue.mpg.de/)
AMASS Annotations:
1. BABEL: Bodies, Action and Behaviours with English Labels [Website](https://babel.is.tue.mpg.de/index.html)
2. HumanML3D: 3D Human Motion-Language Dataset [GitHub](https://github.com/EricGuo5513/HumanML3D)
3. HUMANISE: Language-conditioned Human Motion Generation in 3D Scenes [GitHub](https://github.com/Silverster98/HUMANISE?tab=readme-ov-file)

**Dataset with Language Annotations:**
1. KIT Motion-Language Dataset [Website](https://motion-annotation.humanoids.kit.edu/dataset/)
2. Motion-X Dataset [Website](https://motion-x-dataset.github.io/)
3. HumanAct12 Dataset [Website](https://ericguo5513.github.io/action-to-motion/#data) Note: not active at the time of access on 24.04.2025.
4. NTU RGB+D 120 Dataset [Website](https://rose1.ntu.edu.sg/dataset/actionRecognition/)

## Annotation Tools
+ KIT Annotation Tool [Website](https://motion-annotation.humanoids.kit.edu/)
+ Babel Frame and Sequence Labelling Tools [Website](https://babel.is.tue.mpg.de/demos.html)

## Simulation Environments and Visualisation Tools
+ Unity Hub
+ Blender
+ Isaac Sim
+ Aitviewer [GitHub](https://github.com/eth-ait/aitviewer)
+ Python SMPLX [GitHub](https://github.com/vchoutas/smplx)

## Data Creation Tools
+ RGB to MoCap Generation: EasyMoCap [GitHUb](https://github.com/zju3dv/EasyMocap)
+ MoCap to SMPL Convertion: Mosh++ [GitHub](https://github.com/nghorbani/moshpp)

## Motion Generation Models

## Recommended Conferences and workshops
* NeurIPS
* CVPR
* ICCV
* ECCV
* ICLR
* 3DV
* IEEE VR
* HuMoGen (CVPR workshop)

## Metrics
- FID
- Diversity
- R-Precision
- MultiModal Distance
- [Arxiv Paper](https://arxiv.org/pdf/2405.07680)
- [Arxiv Paper](https://arxiv.org/pdf/2309.10248)

## Code

Code snippets are provided within the folder 'code'. If you would like to discuss or require code snippets for other works, please raise an issue.


