#Given an array nums, write a function to move all zeroes to the end of it while maintaining the relative order of 
#the non-zero elements.
array1 = [0,1,0,3,12]
array2 = [1,7,0,0,8,0,10,12,0,4]

def move_zeroes(array):
    for item in array:
        if 0 in array:
            array.remove(0)#function remove deletes first appearence of an element
            array.append(0)
    return array


print(move_zeroes(array1))
print(move_zeroes(array2))
