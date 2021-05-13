import math
from copy import deepcopy
from queue import PriorityQueue

class Item:
    def __init__(self, benefit, weight):
        self.benefit = benefit
        self.weight = weight

class Node:
    def __init__(self, binary, items, max_weight, index):
        self.binary = binary
        self.items = items
        self.index = index
        self.max_weight = max_weight

    def __gt__(self, other):
        return self.value() < other.value()

    def __eq__(self, other):
        return self.value() == other.value()

    def value(self):
        weight = 0
        benefit = 0
        for i, bit in enumerate(self.binary):
            if (bit is None or bit == 1) and weight + self.items[i].weight <= self.max_weight:
                weight += self.items[i].weight
                benefit += self.items[i].benefit
        return (benefit, weight)

    def lower_bound(self):
        benefit = 0
        weight = 0
        for i, bit in enumerate(self.binary):
            if bit == 1:
                benefit += self.items[i].benefit
                weight += self.items[i].weight
        return (benefit, weight)

    def upper_bound(self):
        benefit, weight = self.value()

        if weight != self.max_weight:
            last_benefit = (
                (self.items[-1].benefit * (self.max_weight - weight)) / self.items[-1].weight)
            return (math.floor(benefit + last_benefit), self.max_weight)
        else:
            return (benefit, self.max_weight)

class bb():
    def __init__(self, max_weight, items):
        self.max_weight = max_weight
        self.items = items
    
    def sol():
        queue = PriorityQueue()

        root = Node([None] * len(items), items, max_weight, 0)
        highest_lb_benefit, _ = root.lower_bound()
        queue.put(root)

        path = []
        while not queue.empty():
            node = queue.get()
            lb_benefit, _ = node.lower_bound()

            if lb_benefit < highest_lb_benefit:
                break
            else:
                highest_lb_benefit = lb_benefit
                path.append(node)

            if node.index < len(items):
                for i in range(2):
                    binary = deepcopy(node.binary)
                    binary[node.index] = i
                    new_node = Node(binary, items, max_weight, node.index + 1)

                    lb_benefit, lb_weight = new_node.lower_bound()
                    if lb_weight <= max_weight and lb_benefit >= highest_lb_benefit:
                        queue.put(new_node)
        return path, highest_lb_benefit

        

max_weight = 28
items = [ Item(8, 4), Item(12, 8), Item(16, 12), Item(20, 16)]
bb(max_weight, items)

path, highest_lb_benefit = bb.sol()
for i, node in enumerate(path):
    print(f'cota_inferior:{node.lower_bound()[0]} | beneficio:{node.value()[0]} | cota_superior:{node.upper_bound()[0]}')
print(f'c:{highest_lb_benefit}')