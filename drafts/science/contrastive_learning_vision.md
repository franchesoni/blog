
# Contrastive learning for vision: a little survey

It happened to me that I want to design a filter trained by contrastive learning methods. But I do not know what is the best way. This is my fast review to find this out (3 am).

## Titles
We start by listing some interesting titles 

- A Simple Framework for Contrastive Learning of Visual Representations
- MoCo, BYOL (I want more recent)
- Unsupervised Learning of Visual Features by Contrasting Cluster Assignments: SwAV, instead of running pairwise comparisons they use data augmentation and cluster assingment. To do this they use the _representation_ extracted from one view to predict the _cluster assigned_ to another view of the image.
- Supervised Contrastive Learning: they use the labels used to compute the cross-entropy loss in the traditional supervised setting to do contrastive learning, i.e. pushing representations of the same class together.
- Exploring Simple Siamese Representation Learning (Kaiming He)
- Divide and Contrast: Self-supervised Learning from Uncurated Data
- Mean Shift for Self-Supervised Learning: a generalization of BYOL that shifts representations of views towards the mean of the nearest neighbors' representations.
- Momentum^2 Teacher: Momentum Teacher with Momentum Statistics for Self-Supervised Learning. It seems vaguely similar to BYOL but the idea is not seducing enough. I want basic but powerful contrastive!
- With a Little Help from My Friends: Nearest-Neighbor Contrastive Learning of Visual Representations
- Train a One-Million-Way Instance Classifier for Unsupervised Visual Representation Learning. The title is expressive, they try to solve the problems that arise when doing this naively. This could be useful.
- Efficient Visual Pretraining with Contrastive Detection. I think I have read this paper from DeepMind. It is interesting, although I forgot the contrastive method.
- A Low Rank Promoting Prior for Unsupervised Contrastive Learning. They do not only look for clusters but also for clusters that live in low-dimensional spaces. This is supposed to increase performance. At the cost of some complexity, of course.
- DetCo: Unsupervised Contrastive Learning for Object Detection
- An Empirical Study of Training Self-Supervised Vision Transformers. Ok, this is the paper I want to read.
- Propagate Yourself: Exploring Pixel-Level Consistency for Unsupervised Visual Representation Learning. This one is in my to-read list, oups.
- Divide and Contrast: Self-supervised Learning from Uncurated Data. They alternate between contrastive learning and clustering-based hard negative mining. I don't like alternating, it is not simple enough.
- Unsupervised Pretraining for Object Detection by Patch Reidentification
- Understanding self-supervised Learning Dynamics without Contrastive Pairs
- Self-supervised Learning from a Multi-view Perspective. Theoretical work, sounds interesting.
- Barlow Twins: Self-Supervised Learning via Redundancy Reduction. It is an improvement over traditional contrastive learning that suffers from sometimes having views that are very similar.

Now I'm satisfied with my literature review and luckily Kaiming He wrote the paper _An Empirical Study of Training Self-Supervised Vision Transformers_. I think this paper will be enough to continue my little review and get an idea of which methods I should use. (03:38)

## _An Empirical Study of Training Self-Supervised Vision Transformers_

I feel like the abstract is not really what I wanted, as they talk about "benchmark ViT results in MoCo v3 and several other self-supervised frameworks". I hope they are not _that_ centered in MoCo, I want a wide overview. However, I trust the authors' criteria (which doesn't always happen). I'll give a summary. 

### Intro

#### Part 1
They try self-supervised methodologies based in siamese networks for use with Vision Transformers (ViT). They do that because ViT work better. They use MoCo, _A simple framework for contrastive learning of visual representations_, _Unsupervised learning of visual features by contrasting cluster assignments_ and BYOL.

#### Part 2

Convnets have been already studied. For ViT, there is mild degradation related to training instability. To solve this they "freeze the patch projection layer in ViT to a fixed random patch projection".

#### Part 3

Their big ViT works well and is competitive against big ResNets. This was before the Masked Autoencoder paper. But they were already suggesting that aggresive SSL on ViT could be great. 

### Related work
The interesting part. 

#### Contrastive learning
Contrastive learning is to attract positive samples and dispel negative samples. The need of negative samples has been questioned, which is important is to match positives.

#### MoCo v3
Two crops under random data augmentation. These views are encoded to vectors $q, k$ by encoders $f_q, f_k$. They use the InfoNCE loss:
$$\mathcal{L}_q = -\log{\frac{\exp{(q\cdot k^+ / \tau)}}{\exp{(q \cdot k^+ / \tau)}+\sum_{k^-}{\exp{(q \cdot k^- / \tau)}}}}$$

where $k^+$ and $k^-$ are encodings of the same and a different image than $q$, respectively. 
However, they simplify the loss function to:
```python
loss = ctr(q1, k2) + ctr(q2, k1)

def ctr(q, k):
    logits = mm(q, k.t())  # [N, N] pairs
    labels = range(N)
    loss = CrossEntropyLoss(logits/tau, labels)
    return 2 * tau * loss
```
where `q1 q2 k1 k2` are the encodings of images `1` and `2` through $f_q$ and $f_k$. Note that $f_k$ is a backbone with a projection MLP on top, while $f_q$ is a backbone, a projection MLP and a prediction MLP. $f_k$ is updated by the moving average of $f_q$ (excluding the prediction head).

#### Training and instability

They show a few curves that indeed show some abrupt falls and a performance loss, depending on the batch size. Large batch sizes create a "training restart" effect.  

Then, use 4k batch size, AdamW optimizer, and _freeze the weights of the patch projection_. This is something I don't want to do for my application, but let's keep reading.

It's basically that, some hyperparameters, and the non-negligible fact that they trained on 512 TPUs. This is, if I do it in 1 TPU it would take more than a year :)

#### SSL frameworks
MoCo, SimCLR, BYOL, SwAV. MoCo is the best for transformers (according to this paper). Moreover, removing the prediction MLP does not hurt accuracy by a lot, which is good because it's simpler.

## My conclusion

If thinking about doing contrastive learning with ViT, probably the method below is simple and should provide a good baseline.

Procedure (for each image):
- take two views of the same image
- pass both of them through both networks $f_q$, $f_k$ (we get $q_1, q_2, k_1, k_2$). The networks should consist on a backbone + an MLP projection head. They must be identical.
- compute the loss as described in a section above
- update the weights of $f_q$ (or $f_k$, it is symmetrical), and write a moving average of $f_q$ weights into $f_k$ weights
- train :)

I have to see still how to do the update. Tomorrow starts the implementation. (04:46)

