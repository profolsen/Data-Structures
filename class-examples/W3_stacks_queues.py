class Queue:
    '''
    This class represents a Queue.
    An object of this class supports operations:
    1. O(1) enqueue
    2. O(1) dequeue (amortized)
    3. O(1) size
    4. O(1) first [peek]
    5. O(1) is_empty 
    The size of the queue adapts to the number of elements in the queue.
    '''
    def __init__(self):
        '''
        Creates an initially empty Queue.
        Parameters:
            None
        '''
        self.contents = []
        self.remove_index = 0
    
    def is_empty(self):
        '''
        Returns True if and only if this Queue is empty
        Parameters:
            None
        Returns:
            True if and only if this Queue is empty.
        '''
        return self.remove_index == len(self.contents)
        
    def first(self):
        '''
        Returns the first item (the next one to be dequeued) in this Queue.
        Parameters:
            None
        Returns:
            the first item in this Queue.
        '''
        return self.contents[self.remove_index]
        
    def enqueue(self, item):
        '''
        Enqueues a new item to the end of this Queue.
        Parameters:
            item: the item to enqueue
        Returns:
            None
        '''
        self.contents.append(item)
        
    def dequeue(self):
        '''
        Dequeues and returns the first item in the queue.
        This operation does delayed deletion, i.e., it postpones removing the dequeued item
            from this Queue until the number of items to be removed is more than half the 
            number of items in the queue.
        Delayed deletion allows for an O(n) condense operation which removes all dequeued
            items at once to average out to O(1) work per deleted item, making dequeue an O(1)
            (amortized time) operation.
        Parameters:
            None
        Returns:
            The item that was dequeued.
        '''
        x = self.contents[self.remove_index]
        self.remove_index += 1
        if self.wasted_space() > 0.5:
            self.__condense()
        return x
    
    def size(self):
        '''
        Returns how many items are on this Queue.
        Parameters:
            None
        Returns:
            how many items are on this Queue.
        '''
        return len(self.contents) - self.remove_index
        
    def wasted_space(self):
        '''
        Returns how many dequeued items are still stored in this Queue, i.e., how much
            of this Queue is just "wasted space".
        Parameters:
            None
        Returns:
            how many dequeued items are still stored in this Queue.
        '''
        return self.remove_index / (len(self.contents))
    
    
    def __condense(self):
        '''
        An O(n) operation which removes all items from the queue that were previously dequeued but not 
            completely removed.
        Parameters:
            None
        Returns:
            None
        '''
        t = self.contents
        self.contents = []
        for e in t[self.remove_index:]:
            self.contents.append(e)
        self.remove_index = 0
        
    def __repr__(self):
        '''
        Returns an easy-to-read string representation of this Queue.
        Parameters:
            None
        Returns:
            An easy-to-read string representation of this Queue.
        '''
        return f"Queue:{self.contents[self.remove_index:]}"
        
class Stack:
    '''
    This class represents a Stack.
    An object of this class supports operations:
    1. O(1) push
    2. O(1) pop
    3. O(1) size
    4. O(1) peek
    5. O(1) is_empty 
    The size of the stack adapts to the number of elements in the stack.
    '''
    def __init__(self):
        '''
        Creates an initially empty Stack.
        Parameters:
            None
        '''
        self.contents = []
        
    def is_empty(self):
        '''
        Returns True if an only if this Stack is empty.
        Parameters:
            None
        Returns:
            True if an only if this Stack is empty.
        '''
        return len(self.contents) == 0
    
    def push(self, item):
        '''
        Pushes a new item to the top of the stack.
        Parameters:
            item: the new item to push.
        Returns:
            None
        '''
        self.contents.append(item)
    
    def peek(self):
        '''
        Returns the item on the top of the stack without removing it.
        Parameters:
            None
        Returns:
            The item on the top of the stack.
        '''
        return self.contents[-1]
        
    def pop(self):
        '''
        Returns and removes the item on the top of this Stack.
        Parameters:
            None
        Returns:
            The item on the top of this Stack.
        '''
        x = self.contents.pop(-1) # pop(-1) is O(1) in Python.
        return x
    
    def size(self):
        '''
        Returns the number of items on this Stack.
        Parameters:
            None
        Returns:
            The number of items on this Stack.
        '''
        return len(self.contents)
    
    def __repr__(self):
        '''
        Returns an easy-to-read string representation of this Stack.
        Parameters:
            None
        Returns:
            An easy-to-read string representation of this Stack.
        '''
        return f"Stack:{self.contents}"


def remove_smallest(a_queue):
    '''
    This function removes the smallest item from a FIFO Queue.
    It works by dequeuing each element and keeping and storing it in "smallest"
    If it finds another element smaller than "smallest", it re-enqueues smallest and
        sets smallest to store the newly discovered, smaller element.
    It makes sure it only goes through each item in the queue once by initally enqueueing
        a None on the end of the queue.
    When this None is dequeued, the function stops, and the current value of smallest is returned.
    Parameters:
        a_queue: A FIFO Queue.
    Returns:
        The smallest item stored in a_queue.
    '''
    if a_queue.is_empty():
        return None
    a_queue.enqueue(None)
    element = a_queue.dequeue()
    smallest = element
    first_iteration = True
    while element is not None:
        if element < smallest:
            a_queue.enqueue(smallest)
            smallest = element
        elif first_iteration:
            first_iteration = False
        else:
            a_queue.enqueue(element)
        element = a_queue.dequeue()
    return smallest

def selection_sort(a_queue):
    '''
    Performs a selection sort on a_queue to put all its elements in ASCENDING order.
    While the queue is not empty, items are removed in the queue in ASCENDING 
        order (using remove_smallest) and pushed onto the first stack.
    After all items are dequeued, the first stack stores things in DESCENDING order (from top to bottom).
    Items are popped from the first stack and pushed onto the second stack.
    Items are now on the second stack in ASCENDING order (from top to bottom).
    Items are then popped off the second stack and enqueued back onto the queue in ASCENDING order.
    Parameters:
        a_queue: A FIFO queue.
    Returns:
        The same queue, with its items now in sorted order.
    '''
    s1 = Stack()
    print(f"Starting queue:{a_queue}")
    while not a_queue.is_empty():
        small = remove_smallest(a_queue)
        s1.push(small)
        print(s1, a_queue)
    s2 = Stack()
    while not s1.is_empty():
        s2.push(s1.pop())
    print(s2, s1, a_queue)
    while not s2.is_empty():
        a_queue.enqueue(s2.pop())
    print(a_queue.wasted_space())
    return a_queue
    
def smoke_test():
    q = Queue()
    for i in [2, 5, 1, 4, 3]:
        q.enqueue(i)
    print("After sort:", selection_sort(q), "\n\n")
    q = Queue()
    for i in [1, 5, 2, 4, 3]:
        q.enqueue(i)
    print("After sort:", selection_sort(q))
    
if __name__ == "__main__":
    smoke_test()
    
        