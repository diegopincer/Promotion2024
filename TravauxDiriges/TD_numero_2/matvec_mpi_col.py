# Produit matrice-vecteur v = A.u parallèle
from mpi4py import MPI
import numpy as np
import time

# Initialisation de MPI
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

# Dimension du problème (peut-être changé)
dim = 120 #N
nbp = size  # Nombre de tâches

# Supposons que N est divisible par nbp
N_loc = dim // nbp

# Initialisation de la matrice A, du vecteur u et du vector resultat v

A = np.array([[(i + j) % dim + 1. for i in range(dim)] for j in range(dim)])
u = np.array([i + 1. for i in range(dim)])
v = np.zeros(dim)

# Distribution des colonnes de A et du vecteur u à tous les processus
# Chaque processus calcule sa propre partie du produit
start_col = rank * N_loc
end_col = (rank + 1) * N_loc
A_local = A[:, start_col:end_col]
u_local = u[start_col:end_col]

# Calcul local
begin = time.time()
v_local = np.dot(A_local, u_local)


# Gather all the partial results to the root process
v = comm.reduce(v_local, op=MPI.SUM, root=0)
end = time.time()


# Le processus racine affiche le résultat
if rank == 0:
    print("Le vecteur résultat v est:", v)
    print(f"Temps utilisé: {end - begin} secondes")


