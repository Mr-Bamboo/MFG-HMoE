# MFG-HMoE (IEEE GRSL 2025)
### [**Paper**](https://ieeexplore.ieee.org/document/10949132) | [**Arxiv**](https://arxiv.org/abs/2502.09654)

PyTorch codes for "[Heterogeneous Mixture of Experts for Remote Sensing Image Super-Resolution](https://ieeexplore.ieee.org/document/10949132)", **IEEE Geoscience and Remote Sensing Letters(GRSL)**, 2025.

## Abstract
> Remote sensing image super-resolution (SR) aims to reconstruct high-resolution (HR) remote sensing images from low-resolution (LR) inputs, thereby addressing limitations imposed by sensors and imaging conditions. However, the inherent characteristics of remote sensing images, including diverse ground object types and complex details, pose significant challenges to achieving high-quality reconstruction. Existing methods typically use a uniform structure to process various types of ground objects without distinction, making it difficult to adapt to the complex characteristics of remote sensing images. To address this issue, we introduce a mixture-of-experts (MoE) model and design a set of heterogeneous experts. These experts are organized into multiple expert groups, where experts within each group are homogeneous while being heterogeneous across groups. This design ensures that specialized activation parameters can be used to handle the diverse and intricate details of ground objects effectively. To better accommodate the heterogeneous experts, we propose a multilevel feature aggregation (MFA) strategy to guide the routing process. In addition, we develop a dual-routing mechanism to adaptively select the optimal expert for each pixel. Experiments conducted on the UCMerced and AID datasets demonstrate that our proposed method achieves superior SR reconstruction accuracy compared with state-of-the-art methods.
## Pipeline  
 ![image](/figs/MFG-HMoE.png)
 
## Install
```
git clone https://github.com/Mr-Bamboo/MFG-HMoE.git
python setup.py develop
```

## Environment
 > * CUDA 11.8
 > * Python >=3.7.0
 > * PyTorch >= 1.9.0
 > * basicsr >= 1.3.4.9


## Usage

### Train
- Single GPU For Training:
```
python hmoe/train.py -opt options/train/train_HMoE_SRx4_UCMerced.yml --auto_resume
```
- The command for multi-GPU training is same as [HAT](https://github.com/XPixelGroup/HAT).

### Test
```
python hmoe/test.py -opt options/test/test_HMoE_SRx4_UCMerced.yml
```


## Acknowledgments
Our MFG-HMoE mainly borrows from [HAT](https://github.com/XPixelGroup/HAT) and [TTST](https://github.com/XY-boy/TTST). Thanks for these excellent open-source works!

## Contact
If you have any questions or suggestions, feel free to contact me.  
Email: chenbowen@buaa.edu.cn

## Citation
If you find our work helpful in your research, please consider citing it. Your support is greatly appreciated! 😊

```
@ARTICLE{10949132,
  author={Chen, Bowen and Chen, Keyan and Yang, Mohan and Zou, Zhengxia and Shi, Zhenwei},
  journal={IEEE Geoscience and Remote Sensing Letters}, 
  title={Heterogeneous Mixture of Experts for Remote Sensing Image Super-Resolution}, 
  year={2025},
  volume={22},
  number={},
  pages={1-5},
  keywords={Remote sensing;Image reconstruction;Feature extraction;Training;Superresolution;Routing;Testing;Sensors;Spatial resolution;Solid modeling;Mixture of experts (MoE);multilevel feature;remote sensing images;super-resolution (SR);upsample},
  doi={10.1109/LGRS.2025.3557928}}
```
