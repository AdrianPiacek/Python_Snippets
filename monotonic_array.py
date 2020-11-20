# Given an array of integers, determine whether the array is monotonic or not.
A = [6, 5, 4, 4] 
B = [1,1,1,3,3,4,3,2,4,2]
C = [1,1,2,3,7]

def monotonic_array(array):

    return all(array[i] <= array[i+1] for i in range(len(array) - 1)) or \
           all(array[i] >= array[i+1] for i in range(len(array) -1))


print(monotonic_array(A))
print(monotonic_array(B))
print(monotonic_array(C))
