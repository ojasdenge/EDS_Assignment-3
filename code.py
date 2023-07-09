import numpy as np 

# Reading a dataset into an array: 
'''data1 = np.read_csv("/content/drive/MyDrive/Colab Notebooks/Files/dataset1.csv") 
data2 = np.read_csv("/content/drive/MyDrive/Colab Notebooks/Files/dataset2.csv")''' 
data1 = np.genfromtxt('/content/drive/MyDrive/Colab Notebooks/Files/dataset1.csv', delimiter=',', skip_header=1) 
data2 = np.genfromtxt('/content/drive/MyDrive/Colab Notebooks/Files/dataset2.csv', delimiter=',', skip_header=1) 

# Performing all matrix operations:
 # Matrix addition addition = np.add(data1, data2)
print("Matrix Addition:") 
print(addition)
print() 

# Matrix subtraction 
subtraction = np.subtract(data1, data2) 
print("Matrix Subtraction:") 
print(subtraction)
print()

# Matrix multiplication 
multiplication = np.multiply(data1, data2) 
print("Matrix Multiplication:")
print(multiplication) print() 

# Matrix division division = np.divide(data1, data2) 
print("Matrix Division:") 
print(division) print() 

# Matrix dot product 
dot_product = np.dot(data1, data2.T) 
print("Matrix Dot Product:") 
print(dot_product)
print() 

# Matrix transpose 
transpose = data1.T 
print("Matrix Transpose:") 
print(transpose) print()

# Horizontal and vertical stacking of NumPy arrays: 
# Horizontal stacking 
horizontal_stack = np.hstack((data1, data2)) 
print("Horizontal Stack:") 
print(horizontal_stack) 
print() 

# Vertical stacking 
vertical_stack = np.vstack((data1, data2)) 
print("Vertical Stack:") 
print(vertical_stack) 
print()

# Arithmetic and Statistical Operations, Mathematical Operations, Bitwise Operators: 
# Arithmetic operations addition = np.add(data1, data2) 
print("Addition:") 
print(addition) 

print() subtraction = np.subtract(data1, data2) 
print("Subtraction:") 
print(subtraction) 

print() multiplication = np.multiply(data1, data2) 
print("Multiplication:") 
print(multiplication) 

print() division = np.divide(data1, data2)
print("Division:") 
print(division) 
print() 

# Statistical operations mean = np.mean(data1) 
print("Mean of data1:") 
print(mean) 
print() std_dev = np.std(data2) 
print("Standard Deviation of data2:") 
print(std_dev) 
print() 

# Mathematical operations 
square_root = np.sqrt(data1) 
print("Square Root of data1:") 
print(square_root) 
print() exponential = np.exp(data2) 
print("Exponential of data2:") 
print(exponential) 
print()

# Bitwise operators 
# Bitwise AND bitwise_and = np.bitwise_and(data1.astype(int), data2.astype(int)) 
print("Bitwise AND:") 
print(bitwise_and) 
print() 

# Bitwise OR bitwise_or = np.bitwise_or(data1.astype(int), data2.astype(int)) 
print("Bitwise OR:") 
print(bitwise_or) 
print() 

# Bitwise XOR 
bitwise_xor = np.bitwise_xor(data1.astype(int), data2.astype(int)) 
print("Bitwise XOR:") 
print(bitwise_xor) 
print() 

# Bitwise NOT 
bitwise_not_data1 = np.bitwise_not(data1.astype(int)) 
print("Bitwise NOT of data1:") 
print(bitwise_not_data1) 
print() 
bitwise_not_data2 = np.bitwise_not(data2.astype(int))
print("Bitwise NOT of data2:") 
print(bitwise_not_data2) 
print()

# Data Stacking, Searching, Sorting, Counting, Broadcasting: 
# Data stacking 
stacked_data = np.stack((data1, data2), axis=0) print("Data Stacking:") 
print(stacked_data) 
print() 

# Searching index = np.where(data1 == 27.79) 
print("Index where data1 equals 27.79:") 
print(index) 
print() 

# Sorting sorted_data = np.sort(data1) 
print("Sorted data1:") 
print(sorted_data) 
print() 

# Counting
count = np.count_nonzero(data1 > 30) 
print("Count of elements in data1 greater than 30:") 
print(count) 
print() 

# Broadcasting 
broadcasted_data = data1 * 2 print("Broadcasted data1 (multiplied by 2):") 
print(broadcasted_data) 
print()