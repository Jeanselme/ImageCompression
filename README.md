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
```
python3.5 performances.py
```
This command computes the compressed image for k = 10, 20, 30, 40, 50 (y axis) with a learning rate = 1/k for iteration = 1, 11, 21, 31, 41, 51, 61, 71, 81, 91 (x axis).  
![ResultGD](https://raw.githubusercontent.com/Jeanselme/ImageCompression/master/Images/GDResults.png)  

The following image shows the advantage of stochastic gradient descent :  
![ResultSGD](https://raw.githubusercontent.com/Jeanselme/ImageCompression/master/Images/SGDResults.png)  
-	Error is more uniform
-	Convergence is faster

This impression is confirmed by the following graph of error :  
![SGDError](https://raw.githubusercontent.com/Jeanselme/ImageCompression/master/Images/SGDError.png)  

Compared to the gradient descent mean error :  
![GDError](https://raw.githubusercontent.com/Jeanselme/ImageCompression/master/Images/GDError.png)  

They are not a state of the art compression.  

Here an example on larger image, original one :  
![HighDimension](https://raw.githubusercontent.com/Jeanselme/ImageCompression/master/Images/HighDimension.jpg)  

Compressed with k = 50, after 100 iterations  
![Compressed](https://raw.githubusercontent.com/Jeanselme/ImageCompression/master/Images/Compression-50-100.png)  

The number of features needed to compress an image, seems to be linked to the image and not its dimension (We observe similar mean error with k = 50 for smaller dimension).

## Libraries
Needs numpy, scipy and sys. Compiled with python3.5
