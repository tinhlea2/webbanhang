
def DFS(initialState, goal):

    frontier = [initialState]
    
    explored = []

    while frontier:

        #print(frontier)
        state = frontier.pop(len(frontier)-1) #gan state cho trang thai cuoi
        explored.append(state)  #add state và explored

        if goal == state:

            return explored

        for neighbor in graph[state]:     #for biến_lap in chuoi_lap:

            if neighbor not in (explored and frontier):
                
                frontier.append(neighbor)

    return False
    

if __name__ == '__main__':

    graph = {

    'A' : ['C','B'],

    'B' : ['E','D'],

    'C' : ['G','F'],

    'D' : ['I','H'],

    'E' : ['K','J'],

    'F' : ['M','L'],

    'G' : ['O','N'],

    'H' : [],

    'I' : [],

    'J' : [],

    'K' : [],

    'L' : [],

    'M' : [],

    'N' : [],

    'O' : []

    }

    result = DFS('A','C')
    
    if result:

        s = 'explored: '

        for i in result:

            s += i + ' '

            print(s)

    else:

        print("404 Not Found!")