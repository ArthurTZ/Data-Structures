
def quickSort(array : list):
    if len(array) <=1:
        return array
    
    pivot_point = array[len(array) // 2]
    left = [x for x in array if x < pivot_point]
    middle = [x for x in array if x == pivot_point]
    right = [x for x in array if x > pivot_point]
    return quickSort(left) + middle + quickSort(right)

array = [2, 3, 5, 1, 7, 4, 4, 4, 2, 6, 0]
array_ordenado = quickSort(array)
print("Array ordenado:", array_ordenado)