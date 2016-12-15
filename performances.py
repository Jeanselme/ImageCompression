import scipy.misc
from compression import compression

fileName = 'Images/PolarLight.jpg'
image = scipy.misc.imread(fileName)
dim = image.shape[0]*image.shape[1]*image.shape[2]
ks = range(10,61,10)
ites = range(1,100,10)

errors = []

for ite in ites:
	for k in ks:
		p,q,res,error = compression(image, k, ite)
		newDim = k*(image.shape[0] + image.shape[1])*image.shape[2]
		output = "Images/{}-{}-{}.png".format(k, ite, 100*newDim/dim)
		print("Image compressed with a k = {}, with {} iterations -> {}".format(k, ite, error))

		errors.append(error)
		scipy.misc.imsave(output, res)
