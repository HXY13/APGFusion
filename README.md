# APGFusion: An Adaptive Dual-Branch Feature Fusion Network for Multimodal Medical Image Fusion
## Recommended Environment:
python=3.8\
torch=1.12.1+cu113\
scipy=1.9.3\
scikit-image=0.19.2\
scikit-learn=1.1.3\
tqdm=4.62.0
## Network Architecture:
Our APGFusion is implemented in ``net.py``.
## Training:
### Data preprocessing
Run 
```
python dataprocessing.py
```
### Model training
Run 
```
python train.py
```
## Testing:
Run 
```
python test_MIF.py
```

## 相关工作
```
@inproceedings{zhao2023cddfuse,
  title={Cddfuse: Correlation-driven dual-branch feature decomposition for multi-modality image fusion},
  author={Zhao, Zixiang and Bai, Haowen and Zhang, Jiangshe and Zhang, Yulun and Xu, Shuang and Lin, Zudi and Timofte, Radu and Van Gool, Luc},
  booktitle={Proceedings of the IEEE/CVF conference on computer vision and pattern recognition},
  pages={5906--5916},
  year={2023}
}
```
```
@article{hu2024pfcfuse,
  title={PFCFuse: A Poolformer and CNN fusion network for Infrared-Visible Image Fusion},
  author={Hu, Xinyu and Liu, Yang and Yang, Feng},
  journal={IEEE Transactions on Instrumentation and Measurement},
  year={2024},
  publisher={IEEE}
}
```
