ufscar-2014-graph-theory-task5a
===============================

This is the code for the fifth task from Graph Theory course on UFSCar (Universidade Federal de São Carlos), on the second semester of 2014, taught by Professor Doctor Alexandre Levada.

T5a: O Problema do Caixeiro Viajante
O programa deve ler um grafo Hamiltoniano ponderado a partir de um arquivo qualquer e através de um algoritmo visto em sala (2-otimal ou Twice-Around) obter 10 soluções diferentes para o problema do caixeiro-viajante.

METODOLOGIA

Para obter soluções distintas para o problema há algumas heurísticas comumente adotadas na prática: utilizar diferentes inicializações, ou seja, soluções iniciais. Elas podem ser geradas simplesmente aletoriamente (selecionando vértices quaisquer) ou utilizando alguma heurística, como por exemplo a escolha do vizinho mais próximo por exemplo. Dessa forma, escolhe-se aleatoriamente apenas o primeiro vértice do ciclo (v0) e depois sempre é escolhido como próximo elemento da sequência o vizinho mais próximo do vértice atual, até que o ciclo Hamiltoniano seja formado (não sobre mais vértices). 

OBS: Em caso de implementação do algoritmo Twice-Around utilize alguma função presente na biblioteca NetworkX para a geração de circuitos Eulerianos (que implemente o algoritmo de Fleury ou uma variante). Isso facilita significativamente o desenvolvimento.

QUESTIONAMENTOS

Liste as 3 melhores soluções e as 3 piores obtidas. Qual a diferença de custo entre a melhor e a pior? Discuta como a diferença pode ser significativa.

a) Considere o grafo a seguir de 59 vértices

WG59
Matriz de adjacência com as distâncias entre os pontos para o grafo de 59 vértices
Nomes dos vértices (cidades da Alemanha)


b) Considere o grafo a seguir de 128 vértices
US128
Matriz de adjacência com as distâncias entre os pontos para o grafo de 128 vértices
Nomes dos vértices (cidades dos EUA)

c) Considere o grafo a seguir de 30 vértices (HA30). 
30 cidades
Matriz de adjacência com as distâncias entre os pontos para o grafo de 30 vértices
Nomes dos vértices (30 cidades do mundo) 


Alguns datasets reais adicionais podem ser encontrados em http://people.sc.fsu.edu/~jburkardt/datasets/cities/cities.html ou http://www.math.uwaterloo.ca/tsp/data/ ou http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/
