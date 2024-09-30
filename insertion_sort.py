
### - Sort - (basicamente é para ordernar uma DS - O(n**2))

### - Using buil-in functions
def sort_list(array : list) -> list:
    return array.sort()

array = [6,3,4,1,2]
# print(sort_list(array))

### - Insertion Sort Manually
def insertion_sort(array : list) -> None:
    for index in range(1,len(array)):
         compare = index
         print(compare)
         while array[compare - 1] > array[compare] and compare > 0:
            array[compare - 1], array[compare] =  array[compare],array[compare-1]
            compare-=1

insertion_sort(array)     
print(array)        