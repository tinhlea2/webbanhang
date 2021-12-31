from queue import PriorityQueue
def A_starv1(initialState,cost_f,goal,data):
    explored=set()
    Frontier=PriorityQueue()
    Frontier.put((cost_f,initialState))
    while Frontier:
        cost, node = Frontier.get()
    
        print(node , cost)
        if node not in explored:
           explored.add(node)
        if node == goal:
            return True
        for i in data[node]:
            if i not in explored :  
                s_cost= cost - data[node][node] + data[node][i] + data[i][i]
                Frontier.put((s_cost,i))
                
if __name__=="__main__":
     data = {
        'A' : { 'A' : 6, 'B' : 2 , 'C' : 1 , 'D' : 3 },
        'B' : { 'B':3 , 'E' : 5 , 'F' : 4 },
        'C' : { 'C':4 , 'G' : 6 , 'H' : 3 },
        'D' : {'D': 5, 'I' : 2 , 'J' : 4 },
        'E' : {'E': 3},
        'F' : {'F': 1, 'K' : 2 , 'L' : 1 , 'M' : 4 },
        'G' : {'G':6},
        'H' : {'H':2 , 'N' : 2 , 'O' : 4 },
        'I' : { 'I' : 5},
        'J' : { 'J' : 4},
        'K' : { 'K' : 2},
        'L' : { 'L' : 0},
        'M' : { 'M' : 4},
        'N' : { 'N' : 0},
        'O' : {'O': 4 }
    }

     result =A_starv1('A',6,'M',data)
   
    

   
   




