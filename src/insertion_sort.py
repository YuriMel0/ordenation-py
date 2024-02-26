def my_insertion_sort(lista):

    n = len(lista)

    for i in range(1, n):

        value_insert = lista[i] 
        j = i - 1
        while j >= 0 and lista[j] > value_insert:

            lista[j + 1] = lista[j]

            j -= 1
        lista[j + 1] = value_insert

    return lista

 

lista = [10, 9, 5, 8, 11, -1, 3]
my_insertion_sort(lista)
print(lista)