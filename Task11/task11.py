import numpy as np

array = np.array([
    [10, 32, 38, 44, 56],
    [6, 74, 88, 95, 160],
    [110, 192, 213, 164, 15],
    [16, 197, 198, 196, 20],
    [217, 221, 234, 248, 205]
])
subarray = array[1:4, 1:4]
print(subarray)


randomtherrdarray = np.random.random((4,3,2))
print(randomtherrdarray)
slicearray = randomtherrdarray[:2,:,:1]
print(slicearray)

oneDex1 = np.array([2,4,6,8,2,23,5])
fancyindex = oneDex1[[3,4,6]]
print(fancyindex)


twoDex2 = np.array([
    [25,84,32],
    [18,2,23],
    [12,54,23],
    [23,45,13]
])
rows = [0, 2, 3]
columns = [1, 2]
fancytwoDindex  = twoDex2[np.ix_(rows, columns)]
print(fancytwoDindex)


OneDarray = np.array([1,2,53,53,73,1,9,4,23,84,2,9,4,7])
greaterthan10 = []
for num in OneDarray:
    if num > 10:
        greaterthan10.append(num)
print(greaterthan10)


twoDarray = np.random.randint(0, 21, (5, 5))
twoDarray[twoDarray > 15] = 0
print(twoDarray)


array_1d = np.array([23,62,76])
array_2d = np.array([[27,24,2],
                    [6,9,2,],
                    [6,73,9],
                    [23,7,1]])

addedarray = array_2d + array_1d
print(addedarray)


array_1d = np.array([23,62,76])
array_2d = np.array([[27,24,2],
                    [6,9,2,],
                    [6,73,9],
                    [23,7,1]])

productarray = array_2d * array_1d
print(productarray)


twoDex2 = np.array([
    [25,84,32],
    [18,2,23],
    [12,54,23]
    ]) 
array_2d = np.array([
                    [27,24,2],
                    [6,9,2,],
                    [6,73,9],
                            ])

result= twoDex2 + array_2d
print(result)


array3d = np.array([[[2,4,8,4],
                    [23,85,2,66],
                    [24,8,3,321]],
                   [[39,7,3,34],
                    [9,2,8,3],
                    [67,235,75,32]]
                   ])
array2d = np.array([[12,23,63,34]
                   [12,34,6,16]])
addinarray = array3d + array2d
print(addinarray)


array_2d = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])
slicedarray = array_2d[::2, ::2]
array1D = np.array([1, 2])
resultarray = slicedarray + array_1d
print(resultarray)


array_3d = np.arange(24).reshape(4, 3, 2)
subarray3d = array_3d[:2, :, :]
array_2d = np.array([[1, 1], [2, 2], [3, 3]])
resultarray3d = subarray3d - array_2d[:, np.newaxis]
print(resultarray3d)


array_2d = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
diagonal_elements = np.diag(array_2d)
print(diagonal_elements)


array_2d = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
reversed_array = array_2d[:, ::-1]
print(reversed_array)


array_3d = np.arange(120).reshape(4, 5, 6)
sub_array_3d = array_3d[:2, :3, :4]
array_1d = np.array([1, 2, 3, 4])
result_array_3d = sub_array_3d + array_1d
print(result_array_3d)



array_2d = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
array_2d[:, -1] = array_2d[:, 0] + array_2d[:, 1]
print(array_2d)






