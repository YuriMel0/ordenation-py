def my_selection_sort(lista):
    n = len(lista)

    for i in range(0, n):

        index_min = i

        for j in range(i+1, n):

            if lista[j] < lista[index_min]:

                index_min = j

        lista[i], lista[index_min] = lista[index_min], lista[i]

    return lista

 
 

lista = [10, 9, 5, 8, 11, -1, 3]

my_selection_sort(lista)

print(lista)