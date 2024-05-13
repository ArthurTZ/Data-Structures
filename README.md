# Data-Structures
data structures in Python

## - Insertion_sort:
### - Sort 
- (Basically used to sort a data structure - O(n^2))
### - Using built-in functions:
  ```python
  def sort_list(array: list) -> list:
      return array.sort()
  
  array = [6, 3, 4, 1, 2]
  # print(sort_list(array))
  ```
## - Insertion Sort Manually
```python
def insertion_sort(array: list) -> None:
    for index in range(1, len(array)):
        compare = index
        while array[compare - 1] > array[compare] and compare > 0:
            array[compare - 1], array[compare] =  array[compare], array[compare - 1]
            compare -= 1
insertion_sort(array)     
print(array)
```
## - Merge Sort:
  ### - Utilizes the divide and conquer algorithm, dividing the array in two parts, sorting them, and then merging them into a single sorted array.
```python
def mergeSort(array: list):
    if len(array) > 1:
        left_array = array[:len(array)//2]
        right_array = array[len(array)//2:]

        mergeSort(left_array)
        mergeSort(right_array)

        # Merge step
        i = 0  # Left array index
        j = 0  # Right array index
        k = 0  # Merge array index

        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                array[k] = left_array[i]
                i += 1
            else:
                array[k] = right_array[j]
                j += 1
            k += 1

        while i < len(left_array):
            array[k] = left_array[i]
            i += 1
            k += 1

        while j < len(right_array):
            array[k] = right_array[j]
            j += 1
            k += 1

# Give an array of integers unordered from 0 to 10

array = [2, 3, 5, 1, 7, 4, 4, 4, 2, 6, 0]
mergeSort(array)
print(array)
```
## - QuickSort:
  ### - Selection Sort Manually
```python
def selectionSort(array: list):
    for index in range(0, len(array) - 1):
        cur_min = index
        for j in range(index + 1, len(array)):
            if array[j] < array[cur_min]:
                cur_min = j

        array[index], array[cur_min] = array[cur_min], array[index]  # Swap values

array = [2, 6, 5, 1, 3, 4]
selectionSort(array)
print(array)

```



