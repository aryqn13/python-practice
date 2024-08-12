#let us start with arrays in python

my_arr = [8,15,10,7,5,6,9,2,17,4,3,21]

min_val = my_arr[0]

for i in my_arr:
    if i < min_val:
        min_val = i

print(f"{min_val} is the lowest value in the array")
# this code prints an array in python using list data type and finds the lowest element from the array
# # this program uses the given algo
# Variable 'minVal' = array[0]
# For each element in the array
#     If current element < minVal
        # minVal = current element