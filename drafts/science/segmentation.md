
Just ended a call with my supervisor, JMM. He is very experienced. I was thinking about how he mentioned texture segmentation a few months ago (too many) and my other supervisor and I continued talking about neural networks.

Today I had all of his time and it was very interesting. I also showed quite a lot of images related to feature correspondence and attention in transformers. He said too many important things

- transformers do non-local-means or attention which is basically clustering
- apparently the field is going back to feature clustering
- bilateral filtering of textures is desirable
- after 50 years the segmentation problem is still not solved
- multiscale problem
- which is the progress?

my thoughts:
- superpixels are not what we want
- texture oversegmentation is what we want
- experience with my cousing, valizas foca
- making dnn features dense again

problems to solve:
- texture features (we have the decalage problem)
- borders (some bilateral filtering or CRF)
- making NN features dense
    - try XCiT features
    - XCiT with more patches (different stride)

how to solve segmentation?
- more info: video, stereo, lidar
- better features
    - color features
    - border-sensitive features
    - texture features
    - SSL learned features
- better feature processing
    - many candidate segmentations
    - different affinity matrices
