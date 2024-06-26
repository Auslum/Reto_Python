A = {1, 2, 3, 4, 5}
B = set()
C = {True, "Hola Mundo", 11, False, 8.81}

B.add(2)
B.add(3)
B.add(5)
B.add(7)
B.add(11)
C.discard(11)
C.discard(8.81)
C.clear()
print("A:", A)
print("B:", B)
print("C:", C)
#Operaciones con Conjuntos
union = A | B
print("Union A | B:", union)
print("Union B | A:", B.union(A))
print("Interseccion A & B:", A & B)
print("Interseccion B & A:", B.intersection(A))
print("Diferencia A - B:", A - B)
print("Diferencia B - A:", B.difference(A))
print("Diferencia Simetrica A ^ B:", A ^ B)
print("Diferencia Simetrica B ^ A:", B.symmetric_difference(A))