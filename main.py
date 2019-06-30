from arrays_solutions import ArraySolver


lista = [1, 2, 3, 6, 4]
unsorted_list = [1, 312, 2, 123, 44, 45, 5, 12121, 333, 311, 312, 0]
lista_duplicada = [1, 2, 3, 6, 4, 5, 3, 3, 3, 1, 9]

print(ArraySolver.find_missing_number(lista, len(lista) + 1))

print(ArraySolver.remove_duplicate_from_list(lista_duplicada))

print(ArraySolver.get_duplicated_from_list(lista_duplicada))

print(ArraySolver.get_largest_smallest_number(unsorted_list))

print(ArraySolver.get_pair_of_sum_n_2(lista_duplicada, 7))

print(ArraySolver.get_pair_of_sum_n(lista_duplicada, 7))

print(ArraySolver.get_pair_of_sum_wo_repeated(lista_duplicada, 7))

print(ArraySolver.quicksort(unsorted_list))
