import sys
import numpy as np
import numpy.random as random
import scipy.misc

def compression(image, k, maxIter):
	"""
	Computes a matrix factorization of an image in order to compress it
	Thanks to gradient descent
	image = P * Q
	"""
	# Random initial centroids
	p = random.rand(image.shape[0], k, image.shape[2])
	q = random.rand(k, image.shape[1], image.shape[2])

	# Normalization
	normImage = np.copy(image)/255
	res = np.zeros(image.shape)
	for iteration in range(maxIter):
		print("Iteration {} / {}".format(iteration+1, maxIter))
		# Loop over all pixel
		for i in range(image.shape[0]):
			for j in range(image.shape[1]):
				for c in range(image.shape[2]):
					pixel = normImage[i,j,c]
					eij = np.dot(p[i,:,c],q[:,j,c]) - pixel
					for ki in range(k):
						old = p[i,ki,c]
						p[i,ki,c] -= 2*q[ki,j,c]*eij/k
						q[ki,j,c] -= 2*old*eij/k
	error = 0
	dim = image.shape[0] * image.shape[1] * image.shape[2]
	for i in range(image.shape[0]):
		for j in range(image.shape[1]):
			for c in range(image.shape[2]):
				res[i,j,c] = np.dot(p[i,:,c],q[:,j,c])*255
				error += (res[i,j,c] - image[i,j,c])**2/(dim)

	return p,q,res,error

def help():
    print("python3.5 compression.py FileName.png [-k int] [-i int] [-o resultFileName]")
    quit()

def main():
    arg = sys.argv
    if len(arg) < 2:
        help()
    elif ".png" in arg[1] or ".jpg" in arg[1] :
        fileName = arg[1]
        output = ""
        i = 2
        k = 3
        ite = 3

        # Parse the command line
        while i+1 < len(arg):
            if arg[i] == "-k":
                k = int(arg[i+1])
                i+=2
            elif arg[i] == "-i":
                ite = int(arg[i+1])
                i+=2
            elif arg[i] == "-o":
                output = arg[i+1]
                i+=2
            else :
                help()

        if (k <= 0 or ite <= 0):
            help()
        else:
            image = scipy.misc.imread(fileName)
            p, q, res, error = compression(image, k, ite)
            print("Image compressed with a k = {} with {} iterations -> {}".format(k, ite, error))
            if (output != ""):
                scipy.misc.imsave(output, res)
            else:
                scipy.misc.imshow(res)

    else:
        help()

if __name__ == '__main__':
    main()
