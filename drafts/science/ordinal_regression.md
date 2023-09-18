# Ordinal regression (aka ranking, ordinal classification)

## Intro

As you read this, you will find some losses you can use to train neural networks for the ordinal regression problem.

Check that you already manage these concepts:
- A regressor is a parameterized function $f_\theta$ that outputs a single scalar value $\hat{y}$, presumably close to the target one $y$.
- Ordinal regression or ranking aims to maximize the spearman correlation between the predicted data and the target data. This is, we want to make the ordinal regressor $f_\theta$ predict values that are in the same order than their labels.
- Linear regression is a neural network with one neuron and identity activation. Neural networks (and linear regression) are trained by gradient descent on a differentiable loss.
- Notation will be: $y$, $\hat{y}$, $y_i$, $\hat{y}_i$ are the vector target, predicted vector, target element, and predicted element, respectively. All losses $L$ are functions $L(\hat{y}, y) \to \mathrm{R}$. $K$ is the number of classes, bins or ranks in which to put the data. $N$ is the number of datapoints.
- Ordinal classification is exactly the same than ordinal regression, although one could expect that "classification" refers to the case $K \ll N$ and "regression" refers to the case $K \approx N$.

## Losses
You will see listed here many approaches to train an ordinal regressor $f_\theta$. The ordinal regressor $f_\theta$ can be any algorithm that relies on the gradient on the loss (e.g. a neural network). **Each different approach is a different loss function**. 

### Regression
The simplest loss is the regression loss, because we are used to it. However, regression tries to learn both the ranking and the scaling, which is harder than learning only the ranking. We expect regression to be the least performing method.

There is no single loss for regression, although the most used ones are Mean Absolute Error (MAE) and Mean Squared Error (MSE). Both are cases of the $L_p$ norm of the difference between output and target. There are many other losses and listing them all is out of scope.

$$
L(\hat{y}, y) = L_p(\hat{y}, y) = \left(\sum_i |\hat{y}_i - y_i|^p \right)^{{1}/{p}}
$$

### Cumulative one hot
This is a smart way to solve the ordinal classification problem: instead of predicting a one hot vector, e.g. $[0, 0, 1, 0]$, as in usual multiclass classification, the predicted vector is a "cumulative one hot" vector, e.g. $[1, 1, 1, 0]$. 

To achieve the training, $f_\theta$ should be constrained: the last layer is a single neuron (without activation) that will output the ordinal regressed value. The previous-to-last layer has $K$ neurons with sigmoid activation. The loss is binary cross entropy between the cumulative one hot target and the output of this layer.

Let us call $y^{(c)}$ the cumulative one hot version of $y$. If $y$ is of shape $(B, 1)$, then $y^{(c)}$ will be of shape $(B, K)$. Let $H$ be the mapping $H(y) = y^{(c)}$.

$$
L(\hat{y}, y) = 
$$

