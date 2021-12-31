from queue import PriorityQueue

def DFS(initialState, goal):

    frontier = [initialState]
    
    explored = []

    while frontier:

        #print(frontier)
        state = frontier.pop(0) #gan state cho trang thai cuoi
        explored.append(state)  #add state và explored

        if goal == state:

            return explored
        
    
        for i in data[state]:     #for biến_lap in chuoi_lap:
             if i not in explored : 
                tam = PriorityQueue()
                frontier.append(tam)

    

if __name__ == '__main__':

    data = {
        'A' : { 'A' : 6, 'B' : 3 , 'C' : 4 , 'D' : 5 },
        'B' : { 'E' : 3 , 'F' : 1 },
        'C' : { 'G' : 6 , 'H' : 2 },
        'D' : { 'I' : 5 , 'J' : 4 },
        'E' : { 'E' : 3},
        'F' : { 'K' : 2 , 'L' : 0 , 'M' : 4 },
        'G' : { 'G' : 6},
        'H' : { 'N' : 0 , 'O' : 4 },
        'I' : { 'I' : 5},
        'K' : { 'K' : 2},
        'L' : { 'L' : 0},
        'M' : { 'M' : 4},
        'N' : { 'N' : 0},
        'J' : { 'J' : 4}
    }

    result = DFS('A','O')
    
    if result:

        s = 'explored: '

        for i in result:

            s += i + ' '

            print(s)

    else:

        print("404 Not Found!")