from queue import PriorityQueue
def UCS(initialState,cost_f,goal,data):
    explored=set()
    Frontier=PriorityQueue()
    Frontier.put((cost_f,initialState))
    while Frontier:
        cost, node = Frontier.get()
        print(node, cost)
        if node not in explored:
           explored.add(node)
        if node == goal:
            return True
        for i in data[node]:
            if i not in explored :  
                cost=  data[node][i]
                Frontier.put((cost,i))
    return False
                
if __name__=="__main__":
    data = {
        'A' : { 'A' : 6, 'B' : 3 , 'C' : 4 , 'D' : 5 },
        'B' : { 'B' : 3 , 'E' : 3 , 'F' : 1 },
        'C' : { 'C' : 4 , 'G' : 6 , 'H' : 2 },
        'D' : { 'D' : 5, 'I' : 5 , 'J' : 4 },
        'E' : { 'E' : 3},
        'F' : { 'F' : 1, 'K' : 2 , 'L' : 0 , 'M' : 4 },
        'G' : { 'G' : 6},
        'H' : { 'H' : 2 , 'N' : 0 , 'O' : 4 },
        'I' : { 'I' : 5},
        'J' : { 'J' : 4},
        'K' : { 'K' : 2},
        'L' : { 'L' : 0},
        'M' : { 'M' : 4},
        'N' : { 'N' : 0},
        'O' : {'O': 4 }
    }

    result =UCS('A',6,'O',data)
   

   
   




