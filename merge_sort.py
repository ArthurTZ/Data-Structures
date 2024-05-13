

### - Merge Sort utiliza o divide and conquer algorithm 
### - ou seja, divide no meio o array em duas partes, orderna-os e depois junta para um so array ordenado

def mergeSort(array : list):
    if len(array) > 1:
        left_array = array[:len(array)//2]
        right_array = array[len(array)//2:]

        mergeSort(left_array)
        mergeSort(right_array)

    # merge step
        i = 0 # - left array index
        j = 0 # - right_array index
        k = 0 # - Merge array index
        
        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                array[k] = left_array[i]
                i +=1
            else:
                array[k] = right_array[j]
                j+= 1
            k+=1
        while i < len(left_array):
            array[k] = left_array[i]
            i += 1
            k += 1

        while j < len(right_array):
            array[k] = right_array[j]
            j+=1
            k+=1


# give an array of intengers unordered from 0 to 10

array = [2,3,5,1,7,4,4,4,2,6,0]
mergeSort(array)
print(array)