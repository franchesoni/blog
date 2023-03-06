---
layout: post
title:  "Best black-and-white image format"
date:   2023-03-06 14:06:55 +0000
categories: software
---


# .PNG is the lightest format for binary images

Imagine you have a mask, this is, an image filled with `0`s and `1`s or `False` and `True`.
Such a mask could look like
![head-stencil](https://raw.githubusercontent.com/franchesoni/blog/main/docs/assets/images/nm2HM.png)

**What's the lightest format to save this image into?**

## Formats
- JPEG: is the usual format for lightweight images. It uses frequency information to achieve a smart compression that ends up being perceptually similar but very lightweight. The bad side is that it's a lossy compression mechanism and it deals with images that have at least 8 bit depth. Our images have 1 bit depth.
- PNG: is the usual format that allows for transparency and it's lossless. We will perfectly reconstruct the image. Although it appears the most complex at first sight it can handle various bit depths (giving us a 8x factor) and has some interesting lossless compression mechanisms for that case.
- PBM: portable bit map format appears to be specific for binary images. Although it uses bits instead of bytes for the values it doesn't involve compression.

## Experiments
We load images and save them using each of the formats above to see the final size. Full code is given at the end.

### Particular image
We load and save the following binary image (488x275) using the different formats

![head-stencil](https://raw.githubusercontent.com/franchesoni/blog/main/docs/assets/images/nm2HM.png)
```python
imgname = "nm2HM.png"
pilimg = Image.open(imgname)
npimg = np.array(pilimg)
for format in formats:
  outpath = "out1" + format
  pilimg.save(outpath)
  outpaths.append(outpath)
```


### Random images
This experiments generates random binary images of sizes (10,10), (100,100), ..., (10000,10000) and saves them using the different formats. This experiment stress-tests the compression methods.

```python
print('generating random images...')
for size in [10, 100, 1000, 10000]:
  random_img = Image.fromarray((np.random.rand(size, size)>0.5).astype(np.uint8)*255)
  for format in formats:
    outpath = f"out_size_{size}{format}"
    random_img.save(outpath)
    outpaths.append(outpath)
```

### Results

Sizes in bytes, the lowest is bold-face.
 
| image | .JPEG | .PNG | .PBM |
|---|---|---|---|
| example | 14818 | **4191** | 402615 |
| out_size_10 | 478 | **104** | 113 |
| out_size_100.jpeg | 7643 | **2334** | 10015 |
| out_size_1000.jpeg | 681430 | **214614** | 1000017 |
| out_size_10000.jpeg | 68087734 | **20329735** | 100000019 |