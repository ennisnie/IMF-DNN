# IMF-DNN

Integrated Multimodality Deep Fusion Deep Neural Network (IMF-DNN), which can flexibly accomplish both object detection and end-to-end tasks. The key of our approach is to process each modality independently with its own networks meanwhile to integrate these networks using additional central networks. This character makes our IMF-DNN flexible and able to accomplish both modular pipeline and end-to-end tasks. 

Extensive experiments demonstrate the test strategy to systematically analyze DNNs robustness and generalization ability in large amounts of diverse driving environment conditions We hope it will become useful resources for the intelligent vehicles research community.



## introduction

This work is based on our research paper, but we are still waiting for reviews. In this repository, we release the demo code for training with images and pointcloud. The data we used are from dataset DBNnet ([here](https://drive.google.com/open?id=14RPdVTwBTuCTo0tFeYmL_SyN8fD0g6Hc))

For KITTI 2D Object Detection Task, please refers to:

https://github.com/momo1986/pytorch-ssd

For KITTI Test Strategy. please refers to:

https://github.com/rentju/RRC-SSD


## Requirements

  Tensorflow 1.14
  PyTorch 1.0
  opencv-python 3.4+
  Python 3.6
  CUDA 10.0
  normally used python libraries and **laspy**

12.11.2019 update: add mixing template code

28.12.2019 update: add image+Pointnet fusion version

08.06.2020 update: new branch - mobilenet(V3) instead of VGG as backbone

01.07.2020 update: add object detection on KITTI code branch reference and test strategy for cross-domain neural network performance test strtegy
