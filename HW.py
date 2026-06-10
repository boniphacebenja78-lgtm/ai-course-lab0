import sympy as sp

#present the matrix in 4*5 system.
A = sp.Matrix([[8, 11, -6, -7, 13],
               [-7, -8, 5, 6, -9],
               [11, 7, -7, -9, -6],
               [-3, 4, 1, 8, 7]])

#find the Reduced Row Echelon Form
rref_matrix, pivot_columns = A.rref()

#result to be printed
print("RREF:")
print(rref_matrix)

print("pivot column:")
print(pivot_columns)