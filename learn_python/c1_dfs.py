
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

    'S' : ['A','B','C'],

    'A' : ['B','D'],

    'B' : ['C','D','G','F'],

    'C' : ['F'],

    'D' : ['E'],

    'E' : ['F','G'],

    'F' : ['H'],

    'G' : [],

    'H' : ['G'],

    }

    result = DFS('S','G')
    
    if result:

        s = 'explored: '

        for i in result:

            s += i + ' '

            print(s)

    else:

        print("khong tim thay duong di")