from Tree_s import node
from Tree_s import Tree
import heapq
def update_cost(tree, current , prev):
    if tree.get_edge(prev, current) is not None:
        if current.cost > prev.cost + tree.get_edge(prev, current)[2]:
            current.cost = prev.cost + tree.get_edge(prev, current)[2]

def A_Star(tree , start, end ):
    frontier =[start]
    heapq.heapify(frontier)
    explored = []
    while len(frontier)>0:
        state= heapq.heappop(frontier)
        explored.append(state)
        print(state)
        if state == end :
            return explored           
        for child in state.neighbors():
            update_cost(tree, child, state)
            if child.get_label() not in list(set(node.get_label() for node in frontier +explored)):
                heapq.heappush(frontier, child)
    return False
                
if __name__=="__main__":
     tree = Tree()
     tree.add_nodes(
         [
            node("A", 6),
            node("B", 3),
            node("C", 4),
            node("D", 5),
            node("E", 3),
            node("F", 1),
            node("G", 6),
            node("H", 2),
            node("I", 5),
            node("J", 4),
            node("K", 2),
            node("L", 0),
            node("M", 4),
            node("N", 0),
            node("O", 4),
            
         ]
     )
     tree.add_edge(
         [
            ("A","A", "B", 2),
            ("A","A", "C", 2),
            ("A","A", "D", 2),
            ("B","B", "E", 2),
            ("B","B", "F", 2),
            ("C","C", "G", 2),
            ("C","C", "H", 2),
            ("D","D", "I", 2),
            ("D","D", "J", 2),
            ("F","F", "K", 2),
            ("F","F", "L", 2),
            ("F","F", "M", 2),
            ("H","H", "N", 2),
            ("H","H", "O", 2)
         
         ]
     )
     tree.nodes[0].cost= 0
     print(tree.nodes[2].cost)
     print(tree.nodes[2])
     result= A_Star(tree,tree.nodes[0], tree.nodes[1])
     if result:
         s= 'explored:   '
         for i in result:
             s+= i.label + " "
             print(s)
     else:
         print("404")
     


     


