def OrdenarSeleccion(Numeros):
    
    # (int i = 0 ; i < n-1 ; i++)
    for i in range(len(Numeros)-1):

        min = i
        # (int = j = i + 1 ; i < n ; i++ )
        for j in range(i + 1, len(Numeros)):

            if Numeros[j] < Numeros[min]:

                min = j

        if min != i:

            Numeros[i], Numeros[min] = Numeros[min], Numeros[i]




def insertion_sort_insert(A, nuevo_dato):
    A += [0]  
    A[len(A)-1] = nuevo_dato  

    i = len(A) - 1
    while i > 0 and A[i - 1] > A[i]:
        A[i], A[i - 1] = A[i - 1], A[i]
        i -= 1

lista = [11, 22, 33, 44, 55]
print("Lista inicial:", lista)

nuevo = int(input("Inserte un dato: "))

insertion_sort_insert(lista, nuevo)

print("Lista actualizada y ordenada:", lista)
