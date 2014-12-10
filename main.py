#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Thales Menato'
__author__ = 'Daniel Nobusada'

"""
T5a: O Problema do Caixeiro Viajante
O programa deve ler um grafo Hamiltoniano ponderado a partir de um arquivo qualquer e através de um algoritmo visto em
 sala (2-otimal ou Twice-Around) obter 10 soluções diferentes para o problema do caixeiro-viajante.

METODOLOGIA

Para obter soluções distintas para o problema há algumas heurísticas comumente adotadas na prática: utilizar diferentes
inicializações, ou seja, soluções iniciais. Elas podem ser geradas simplesmente aletoriamente (selecionando
 vértices quaisquer) ou utilizando alguma heurística, como por exemplo a escolha do vizinho mais próximo por exemplo.
 Dessa forma, escolhe-se aleatoriamente apenas o primeiro vértice do ciclo (v0) e depois sempre é escolhido como próximo
elemento da sequência o vizinho mais próximo do vértice atual, até que o ciclo Hamiltoniano seja formado (não sobre mais
vértices).

OBS: Em caso de implementação do algoritmo Twice-Around utilize alguma função presente na biblioteca NetworkX para a
geração de circuitos Eulerianos (que implemente o algoritmo de Fleury ou uma variante). Isso facilita significativamente
  desenvolvimento.

QUESTIONAMENTOS

Liste as 3 melhores soluções e as 3 piores obtidas. Qual a diferença de custo entre a melhor e a pior? Discuta como a
diferença pode ser significativa.
"""

import networkx as nx
from prim import prim
import load_graph
import os
import matplotlib.pyplot as plt

dataset = [('ha30_dist.txt','ha30_name.txt'), ('sgb128_dist.txt','sgb128_name.txt'), ('wg59_dist.txt','wg59_name.txt')]


# Itera entre cada dataset
for data in dataset:
    G = load_graph.load_graph(os.path.abspath('..')+'\\ufscar-2014-graph-theory-task5a\\Datasets\\'+data[0],
                              os.path.abspath('..')+'\\ufscar-2014-graph-theory-task5a\\Datasets\\'+data[1])

    # Aplica o algoritmo de Prim para 10 árvores diferentes
    msts = []
    for i in range(10):
        T = prim(G)
        # Transforma o Grafo em um Digrafo e o coloca em um vetor de 10 posicoes
        mst_digraph = T.to_directed()
        msts.append((mst_digraph))

    # Aplica a busca de caminhos eulerianos

    # Verificacao que a arvore eh euleriana
    # if nx.is_eulerian(mst_digraph) == True:
    #    print "A arvore eh euleriana!"

    # Classe circuito que sera utilizada, ela tera dois atributos: peso e circuito.
    class circuito: pass

    # Criacao da lista de objetos da classe circuito, e a sua devida inicializacao
    circuitos_eulerianos = []
    contador = 1
    for i in msts:
        c = circuito()
        c.peso = 0
        c.circuito = list(nx.eulerian_circuit(i))
        c.grafo = nx.Graph(c.circuito)
        c.num = contador
        contador += 1
        circuitos_eulerianos.append(c)

    # Soma dos pesos
    for i in circuitos_eulerianos:
        i.peso = sum([G[j[0]][j[1]]['weight'] for j in i.circuito])

        f = open(os.path.abspath('..')+'\\ufscar-2014-graph-theory-task5a\\Datasets\\peso '+data[0][:-4]+str(i.num)+'.txt','w')
        f.write(os.path.abspath('..')+'\\ufscar-2014-graph-theory-task5a\\Datasets\\'+data[0][:-4]+str(i.num)+"\n")
        f.write("Peso: "+str(i.peso))
        f.close()
        """
        # Print das coisas
        plt.figure(1, figsize=(15,15))		# Cria figura para desenhar grafo: 15 eh a dimensao da imagem

        # Coordenadas mantém as coordenadas dos vértices do grafo
        coordinates = nx.spring_layout(i.grafo)
        # Salva a primeira imagem
        nx.draw(i.grafo, coordinates, node_size=350, font_size=10, edge_width=1, alpha=0.5, arrows=False,
                with_labels=True)
        plt.savefig(os.path.abspath('..')+'\\ufscar-2014-graph-theory-task5a\\Datasets\\'+data[0][:-4]+str(i.num)+'.png')
        plt.close()
        #plt.show()
        """