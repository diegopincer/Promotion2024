from mpi4py import MPI
import numpy as np

# Initialisation de MPI
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

# Le processus 0 génère des nombres aléatoires
if rank == 0:
    # Génère un tableau de nombres aléatoires
    arr_size = 100  # Taille du tableau
    data = np.random.rand(arr_size)
    # Détermine la taille des sous-tableaux pour la distribution aux processus
    chunk_sizes = [arr_size // size] * size
    for i in range(arr_size % size):
        chunk_sizes[i] += 1
    # Détermine les décalages pour chaque sous-tableau
    offsets = [sum(chunk_sizes[:i]) for i in range(size)]
else:
    data = None
    chunk_sizes = None
    offsets = None

# Distribue la taille de chaque sous-tableau à tous les processus
chunk_size = comm.scatter(chunk_sizes, root=0)

# Crée un tampon pour recevoir les sous-tableaux
subarr = np.zeros(chunk_size)

# Distribue les sous-tableaux à chaque processus
comm.Scatterv([data, chunk_sizes, offsets, MPI.DOUBLE], subarr, root=0)

# Chaque processus trie son sous-tableau
subarr.sort()

# Collecte les sous-tableaux triés dans le processus 0
sorted_data = None
if rank == 0:
    sorted_data = np.empty(arr_size, dtype=float)

comm.Gatherv(subarr, [sorted_data, chunk_sizes, offsets, MPI.DOUBLE], root=0)

# Le processus 0 affiche le tableau trié
if rank == 0:
    print("Tableau trié :", sorted_data)
