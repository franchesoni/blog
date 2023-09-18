
# Masked Autoencoders Are Scalable Vision Learners - Explained

## Pointers

- [Masked Autoencoders Are Scalable Vision Learners](https://arxiv.org/abs/2111.06377) (Paper)
- [Attention is all you need](https://arxiv.org/pdf/1706.03762.pdf) (Paper)
- [Implementation in Keras](https://keras.io/examples/vision/masked_image_modeling/) (Tutorial)
- [Implementation in Pytorch (1)](https://github.com/FlyEgle/MAE-pytorch) (Repository)
- [Implementation in Pytorch (2)](https://github.com/pengzhiliang/MAE-pytorch) (Repository)


## Summary
This paper proposes a way to train Vision Transformers (ViT) in a self-supervised way in order to get useful representations of the input image. This is achieved by masking out a large proportion of the input patches, e.g. three out of four, and then reconstructing these masked patches. The idea resembles that in Natural Language Processing (NLP) and potentially unlocks a new chapter in computer vision. 

The obtained image representations are evaluated by measuring the performance of fine-tuned networks on downstream tasks. These networks use the encoded image as input. The simplest network is a linear regression, but the downstream performance improves with greater fine-tuning. The representations obtained by this method are superior than those of previous methods in all downstream tasks.

## High level overview

### Training

Each image $I_i$ in the database is used to generate an input $x_i$ and a target $y_i$ pair. The input $x_i$ is obtained by the following procedure:
- Data augmentation is:
    - rescaling to $[0,1]$, e.g. divide by $255$
    - resizing to some predefined shape
    - random crop a square of `IMAGE_SIZE` 
    - horizontal random flip
- Divide the augmented $I_i$ in square patches $p_{ij}$ indexed by $j$. The index $j$ corresponds to the position of the patch according to some `reshape` function.
- 


### Inference
- Image preprocessing is:
    - rescaling to $[0,1]$, e.g. divide by $255$
    - resizing to `IMAGE_SIZE` 








