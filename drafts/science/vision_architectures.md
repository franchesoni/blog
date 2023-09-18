
# Vision architectures

RoI = Region of Interest

## Mask R-CNN
For instance segmentation, which is different than object detection and semantic segmentation. For instance, we mask pixels as "person 1", "person 2" and not "people". Semantic segmentation gives a big mask for people hugging but instance segmentation gives a different mask to each person participating on the hug.

Extends Faster R-CNN by adding a branch for prediction segmentation masks on each Region of Interest, in _parallel_ with the existing branch for classification and bounding box regression. 

The mask branch is a small FCN applied to each RoI. Predicting segmentation mask in a pixel-to-pixel manner.

The paper introduces RoIAlign





