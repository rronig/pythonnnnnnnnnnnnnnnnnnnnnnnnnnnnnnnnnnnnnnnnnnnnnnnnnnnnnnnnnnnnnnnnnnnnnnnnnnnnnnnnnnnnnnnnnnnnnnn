import numpy as np
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr_2d)
element=arr_2d[1,2]
print(element)
dimensions=arr_2d.ndim
arr_shape=arr_2d.shape
print(arr_shape)
print(dimensions)
sub_array=arr_2d[:1, :3]
print(sub_array)
sub_array2=arr_2d[:1:2]
sub_array3=arr_2d[:, ::2]
total_sum=np.sum(arr_2d)
print(total_sum)
average=np.average(arr_2d)
print(average)
mean=np.mean(arr_2d)
print(mean)
sum_columns=np.sum(arr_2d, axis=0)
sum_rows=np.sum(arr_2d, axis=1)
print(sum_columns)
print(sum_rows)
reshaped_array = np.reshape(arr_2d, (1,))
print(reshaped_array)