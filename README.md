# ImageCompression
Compress an image thanks to matrix factorisation.

## Idea
Find two matrices p and q such that p x q = image.  
However we want p of dimension(height, k) and q(k, width), assuming k << min(height, width).  

In order to compute those matrices, we use the gradient descent algorithm in order to reduce the euclidean error between the dot product and the real image.  

## Execution
```
python3.5 compression.py FileName.png [-k int] [-i int] [-o resultFileName]
```
This commands computes the compression of the image FileName with dimension k, and i iteration maximum for gradient descent.   

## Results

## Libraries
Needs numpy, scipy and sys. Compiled with python3.5
