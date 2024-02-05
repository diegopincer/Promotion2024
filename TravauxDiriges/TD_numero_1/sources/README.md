
# TD1

`pandoc -s --toc README.md --css=./github-pandoc.css -o README.html`


## lscpu

```
Architecture:            x86_64
  CPU op-mode(s):        32-bit, 64-bit
  Address sizes:         48 bits physical, 48 bits virtual
  Byte Order:            Little Endian
CPU(s):                  8
  On-line CPU(s) list:   0-7
Vendor ID:               AuthenticAMD
  Model name:            AMD Ryzen 5 7520U with Radeon Graphics
    CPU family:          23
    Model:               160
    Thread(s) per core:  2
    Core(s) per socket:  4
    Socket(s):           1
    Stepping:            0
    BogoMIPS:            5589.10  
Caches (sum of all):     
  L1d:                   128 KiB (4 instances)
  L1i:                   128 KiB (4 instances)
  L2:                    2 MiB (4 instances)
  L3:                    4 MiB (1 instance)
```
  


*Des infos utiles s'y trouvent : nb core, taille de cache*


## Produit matrice-matrice

./TestProductMatrix.exe 1023
des temps d'éxécution : 1.16348 1.2476 1.23093 1.17585 1.21549 ≈ 1.20667 secondes (temps moyenne)

./TestProductMatrix.exe 1024
des temps d'éxécution : 8.93566 9.61354 9.53859 8.92176 9.84893 ≈  9.3717 secondes (temps moyenne)

./TestProductMatrix.exe 1025
des temps d'éxécution : 1.32846 1.37041 1.33926 1.32098 1.30887 ≈ 1.3338 secondes (temps moyenne)

### Permutation des boucles

*Expliquer comment est compilé le code (ligne de make ou de gcc) : on aura besoin de savoir l'optim, les paramètres, etc. Par exemple :*

`make TestProduct.exe && ./TestProduct.exe 1024`


La commande make TestProduct.exe && ./TestProduct.exe 1024 compile et exécute un programme de multiplication de matrices en C++, en utilisant un Makefile pour spécifier les fichiers sources et les options de compilation. Les options incluent -O3 pour une optimisation avancée, -fopenmp pour activer le support de parallélisation avec OpenMP, et -march=native pour optimiser le code pour l'architecture spécifique du processeur. Après la compilation, le programme TestProduct.exe est exécuté avec 1024 comme argument, indiquant la taille des matrices à multiplier, permettant ainsi d'évaluer la performance de l'opération de multiplication matricielle sur des matrices de dimension 1024x1024, en tirant parti des optimisations et de la parallélisation pour améliorer les temps d'exécution.


  ordre           | time    | MFlops  | MFlops(n=2048) 
------------------|---------|---------|----------------
i,j,k (origine)   | 10.485  | 204.814 |   117.718            
j,i,k             | 9.78632 | 219.437 |   126.256
i,k,j             | 30.1366 | 71.2582 |   83.9838
k,i,j             | 27.8307 | 77.1624 |   82.3909
j,k,i             | 0.83477 | 2572.54 |   2691.77
k,j,i             | 1.23744 | 1735.43 |   1729.31


*Discussion des résultats*

L'ordre des boucles dans un programme de multiplication de matrices peut fortement influencer le temps d'exécution, en raison de la manière dont les données sont accédées en mémoire. Sur les processeurs modernes, l'accès à la mémoire est plus rapide pour des données lues séquentiellement, grâce à l'utilisation des caches, qui sont des petites zones de mémoire rapide stockant temporairement les données pour diminuer le temps d'accès.

Dans la multiplication de matrices, on additionne les produits des éléments des deux matrices. La base de l'opération ressemble à C[i][j] += A[i][k] * B[k][j]. Il existe trois boucles imbriquées pouvant être arrangées de six manières différentes, représentant les différentes façons d'itérer à travers les matrices A, B et C.
La localité spatiale est exploitée en accédant séquentiellement à des données contiguës, ce qui est rapide une fois que le bloc de données est chargé dans le cache. La localité temporelle réutilise les données accédées récemment, comme les éléments de A ou B utilisés dans différentes additions pour C, en les gardant dans le cache le plus longtemps possible. Les matrices en C++ sont généralement stockées en mémoire ligne par ligne, il est donc préférable d'itérer d'abord sur les indices de colonne à l'intérieur d'une ligne.

La permutation des boucles jki (ou kji) est souvent la plus efficace pour la multiplication de matrices. Dans la boucle la plus interne, un élément fixe de B est multiplié par une ligne entière de A, et le résultat est accumulé dans une position fixe de C, ce qui maintient l'accès contigu aux éléments de C et A et réutilise plusieurs fois un élément de B.


### OMP sur la meilleure boucle 

`make TestProduct.exe && OMP_NUM_THREADS=8 ./TestProduct.exe 1024`

  OMP_NUM         | MFlops  | MFlops(n=2048) | MFlops(n=512)  | MFlops(n=4096)
