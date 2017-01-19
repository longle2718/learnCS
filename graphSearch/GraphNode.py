# Graph Node class
#
# Long Le
# University of Illinois
#

import numpy as np
import matplotlib.pyplot as plt
import json

class GraphNode:
    def __init__(self,x):
        self.val = x
        # adjacency list (not matrix) representation
        # directed graph
        self.ngbs = set()

def serialize(nodes):
    # input is an array of GraphNodes
    dicts = []
    for node in nodes:
        dicts.append({'val':node.val,'ngbs':list(node.ngbs)})

    return json.dumps(dicts)

def deserialize(data,plot=False):
    # input is an array of dictionaries
    dicts = json.loads(data)
    V = len(dicts)
    
    locMap = {}
    nodeMap = {}

    # creating nodes and filling mappings
    nodes = set()
    for d in dicts:
        node = GraphNode(d['val'])
        idx = d['idx']
        nodeMap[idx] = node
        locMap[node] = (np.cos(idx/V*np.pi*2),np.sin(idx/V*np.pi*2))

        nodes.add(node)

    #print('locMap = '+str(locMap))
    #print('nodeMap = '+str(nodeMap))

    # adding neighbors
    for d in dicts:
        node = nodeMap[d['idx']]
        for idxNgb in d['idxNgbs']:
            node.ngbs.add(nodeMap[idxNgb])

    if plot:
        plt.figure()
        ax = plt.axes()
        ax.add_artist(plt.Circle((0, 0), 1.,color='k',ls='--',fill=False))
        for node in nodes:
            loc = locMap[node]
            plt.annotate(str(node.val),xy=loc,xytext=(loc[0]+.1,loc[1]+.1))
            for ngb in node.ngbs:
                locNgb = locMap[ngb]
                plt.arrow(loc[0],loc[1],locNgb[0]-loc[0],locNgb[1]-loc[1],head_width=0.05,head_length=0.1,fc='k',ec='k')
                #plt.plot([loc[0],locNgb[0]],[loc[1],locNgb[1]])

        plt.axis([-1.2,1.2,-1.2,1.2])
        plt.show()

    return nodes
