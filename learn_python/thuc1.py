
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
    
def BFS(initialState, goal):

    frontier = [initialState]

    explored = []

    while frontier:

        state = frontier.pop(0)  #gan state cho trang thai dau

        explored.append(state)  #add state và explored

        if goal == state:

            return explored

        for neighbor in graph[state]:     #for biến_lap in chuoi_lap:

            if neighbor not in (explored and frontier):

                frontier.append(neighbor)

    return False
if __name__ == '__main__':

    graph = {


    'A' : ['B','D','C'],

    'B' : [],

    'C' : ['B','D','E','F'],

    'D' : ['B'],

    'E' : [],

    'F' : ['E'],

    

    }

    result = BFS('A','F')
    
    if result:

        s = 'explored: '

        for i in result:

            s += i + ' '

            print(s)

    else:

        print("404 Not Found!")