------------------|---------|----------------|----------------|---------------
1                 | 2658.82 |     2849.82    |     3507.41    |    2591.98
2                 | 5256.29 |     4945.41    |     6098.38    |    4730.52
3                 | 6626.06 |     5070.34    |     6820.68    |    6451.29
4                 | 7349.39 |     7619.30    |     7553.94    |    7368.80
5                 | 8497.28 |     8503.03    |     9406.10    |    8074.01
6                 | 9350.42 |     9038.22    |     9911.62    |    8175.17  
7                 |10124.07 |     9196.18    |    10071.5     |   10071.50
8                 |11645.60 |     8776.89    |     8680.43    |    8193.55

Pour améliorer le résultat obtenu dans une opération de produit matrice-matrice parallélisée avec OpenMP, il est crucial d'optimiser la gestion des threads et la répartition de la charge de travail. Une répartition inégale peut entraîner des threads inactifs tandis que d'autres finissent leur travail, ce qui affecte l'efficacité globale. L'utilisation de techniques telles que le scheduling dynamique, la réduction des surcoûts de synchronisation et l'optimisation de l'accès à la mémoire (comme la minimisation des conflits de cache et l'utilisation efficace de la localité des données) peut conduire à des gains significatifs. De plus, s'assurer que le nombre de threads ne dépasse pas le nombre de cœurs physiques disponibles peut éviter une concurrence inutile pour les ressources du processeur, tandis que l'ajustement des options de compilation pour une meilleure vectorisation et l'utilisation des capacités intrinsèques du processeur peuvent également contribuer à améliorer les performances.


### Produit par blocs

`make TestProduct.exe && ./TestProduct.exe 1024`

  szBlock         | MFlops  | MFlops(n=2048) | MFlops(n=512)  | MFlops(n=4096)
------------------|---------|----------------|----------------|---------------
origine (=max)    |11602.2  |      9242.24   |     8943.12    |    8093.75 
32                | 4518.06 |      3831.5    |     1456.48    |    4448.85
64                |10578.10 |      8869.32   |     4736.01    |    9095.49
128               | 9946.2  |      9629.73   |     6521.14    |    6984.15
256               |11636.4  |      6323.22   |     7816.02    |    7589.72 
512               |10363.4  |      8796.12   |     9647.56    |    7336.07
1024              |9887.33  |      9482.43   |     9018.7     |    8825.7


Meilleure utilisation du cache : La multiplication par blocs tire généralement mieux parti du cache du CPU car elle traite de petites portions de données à la fois, améliorant la localité spatiale et temporelle et réduisant le besoin d'accéder à la mémoire principale.

Parallélisme : La multiplication par blocs peut être plus facilement parallélisée, permettant à plusieurs cœurs de travailler sur différents blocs simultanément, ce qui n'est pas aussi direct dans la multiplication scalaire.

Surcoût de gestion : Bien que la multiplication par blocs puisse être plus efficace pour le cache, elle peut introduire un surcoût supplémentaire de gestion des blocs, ce qui peut affecter la performance si la taille du bloc n'est pas correctement choisie.

Efficacité matérielle : Certaines architectures matérielles peuvent bénéficier davantage de la multiplication par blocs que d'autres, selon des facteurs tels que la taille du cache et la vitesse de la mémoire.

### Bloc + OMP



  szBlock      | OMP_NUM | MFlops  | MFlops(n=2048) | MFlops(n=512)  | MFlops(n=4096)|
---------------|---------|---------|-------------------------------------------------|
A.nbCols       |  1      |   2590  |     1963.46    |     3294.21    |    1918.32    |
512            |  8      |  10845  |     8798.29    |     9140.85    |    7827.58    |
               |         |         |                |                |               |
Speed-up       |         |   4.18  |      4.48      |       2.77     |      4.08     |
               |         |         |                |                |               |

Pour interpréter les résultats, il faut considérer l'efficacité avec laquelle chaque thread peut travailler sans interférence ou attente inutile, ainsi que l'aptitude du matériel à gérer le parallélisme. Des gains significatifs avec le produit par blocs suggèrent une meilleure exploitation des ressources parallèles et du cache, tandis que des résultats similaires ou inférieurs pourraient indiquer des goulots d'étranglement dans l'accès aux données ou une saturation des ressources disponibles.


### Comparaison with BLAS

OMP_NUM_THREADS=8 ./TestProductMatrix.exe
Test passed
Temps CPU produit matrice-matrice naif : 0.261465 secondes
MFlops -> 8213.28

./TestProductMatrix.exe
Test passed
Temps CPU produit matrice-matrice naif : 0.316114 secondes
MFlops -> 6793.39 

./test_product_matrice_blas.exe
Test passed
Temps CPU produit matrice-matrice blas : 0.84908 secondes
MFlops -> 2529.19

# Tips 

```
	env 
	OMP_NUM_THREADS=4 ./produitMatriceMatrice.exe
```

```
    $ for i in $(seq 1 4); do elap=$(OMP_NUM_THREADS=$i ./TestProductOmp.exe|grep "Temps CPU"|cut -d " " -f 7); echo -e "$i\t$elap"; done > timers.out
```
