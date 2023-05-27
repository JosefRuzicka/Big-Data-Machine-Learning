# Código Tarea 2 AGVD
# Estudiantes:
# Josef Ruzicka. B87095
# Emmanuel Zúñiga. B98729
# Derek Suárez Rojas. B97775
# Julián Solís Aguilar. B97634

import pandas as pd
from itertools import combinations
from itertools import chain


def power_set(items):
    combs = []
    for i in range(1,len(items)+1):
        combs.append(list(combinations(items, i)))
    return list(chain.from_iterable(combs))

def create_tree(items): #Primero crear un árbol para hacer DFS
    tree = {}
    powerset = power_set(items)
    for i in range (0,len(powerset)): 
        powerset[i] = list(powerset[i])
    current_len = 0
    for i in range (0,len(powerset)):
        combs = list(combinations(powerset[i], len(powerset[i])-1))
        for j in range (0,len(combs)):
            combs[j] =  list(combs[j])
        tree[''.join(powerset[i])] = combs
    depth_first_tree = {}
    for key in tree:
        if (tree[key] != [[]]):
            if ''.join(tree[key][0]) not in depth_first_tree:
                depth_first_tree[''.join(tree[key][0])] = [key]
            else:
                depth_first_tree[''.join(tree[key][0])].append(key)
        else:
            if ('null' in depth_first_tree) == False:
                depth_first_tree['null'] = [''.join(key)]
            else:
                depth_first_tree['null'].append(''.join(key))
    for i in range (0, len(powerset)):
        if (''.join(powerset[i]) not in depth_first_tree):
            depth_first_tree[''.join(powerset[i])] = []
    depth_first_tree = dict(sorted(depth_first_tree.items(), key=lambda item: (len(item[0]), item[0])))
    return depth_first_tree

def deepfirstsearch(visited_nodes, tree, node, max_depth, max_itemsets, depth=0): #Búsqueda en profundidad
    if node not in visited_nodes: #Si el nodo no ha sido visitado
        #print(depth)
        if depth == max_depth:
            max_itemsets.append(node) #Agregar el nodo a la lista de max_itemsets si se encuentra en la profundidad indicada
        depth+=1
        visited_nodes.add(node)
        for neighbour in tree[node]: #Para cada vecino del nodo
            deepfirstsearch(visited_nodes, tree, neighbour, max_depth, max_itemsets, depth)

tree = create_tree(['a','b','c','d','e'])
key_element_count = 0
for key in tree:
    key_element_count += len(tree[key])
print(key_element_count)
print(tree)
max_itemsets = []
visited_nodes = set() 
n = 3
deepfirstsearch(visited_nodes, tree, 'null', n, max_itemsets)
print("Max ", n, "-itemsets: ", max_itemsets)
print(len(max_itemsets))