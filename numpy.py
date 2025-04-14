import numpy as np
# from time import process_time
# python_list=[i for i in range(1000000)]
# start_time=process_time()
# python_list=[i+5 for i in python_list]

# end_time=process_time()
# print("The time taken is " + str(end_time - start_time))



# # numpy array
# np_arr=np.array([i for i in range(10000000)])
# start_time=process_time()
# np_arr+=5
# end_time=process_time()
# print("The time taken is " + str(end_time - start_time))

# # array of a particular value
# z=np.full((3,3),6)
# print(z)

# # crate an identity matrix
# a=np.eye(3)
# print(a)

# # create numpy with random values
# b=np.random.random((2,2))
# print(b)

# creare numpy with random intergers in specific range

c=np.random.randint(10,20,(1,4))
print(c.ndim)

# # array of evenly spaced array
# d=np.linspace(10,40,7)
# print(d)

# # converting a list into numpy array
# list=[10,20,30,40,50];
# np_array=np.asarray(list)
# print(np_array)