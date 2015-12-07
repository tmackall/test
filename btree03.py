#!/usr/bin/python

import random


class btree(object):
    def __init__(self, val):
        '''
        __init__() - initialize val and set left and right to None
        '''
        self.val = val
        self.left = None
        self.right = None

    def add(self, val):
        # if the new value is less than the current val and not none
        # recurse left
        if val < self.val:
            if self.left is not None:
                self.left.add(val)
            else:
                self.left = btree(val)
        elif val > self.val:
            if self.right is not None:
                self.right.add(val)
            else:
                self.right = btree(val)

    def find(self, val):
        if val < self.val and self.left is not None:
            return self.left.find(val)
        elif val > self.val and self.right is not None:
            return self.right.find(val)
        elif val == self.val:
            return self.val
        return None

    @classmethod
    def tprint(cls, btree):
    # thane tree and print.
        if btree.left is not None:
            cls.tprint(btree.left)
        if btree.right is not None:
            cls.tprint(btree.right)
                # traverse right and recurse until the end
                # print the value once you cannot go left anymore
                # traverse right and recurse until the end

    @classmethod
    def get_height(cls, node):
        # go left until None - increment the left ht
        # if none - return height
        if node is None:
            return 0
        return 1 + max(cls.get_height(node.left),cls.get_height(node.right))

    @classmethod
    def get_height_it(cls, node):
        # init stack with root and set height to 0
        level_queue = []
        level_queue.append(node)
        height = 0
        # outer loop - for each level
        while len(level_queue) > 0:
            # increment height
            height += 1
            # set # of nodes to length of the queue
            nodes = len(level_queue)
            # inner loop - process all nodes on the level
            while nodes > 0:
                # pop off the queue
                tmp_node = level_queue.pop(0)
                # push next level onto the queue
                if tmp_node.left is not None:
                    level_queue.append(tmp_node.left)
                if tmp_node.right is not None:
                    level_queue.append(tmp_node.right)
                # decrement nodes
                nodes -= 1
        return height


size = 10
sample = [60, 24, 47, 40, 85, 63, 25, 52, 78, 84, 5]
tree = btree(size/2)
for i in sample:
    #tree.add(random.randint(1,size))
    #print('%s,' % random.randint(1,size*10)),
    tree.add(i)


btree.tprint(tree)
print btree.get_height(tree)
print btree.get_height_it(tree)
exit(0)

