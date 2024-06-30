import numpy as np

OneDArray = np.array([1,2,3,4,5,6,7,8,9])
print(OneDArray)

TwoDArray = np.array([[19,14,17],
                     [12,10,5],
                     [13,9,0]])
print(TwoDArray)

ThreeDArray = np.ones((2, 3, 4))
print(ThreeDArray)

ThreeDArrayo = np.zeros((1, 3, 4))
print(ThreeDArrayo)

oneDex1 = np.array([2,4,6,8,2])
oneDex2 = np.array([4,7,1,9,5,])

Sum = oneDex1 + oneDex2
Product = oneDex1 * oneDex2

print(Sum)
print(Product)

twoDex1 = np.array([
    [23,64,4],
    [12,6,3]
])
twoDex2 = np.array([
    [25,84],
    [18,2],
    [12,54]
])
print(twoDex1)
print(twoDex2)

Dotprod = np.dot(twoDex1, twoDex2)
print(Dotprod)

Mean = np.mean(OneDArray)
print(Mean)
Median = np.median(OneDArray)
print(Median)
Std = np.std(OneDArray)
print(Std)

Maximum = np.max(twoDex1)
print(Maximum)
Minimum = np.min(twoDex1)
print(Minimum)

randomnumbers = np.random.normal(0, 1, 1000)
print(randomnumbers)

TwoDRandom = np.random.randint(10, 51, size=(5, 5))
print(TwoDRandom)

cumulativesum = np.cumsum(OneDArray)
print(cumulativesum)

CorelationtwoDarray = np.corrcoef(TwoDArray)
print(CorelationtwoDarray)

roll = np.random.randint(1, 7, size=1000)
unique, counts = np.unique(roll, return_counts=True)
print("result")
for i in range(len(unique)):
    print(f"{unique[i]}\t{counts[i]}")