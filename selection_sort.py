

# - Entao basicamente vai iterar sobre o array, marcando o primeiro indice como cur_min e vai encontrar diante da lista um valor menor que foi indicado ou seja se eu tenho uma lista [2,6,5,1,3,4] - o indice 2 vai ser marcado como cur_min e vai encontrar diante da lista um valor menor que ele

### - Selection Sort Manually
def selectionSort(array : list):
    for index in range(0,len(array) - 1):
        cur_min = index
        for j in range( index + 1, len(array) ):
            if array[j] < array[cur_min]:
                cur_min = j

        array[index], array[cur_min] = array[cur_min], array[index] # swap values



array = [2,6,5,1,3,4]
selectionSort(array)
print(array)