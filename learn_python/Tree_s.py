class node:
    def __init__(self, label, goal_cost):
        self.label = label
        self.cost= 10000
        self.goal_cost= goal_cost
        self.save_cost = None
        self.pr = []
        self.child = []
    def __repr__(self):
        return str(dict(
            {
                'label' : self.label,
                "cost" : self.cost,
                "goal cost" : self.goal_cost
            }
        ))
    def __eq__(self, other):
        if self.save_cost ==10000 :
            return self.goal_cost +self.cost < other.goal_cost + other.cost
        else:
            return self.cost <other.cost
    def get_label(self):
        return self.label
    def neighbors (self) :
        return self.child + self.pr
class Tree:
    def __init__(self):
        self.nodes = []
        self.edges = []
    def add_nodes(self, data):
        for node in data:
            self.nodes.append(node)
    def is_container(self, node):
        for el in self.node:
            if el == node:
                return True
            else:
                return False
    def add_node(self, node):
        self.nodes.append(node)
    def add_edge(self, start,end, weight=10000 ):
        start= node(start)
        end = node(end)
        if not self.is_container(start):
            self.add_node(start)
        if not self.is_container(end):
            self.add_node(end)