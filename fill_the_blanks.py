# Given an array containing None values fill in the None values with most recent 
# non None value in the array 

array1 = [1,None,2,3,None,None,5,None]
array2 = [None,2,3,None,None,5,None]
array3 = []

def fill_the_blanks(array):
    latest = 0 #if the first item is None sets it to 0
    for index, item in enumerate(array):
        if item is not None: #same as !=
            latest = item
        else:
            array[index] = latest
    return array

print(fill_the_blanks(array1))
print(fill_the_blanks(array2))
print(fill_the_blanks(array3))

