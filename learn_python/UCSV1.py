from queue import PriorityQueue
def UCS(initialState,goal,data):
    explored=set()
    Frontier=PriorityQueue()
    Frontier.put((0,initialState))
    while Frontier:
        cost, node = Frontier.get()
        print(node , cost)
        if node not in explored:
           explored.add(node)
        if node == goal:
            return True
        for i in data[node]:
            if i not in explored :  
                s_cost= cost + data[node][i]
                Frontier.put((s_cost,i))
if __name__=="__main__":
    data = {
        'A' : {'B' : 2 , 'C' : 1 , 'D' : 3 },
        'B' : { 'E' : 5 , 'F' : 4 },
        'C' : { 'G' : 6 , 'H' : 3 },
        'D' : { 'I' : 2 , 'J' : 4 },
        'E' : {},
        'F' : { 'K' : 2 , 'L' : 1 , 'M' : 4 },
        'G' : {},
        'H' : { 'N' : 2 , 'O' : 4 },
        'I' : {},
        'K' : {},
        'L' : {},
        'M' : {},
        'N' : {},
        'J' : {}
    }
    UCS('A','C',data)




