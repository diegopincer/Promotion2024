# Exercises à rendre

## 1.1 Question du cours


1. Scénario sans interblocage :
Dans un système où les processus et les ressources sont bien gérés, un scénario sans interblocage peut se produire. Par exemple, si un système d'exploitation utilise un algorithme d'ordonnancement des ressources qui évite les conditions de Coffman (exclusion mutuelle, détention et attente, absence de préemption, attente circulaire), un interblocage peut être évité. Un autre exemple pourrait être un système où les processus demandent toutes les ressources dont ils ont besoin en une seule fois et les libèrent toutes ensemble une fois qu'ils ont terminé, empêchant ainsi les dépendances cycliques entre les processus.

2. Scénario avec interblocage :
Un scénario avec interblocage pourrait se produire dans un système où plusieurs processus exécutent des tâches qui nécessitent des ressources partagées. Si chaque processus détient une ressource tout en attendant une autre ressource déjà détenue par un autre processus, et si cette attente crée un cycle de dépendances, alors le système est dans un état d'interblocage. Par exemple, si le Processus A détient la Ressource 1 et attend la Ressource 2, qui est détenue par le Processus B, qui attend à son tour la Ressource 1, nous avons une situation d'interblocage.

Quant à la probabilité d'avoir un interblocage, elle dépend fortement de la conception du système et de l'algorithme d'ordonnancement utilisé. Dans les systèmes bien conçus avec des mécanismes de prévention ou d'évitement des interblocages, la probabilité peut être très faible. Cependant, dans les systèmes complexes où de nombreux processus interagissent avec plusieurs ressources de manière non coordonnée, la probabilité peut être plus élevée.

## 1.2 Question du cours nº2

En sachant  que la partie qu’elle exécute en parallèle représente en temps de traitement 90% du temps d’exécution du programme en séquentiel et que  n ≫ 1. 

$$
 S(n) = \frac{1}{(1 - p) + \frac{p}{n}} 
$$
$$
 \lim_{n\to\infty} S(n) = \frac{1}{1-p} = \frac{1}{1 - 0.9} = \frac{1}{0.1} = 10
$$

En supposant que le gaspillage des ressources CPU commence lorsque l'accélération dépasse 70% de son maximum théorique, nous pouvons déterminer un nombre raisonnable de nœuds de calcul comme suit :

$$
 S(n) = \frac{1}{(1 - p) + \frac{p}{n}} = 7
$$
$$
 n = 21
$$

Donc, le nombre de nœuds de calcul qui semble raisonnable est 21.

Soit la loi de Gustafson et sachant que Alice obtient une accélération maximale
de quatre en augmentant le nombre de nœuds de calcul pour son jeu spécifique de données.
$$
 S(n) = n + (1 - n)*t_s = 4
$$
$$
  n + (1 - n)*0.9 = 4
$$
$$
  n  = 31
$$

## 1.3 Ensemble de mandelbrot

  Pour le code sans parélisation on a

    Temps du calcul de l'ensemble de Mandelbrot : 6.729634761810303

    Temps de constitution de l'image : 0.08461761474609375

### 1.3.1 Partition équitable par ligne
### 1.3.2 Le stratégie maître–esclave


## 1.4 Produit matrice–vecteur

    Temps utilisé sans parélisation: 0.009897232055664062 secondes

### 1.4.1 Produit parallèle matrice – vecteur par colonne

    Temps utilisé avec parélisation par colum (1 processus): 0.0037217140197753906 secondes

    Temps utilisé avec parélisation par colum (2 processus): 0.0012526512145996094 secondes

    Temps utilisé avec parélisation par colum (4 processus): 0.0009002685546875012 secondes

### 1.4.2 Produit parallèle matrice – vecteur par ligne

    Temps utilisé avec parélisation par ligne (1 processus): 0.0011188983917236328 secondes

    Temps utilisé avec parélisation par ligne (2 processus): 3.242492675781250e-05 secondes 

    Temps utilisé avec parélisation par ligne (4 processus): 0.528594970703125e-05 secondes