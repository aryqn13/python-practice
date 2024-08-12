#let us implement bubble sort in python.
# Bubble Sort is an algorithm that sorts an array from the lowest value to the highest value.
my_arr = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(my_arr)

for i in range(n-1):
    for j in range(n-i-1):
        if my_arr[j] > my_arr[j+1]:
            my_arr[j],my_arr[j+1] = my_arr[j+1],my_arr[j]

print(f"the sorted array is {my_arr}")

# the time complexity is O(n^2) / because of two loops
# O(n^2) in avg and worst case and O(n) in best case scenario