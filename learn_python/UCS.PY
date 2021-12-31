from collections import defaultdict
from os import close, get_exec_path
from queue import PriorityQueue
data = defaultdict(list)
data['A'] = ['B' , 2 , 'D' , 1 , 'C' , 3 ]
data['B'] = ['E' , 5 , 'F' , 4 ]
data['C'] = ['G' , 6 , 'H' , 3 ]
data['D'] = ['I' , 2 , 'J' , 4 ]
data['F'] = ['K' , 2 , 'L' , 1 , 'M' , 4 ]
data['H'] = ['N' , 2 , 'O' , 4 ]

class Node:
    def __init__(self, name , par = None , g=0) :
        self.name = name
        self.par = par
        self.g = g
    def display(self):
        print(self.name, self.g)
    def __lt__(self, other) :
        if other == None :
            return False
        return self.g < other.g
    def __eq__(self, other) :
        if other == None :
            return False
        return self.name < other.name
    def equal(O,G):
        if O.name == G.name :
            return True
        return  False
    def checkInpriority (tmp , c):
        if tmp == None :
            return False
        return (tmp in c.queue)
    def getPath (O):
        print(O.name)
        if O.par != None:
           O.getPath(O.par)
        else:
            return    
         
def UCS(S = Node('A') , G = Node('N')) :
    Open = PriorityQueue()
    close = PriorityQueue()
    Open.put(S)
    while True:
        if Open.empty() == True:
            print('404')
            return
        O= Open.get()
        close.put(O)
        print('duyet:   ',O.name, O.g )
        if O.equal(O,G) == True:
            print('THANH CONG')
            O.getPath(O)
            print('distance:   ',O.g)
            return
        i=0
        while i< len(data[O.Name]):
            Name = data[O.name][i]
            G= O.g + data[O.name][i+1]
            tmp= Node[name= Name, g=G]
            ok1=O.checkInpriority ()
    



        

    

