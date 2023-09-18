
# NeurIPS 2022

I have been lucky enough to have a paper accepted at the NeurIPS workshop in human in the loop learning. I'll share my reflections, including overall sentiment of the conference, highlights, topics I saw and things related to my work.

## Overall sentiment

The feeling the conference left on me is one of surprise about how huge and generalist the conference is. Moreover, there were a lot of participants coming from prestigious institutions. There are a few trends I haven't noticed. 

The conference is huge. Not only around 7k people but also a lot of papers. It was organized in two parts: main conference and workshops. The main conference interleaved invited talks for everyone with coffee breaks and poster sessions. The workshops were talks per topic also interleaved with coffee breaks and poster sessions. 

In all poster sessions the posters were not organized by topic. Instead they seemed randomly shuffled with the sole exception of the dataset papers. This made almost mandatory to go through each and every title, most of which I discarded ruthlessly. Most papers were coming from recognizable prestigious institutions or companies. Some MIT, Berkeley, and Stanford, some MILA, ETH, Delf, KAIST and PSL, and then the usual Meta, Google Research, DeepMind, Nvidia, Apple, Microsoft, Samsung, NEC, etc. Recently I saw an article that said that many resources and large size of a lab positively influence academic productivity, probably because there are benefits coming with scale.

## Highlights

### Datasets
The papers related to datasets were interesting. It was later confirmed that the reviewers chosen to evaluate this papers were better on average and that they held the dataset papers to high standards. There was an invited talk on the importance of the datasets and reproducible science which was interesting.

Some dataset (or library) highlights to me were:
- a dataset of fluid dynamics that interested me because the first author is a dear friend,
- "understanding aesthetics with language": a dataset on image aesthetics that paired images with comments / critics of photographers on reddit, which is probably much more informative than the usual Adobe-MIT-FiveK dataset ,
- "Change event dataset for discovery from spatio-temporal remote-sensing images", which could be useful for our lab, and
- myriad, a library comparing classical trajectory optimization and deep learning algorithms




### Forward-forward algorithm

Hinton, who I barely knew, apparently continues to work on biologically plausible ways to get intelligent behavior and he doesn't seem to think that the brain does backpropagation. In his invited talk he introduced the forward-forward training algorithm that presented a few advantages and was interesting. He said he just published a draft of a paper in his webpage based on his experiments. Even though is not yet applicable it could be the future, but it will take time because it is not as short term as what we researchers need today.

### Misc
In "A consistent and differentiable Lp Canonical Calibration Error Estimator" the authors introduce a differentiable calibration loss that enables us to get calibrated models using gradient descent! (maybe in a second training stage to be computationally more efficient)

## Topics

There are a few trends that I saw in this NeurIPS. I saw the following topics much more than what I expected:

- fairness, bias, privacy, etc.
- causal inference
- few-shot learning
- active learning
- reinforcement learning
- optimization

I saw the following topics al ittle less than what I expected:

- NLP 
- Computer Vision
- Optimizers

## My impressions

### Applied vs. not
I think that people that don't work on applied stuff are usually interested on novel ideas and not that much on their applications. Not all of these people strive for simplicity, although many of them do. Simplicity is subjective though and maybe my own mind is limiting me.

### Thinking outside of the box
Very few of us can think outside of the box as Hinton does. I wonder if he's just interpolating big amounts of knowledge or if he's truly thinking outside of the box. More in general, is there such a thing as creativity as opposed to interpolation?

### Interest in values
There is a lot of interest on the fairness / privacy / bias / distributed / ethical problems of AI. Too much to my liking, as many of these problems are political in their foundations.

### On the importance of language
Multimodal models have more and more of a place in the current research. I talked with one author that showed a method that did well on semantic segmentation using CLIP and asked him about other domains. He told me that there were people training vision-language models for biological images and also for remote sensing. I am now starting to get that there is indeed valua in pairing natural language with images but at first it came up to me more as a trend than as something fundamentally valuable. 

In short, there is value (as showed by the results) in using language. The question is why and to which extent it can generalize and be useful.

There are two explanations for the why yes, but first let's argue why not: animals don't use language and they are still able to see. We should be then able to "solve" vision without relying on language. Now let's explore why language can be important:
- first, using language adds more learning signal in the sense that it labels which objects are on the image without giving their location. Not only that, but language can say things about the relations between these objects. This auxiliary learning signal can force a neural network train for those abstractions that are present in language. But language is not only about the creation of entities that can force correspondences inside and between the images but also about making those entities meaningful to us. This is hard to do without language
- the sencond explanation is complementary and was given to me by Igor from Google Research: prediction is probably involved and useful for learning and predicting language is a "just-right" task in terms of difficulty. This just started to make sense to me, and maybe he's right. 

I still have to think about alternatives to language if there are any, in other words, trying to come up with a story about how most animals learn without it.

Regarding the generalization of these models I don't know if they are able to expand their vocabulary. Not being able to do this hinders their generalization capabilies. To which extent can we use the word "thing" to refer to an unknown object in a new image?

### Few-shot, active learning and human-in-the-loop-learning
I think the first two areas lack the human-in-the-loop framework that I introduced. It could be good to look at both from this point of view. I feel I'm alone using human-in-the-loop learning for annotation but it is a good path to pursue. Most human-in-the-loop learning is around robotics, which is interesting, but still seems to me like a collection of ad-hoc methods. 

I got to know 2 annotation companies and one of them offered me a grant.






