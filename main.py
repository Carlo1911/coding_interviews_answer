from arrays_solutions import ArraySolver

solver = ArraySolver()

lista = [1, 2, 3, 6, 4]
total = 6
print(solver.find_missing_number(lista, total))

lista_duplicada = [1, 2, 3, 6, 4, 5, 3, 3, 3, 1, 9]
print(solver.remove_duplicate_from_list(lista_duplicada))

lista_duplicada = [1, 2, 3, 6, 4, 5, 3, 3, 3, 1, 9]
print(solver.get_duplicated_from_list(lista_duplicada))
