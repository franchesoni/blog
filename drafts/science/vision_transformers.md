
# Deep learning for computer vision

Convolutional neural networks (CNN) are the ones that dominate in terms of performance and practical use. Well known models include ResNet, YOLO, EfficientNet, MobileNet, etc.

In Natural Language Processing (NLP), the dominant architecture is the transformer architecture (that I'll describe next). Recently, transformers were applied for computer vision, and their performance is competitive with that of CNNs.

# Vision transformer for image classification

## Divide in patches
Take an image $I \in R^{H\times W \times C}$ with variable $H, W$. 
Divide an image into patches $p_i(I)$. A patch is a square crop of the image. For simplicity, assume $H=W$ and create non-overlaping patches whose concatenation is the image. For instance, take an image of size $512\times 512$ and extract patches from a $32 \times 32$ grid, which means patches with side $16$. 

## Flatten the patches
Now that we have extracted the patches we can flatten them, i.e. put all the values of the patch inside a column vector. The size of such a column vector is $H(p_i(I)) \times W(p_i(I)) \times C$, in our example, $16 \times 16 \times 3 = 768$ for an RGB image ($C=3$). Let's call these vectors $x_i = \text{flatten}(p_i(I))$.

## Create input embedding

### Affine projection (dense layer)
Now we create embeddings $z_i = W x_i + b$. This is a traditional linear layer.

### Add possitional encoding
Given each index $i$ one can generate a positional encoding $pe(i)$ of the same shape than $z$. Any kind of positional encoding is ok.

### Add CLS token
CLS, which stands for classification, is a token introduced because there is the need of one image-level vector, as the other vectors are only associated to patches. In practice this takes the form of a vector $z_0$ of the same dimension of the other $z_i$.

## Understanding attention

### Seq2seq

The attention mechanism was first presented in the context of recurrent neural networks (RNNs). In RNNs, we have an input sequence $\{x_i\}_{1 \leq i \leq m}$, that we encode, yielding states $h_i$ (and intermediate outputs that are used to generate the encoding of the next element on the sequence).

The most common formulation of attention assumes that we want to compute the "attention" weights for an input vector $s_0$, e.g. $s_0 = h_m$. In this context $s_0$ is related to the _query_ and $h_i$ are related to the _keys_. More specifically, one can train linear mappings $W_K$ and $W_Q$ that will generate the keys and query:

$$k_i = W_K h_i$$
$$q_0 = W_Q s_0$$

The matching score between keys and query is given by their inner product, e.g. for query $q_0$ and key $k_i$, the score $\tilde{\alpha}_i$ is given by 

$$\tilde{\alpha}_i = k_i^T q_0$$

Then a softmax function is applied to the vector $\tilde{\alpha}_0$ to obtain the attention weight vector $\alpha_0$. This is, $\alpha_0 = \text{Softmax}(\tilde{\alpha_0})$. Recall that softmax normalizes the input vector so the sum is 1 and all values are in $[0, 1]$.

After obtaining the attention weights $\alpha_0$ one can get the context vector $c_0 = [h_1, \dots, h_m] \alpha_0$, which is associated to $s_0$.

The framework here presented was sequence to sequence learning. To generate the output sequence one usually uses the last output $o_{t-1}$ and the current input $x'_t$. The output is $o_t, s_t = RNN(o_{t-1}, x'_t)$. In the attention case one can use the last context vector as another input, which results in outputs $o_t, s_t = RNN(o_{t-1}, x'_t, c_{t-1})$. Furthermore, one should compute $c_t = [h_1, \dots, h_m] \alpha_t$, with $\alpha_t = \text{Softmax}((W_K h)^T W_Q s_t)$. 

And that's how attention was added to sequence to sequence modeling. 

### Attention is all you need










to do:
- positional encoding
- CLS token embedding
- BLEU score for NLP
- sequence to sequence decoder output



