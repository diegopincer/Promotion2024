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

1. 

2.