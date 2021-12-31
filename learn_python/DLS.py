

def DLS(initialState, goal,limit):

    frontier = [initialState]
    
    explored = []
    depth={
        initialState :0
    }
 
    while frontier:

        #print(frontier)
        state = frontier.pop(len(frontier)-1) #gan state cho trang thai cuoi
        explored.append(state)  #add state và explored
        
        if goal == state :
            return explored
        if depth[state] < limit :
            for neighbor in graph[state]:     #for biến_lap in chuoi_lap:
                
                if neighbor not in (explored and frontier):
                     frontier.append(neighbor)
                     depth[neighbor]=depth[state]+1

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

    result = DLS('A','K',3)
    
    if result:

        s = 'explored: '

        for i in result:

            s += i + ' '

            print(s)

    else:

        print("404 Not Found!")