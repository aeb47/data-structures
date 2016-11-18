


class Heap(object):

    def __init__(self, iterable=None):
        self.heap = [] if iterable is None else list(iterable)
        for i in range(len(self.heap)/2,-1,-1):
            self._heapify(i)

    def __len__(self):
        return len(self.heap)

    def _get_parent(self, i):
        return i / 2

    def _get_left_child(self,i):
        return 2*i

    def _get_right_child(self,i):
        return (2*i) + 1

    def _exchange(self, a, b):
        temp = self.heap[a]
        self.heap[a] = self.heap[b]
        self.heap[b] = temp

    def _heapify(self,i):
        l = self._get_left_child(i)
        r = self._get_right_child(i)
        if l <= len(self.heap)-1 and self.heap[l][0] > self.heap[i][0]:
            largest = l
        else:
            largest = i

        if r <= len(self.heap)-1 and self.heap[r][0] > self.heap[largest][0]:
            largest = r

        if largest != i:
            self._exchange(i,largest)
            self._heapify(largest)


    def maximum(self):
        return self.heap[0][1]

    def extract_max(self):
        if len(self.heap) < 1:
            raise Exception("Can not Extract Max. No items in Heap")
        heap_max = self.heap[0]
        last = self.heap.pop()
        self.heap[0] = last
        self._heapify(0)

        return heap_max[1]

    def increase_key(self,i,key):
        if key < self.heap[i][0]:
            raise Exception ("New key less that old key")

        self.heap[i][0] = key
        
        while i > 0 and self.heap[self._get_parent(i)][0] < self.heap[i][0]:
            self._exchange(i,self._get_parent(i))
            i = self._get_parent(i)


    def insert(self,key,value):
        self.heap.append([float('-inf'),value])
        self.increase_key(len(self.heap)-1,key) 

if __name__ == "__main__":
    from random import shuffle

    arr = [[1,'monkey'],[4,'car'],[9,'tiger'],[2,'baseball'],[5,'soccer'],[6,'trains'],[10,'andrew']]
    arr = arr*10000000

    heap = Heap(arr)

    heap.insert(7,'ford')
    heap.insert(100,'bentley')

    print heap.extract_max()

