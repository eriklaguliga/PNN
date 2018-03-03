import numpy
import math
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as pl
import operator
data_train = numpy.genfromtxt("data_train_PNN.txt",skip_header=1)
data_test = numpy.genfromtxt("data_test_PNN.txt",skip_header=1)
xyz = pl.figure().add_subplot(111,projection='3d')

# xyz.scatter(data_train[:,0],data_train[:,1],data_train[:,2])
# # pl.show()

# print(data_train[:,3])
def pdf(xtrain,ytrain,ztrain,xtest,ytest,ztest):
    param = 0.1
    pdf = math.exp(-((((xtest - xtrain) ** 2) + ((ytest - ytrain) ** 2) + ((ztest - ztrain) ** 2)) / (2 * (param) ** 2)))
    return pdf

#implementasi

a = []
b = []
gausian1 = []
gausian2 = []
gausian3 = []
sumgausian1 = 0
sumgausian2 = 0
sumgausian3 = 0
a = 0
kelas = []
for i in data_test:

    for j in data_train:
        if(j[3] == 0):
            sumgausian1 = sumgausian1 + (pdf(j[0],j[1],j[2],i[0],i[1],i[2]))
        elif(j[3] == 1):
            sumgausian2 = sumgausian2 + (pdf(j[0], j[1], j[2], i[0], i[1], i[2]))
        elif(j[3] == 2):
            sumgausian3 = sumgausian3 + (pdf(j[0], j[1], j[2], i[0], i[1], i[2]))
    a= max(sumgausian1,sumgausian2,sumgausian3)
    # print(a)
    if a == sumgausian1 :
        kelas.append(0)
    elif a == sumgausian2:
        kelas.append(1)
    else:
        kelas.append(2)
    sumgausian1 = 0
    sumgausian2 = 0
    sumgausian3 = 0



kelas = numpy.asarray(kelas)
print(kelas)
data_test = numpy.concatenate((data_test, kelas[:,None]), axis=1)
print(data_test)


xyz.scatter(data_test[:,0],data_test[:,1],data_test[:,2], c=data_test[:,3])
pl.show()