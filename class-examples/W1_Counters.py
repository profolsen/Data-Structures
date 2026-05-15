# Created by Paul Olsen
class NamedCounter:
    '''
    An object of this class is a wrapper for a counter.
    The counter can only be incremented by 1.
    For use in demonstrating how Objects work in Python.
    '''
    
    def __init__(self, name, initial_value):
        '''
        This constructor takes a name and an initial value for the counter.
        Parameters:
            name (string): the name of the counter.
            initial_value (int): the initial value the counter has.
        '''
        self.name = name
        self.value = initial_value
    
    def increment(self):
        '''
        Increments the counter.
        Parameters:
            None
        Returns:
            None
        '''
        self.value += 1
    
    def get_value():
        '''
        Returns the current value of the counter.
        Parameters:
            None
        Returns:
            (int) the current value of the counter.
        '''
        return self.value
        
    def __repr__(self):
        '''
        Returns a string representation of this counter:
            <name>:<value>
        Parameters:
            None
        Returns:
            (string) a string representation of this counter.
        '''
        return f"{self.name}:{self.value}"
        
class SetOfCounters:
    '''
    An object of this class is a list of Counters.
    Counters can be placed in the list by position,
    Counters are removed by name.
    The counter space is set during initialization, but can grow to accomodate new counters.
    Mathematically, SetOfCounters is not a set, but a collection.
    '''
    
    def __init__(self, counter_space):
        '''
        A Constructor for a set of counters. 
        Parameters:
            (int) counter_space: how many counters fit in this set of counters.
        '''
        self.counter_space = counter_space
        self.counters = []
        
    def incrementAll(self):
        '''
        Increments each of the counters in the set.
        If a counter was added n times, it will be incremented n times.
        Parameters:
            None
        Returns:
            None
        '''
        for c in self.counters:
            if c is not None:
                c.increment()
    
    def place(self, new_counter, position):
        '''
        Places a new counter in the set of counters.
        The place does not fail, if position is 
        after the end of the list, the list grows to accomodate the new index.
        Parameters:
            (Counter) new_counter: the counter to add to this SetOfCounters.
            (int) position where in the list of counters new_counter should be placed.
        Returns:
            None
            
        '''
        if position >= self.counter_space:
            return
        while len(self.counters) < position+1:
            self.counters.append(None)
        self.counters[position] = new_counter
        
    def remove(self, counter_name):
        '''
        Removes a counter from the list.
        It will remove the last counter of the given name.
        Parameters:
            (string) counter_name: the name of the counter to remove.
        Returns:
            None
        '''
        toRemove = -1
        for i,c in enumerate(self.counters):
            if c is not None and c.get_name() == counter_name:
                toRemove == i
        if toRemove > -1:
            self.counters[toRemove] = None
    
    def __repr__(self):
        '''
        Returns an easy-to-read summary of this SetOfCounters object.
        Parameters:
            None
        Returns:
            an easy-to-read summary of this SetOfCounters object.
        '''
        return f"(<={self.counter_space} counters): {self.counters}"
    
def smoke_test():
    soc = SetOfCounters(13)
    soc.place(NamedCounter("a", -4), 3)
    soc.place(NamedCounter("b", 8), 5)
    nc = NamedCounter("c", 0)
    soc.place(nc, 1)
    soc.place(nc, 2)
    soc.place(nc, 4)
    soc.incrementAll()
    print(soc)
        
if __name__ == "__main__":
    smoke_test()
        