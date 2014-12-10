#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Thales Menato'
__author__ = 'Daniel Nobusada'

import numpy as np
import networkx as nx
import random
from heapq import heappush, heappop

def prim(G, seed=None):
    """
    Como referencia, foi utilizada as seguintes fontes:
        http://pt.wikipedia.org/wiki/Algoritmo_de_Prim
    Como referencia ao uso do heappop e do heappush, foi utilizado o seguinte algoritmo:
        https://github.com/caioviel/CastFlow/blob/master/CastFlow/noxapp_exp/MSTParser.py

    :param G: graph
        Grafo em qua a funcao sera executada

    :param seed:
        Se seed = None, nao ha semente aonde o grafo começa, e eh escolhido um no aleatório
        Se seed é um inteiro, e o vertice a ser inicializado o algoritmo de Prim

    :return:
        H: graph
        Arvore resultante do Algoritmo de Prim
    """

    # Inicializacao da arvore resposta e insercao do node inicial
    mst = nx.Graph()
    primeiro_no = None
    visitados = []
    arestas_candidatas = []

    # Verificacao de seed, se nao ha seed, entao aleatoriza-se um
    if seed is not None:
        primeiro_no = G[seed]
    else:
        primeiro_no = random.choice(G.nodes())

    # Lista de vertices para utilizacao no Prim
    edgelist = G.edges(data = True)

    # Primeira iteracao do Prim com o primeiro no (seed), usando um heap
    vizinhos = nx.neighbors(G,primeiro_no)

    # Uso do heap
    visitados.append(primeiro_no)
    for vizinho in G[primeiro_no]:
        heappush(arestas_candidatas, (G[primeiro_no][vizinho]['weight'],primeiro_no,vizinho))

    # Loop da escolha da menor aresta
    while len(arestas_candidatas) > 0:
        peso, origem, destino = heappop(arestas_candidatas)
        while destino in visitados and len(arestas_candidatas) > 0:
            peso, origem, destino = heappop(arestas_candidatas)

        if len(arestas_candidatas) > 0:
            visitados.append(destino)
            if not origem in visitados:
                visitados.append(origem)
            vizinhos = [i for i in nx.neighbors(G,destino)]

            for vizinho in vizinhos:
                nova_aresta = (G[destino][vizinho]['weight'], destino, vizinho)
                if nova_aresta not in arestas_candidatas and vizinho not in visitados:
                    heappush(arestas_candidatas, (nova_aresta))

            mst.add_edge(origem, destino, weight=peso)

    return mst
