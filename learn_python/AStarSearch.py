import heapq


class Node:
    def __init__(self, label, goal_cost):
        self.label = label
        self.cost = 10000
        self.goal_cost = goal_cost
        self.save_cost = None
        self.pr = []
        self.child = []

    def __repr__(self):
        return str(dict({
            "label": self.label,
            "cost": self.cost,
            "goal cost": self.goal_cost
        }))

    def __eq__(self, other):
        return self.label == other.label

    def __lt__(self, other):
        if self.save_cost == 10000:
            return self.goal_cost + self.cost < other.goal_cost + other.cost
        else:
            return self.cost < other.cost

    def get_label(self):
        return self.label

    def neighbors(self):
        return self.child + self.pr


class Tree:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def add_nodes(self, data):
        for node in data:
            self.nodes.append(node)

    def add_node(self, node):
        self.nodes.append(node)

    def add_edge(self, edge):
        self.edges.append(edge)
        for node in self.nodes:
            if edge[0] == node.get_label():
                for other_node in self.nodes:
                    if edge[1] == other_node.get_label():
                        break;
                node.child.append(other_node);

    def add_edges(self, data):
        for edge in data:
            self.add_edge(edge)

    def get_edge(self, prev_node, current_node):
        for edge in self.edges:
            if edge[0] == prev_node.get_label() and edge[1] == current_node.get_label():
                return edge

def update_cost(tree, current_node, prev_node):
    if tree.get_edge(prev_node, current_node) is not None:
        temp = prev_node.cost + tree.get_edge(prev_node, current_node)[2]
        if current_node.cost > temp:
            current_node.cost = temp


def A_star(tree, start, end):
    frontier = []
    heapq.heapify(frontier)
    heapq.heappush(frontier, start)
    explored = []
    while len(frontier) > 0:
        state = heapq.heappop(frontier)
        explored.append(state)
        print(state)
        if state == end:
            return explored
        for child in state.neighbors():
            update_cost(tree, child, state)
            if child.get_label() not in list(set(node.get_label() for node in frontier + explored)):
                heapq.heappush(frontier, child)
    return False


if __name__ == "__main__":
    tree = Tree()
    tree.add_nodes([
        Node("A", 6),
        Node("B", 3),
        Node("C", 4),
        Node("D", 5),
        Node("E", 3),
        Node("F", 1),
        Node("G", 6),
        Node("H", 2),
        Node("I", 5),
        Node("J", 4),
        Node("K", 2),
        Node("L", 0),
        Node("M", 4),
        Node("N", 0),
        Node("O", 4)
    ])
    tree.add_edges([
        ("A", "B", 2),
        ("A", "C", 1),
        ("A", "D", 3),
        ("B", "E", 5),
        ("B", "F", 4),
        ("C", "G", 6),
        ("C", "H", 3),
        ("D", "I", 2),
        ("D", "J", 4),
        ("F", "K", 2),
        ("F", "L", 1),
        ("F", "M", 4),
        ("H", "N", 2),
        ("H", "O", 4)
    ])
    tree.nodes[0].cost = 0
    result = A_star(tree, tree.nodes[0], tree.nodes[14])
    if result:
        s = 'explored: '
        for i in result:
            s += i.label + " "
            print(s)
    else:
        print("404 Not Found!")



