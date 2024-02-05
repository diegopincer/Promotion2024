from mpi4py import MPI

# Initialisation du communicateur MPI
comm = MPI.COMM_WORLD
rang = comm.Get_rank()
taille = comm.Get_size()  # Doit être une puissance de 2 pour un hypercube

# Vérification si la taille est appropriée pour une topologie hypercube
assert bin(taille).count('1') == 1, "La taille du communicateur doit être une puissance de 2."

valeur = None
if rang == 0:
    valeur = 42  # Valeur initiale

# Détermination des dimensions de l'hypercube
d = int(bin(taille-1)[2:].zfill(rang.bit_length()))

# Diffusion de la valeur à travers l'hypercube
for i in range(d):
    partenaire = rang ^ (1 << i)
    if partenaire < taille:
        if valeur is not None:
            comm.send(valeur, dest=partenaire)
        if rang > partenaire:
            valeur = comm.recv(source=partenaire)

# Affichage de la valeur dans chaque tâche
print(f"Tâche {rang} a reçu la valeur {valeur}")

#Commande pour executer le code:
# mpiexec -n x python hipercubo.py
# x = 2^(dimension de l'hypercube)
