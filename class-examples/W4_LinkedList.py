import random

class LinkedNode:
    '''
    An object of this class is a LinkedNode containing
        a data item (called __value here) and a reference to a 
        next node in the list (called __next here).
    '''
    
    def __init__(self, value = None, next = None):
        '''
        Initializes a LinkedNode to store value (None by default) and 
            have a reference to the next node (None by default).
        Parameters:
            value: (default: None): the data item this node is responsible for storing.
            next: (default: None): the node that comes next after this node in the list.
        '''
        self.__value = value
        self.__next = next

    def get_value(self):
        '''
        Returns the data item associated with this node.
        Parameters:
            None
        Returns:
            The data item associated with this node.
        '''
        return self.__value

    def get_next(self):
        '''
        Returns the next node after this one in the list.
        Parameters:
            None
        Returns:
            The next node after this one in the list.
        '''
        return self.__next

    def set_value(self, value = None):
        '''
        Changes the data item associated with this list.
        Parameters:
            value (default: None): a new value to associate with this LinkedNode.
        Returns:
            None
        '''
        self.__value = value

    def set_next(self, next = None):
        '''
        Changes the node that comes after this one in the list.
        Parameters:
            value (default: None): a new node to come after this one in the list.
        Returns:
            None
        '''
        self.__next = next

    def __repr__(self):
        '''
        Returns a string representation of the linked list starting at this node.
        Parameters:
            None
        Returns:
           a string representation of the linked list starting at this node.
        '''
        rest = "nothing" if next is None else "etc"
        return f"LinkedNode[{self.__value},{rest}]"

    pass #end of class

class FreqKey:
    '''
    This class represents a two-part key.
    One part, __id is the key for searching based on identity.
    The other part, __frequency, is how many times this key has been "touched"
        while it has been in the data structure.
    '''
    
    def __init__(self, id):
        '''
        Creates a new FreqKey with the given id and a frequency of 0.
        Parameters:
            id: the id of the new key.
        '''
        self.__id = id
        self.__frequency = 0

    def touch(self):
        '''
        Increments the frequency of this FreqKey.
        Parameters:
            None
        Returns:
            None
        '''
        self.__frequency += 1

    def get_frequency(self):
        '''
        Returns the number of times this key has been "touched" (i.e., searched for) in a data structure.
        Parameters:
            None
        Returns:
            The number of times this key has been referenced in a data structure.
        '''
        return self.__frequency

    def get_key(self):
        '''
        Returns the id of this FreqKey.
        Parameters:
            None
        Returns:
            The id of this FreqKeq
        '''
        return self.__id

    def __repr__(self):
        '''
        Returns a string representation of this FreqKey.
        Parameters:
            None
        Returns:
            A string representation of this FreqKey.
        '''
        return f"{self.__id}:{self.__frequency}"

    def __eq__(self, other):
        '''
        Returns True if and only if other is a FreqKey and has the same (per ==) id.
        Parameters:
            other (FreqKey): another FreqKey
        Returns:
            True if and only if this and other have the same id.
        '''
        if not isinstance(other, FreqKey):
            return False
        return self.__id == other.__id

    pass #end of class

class LinkedList:
    '''
    A linked list that stores key-value pairs.
    Key-value pairs are sorted in terms of popularity in the data structure.
    Insert is O(1), but other operations (remove and contains) are O(n) in the worst case.
    However, in practice, especially if the work-load (consisting of many contains queries) 
        is heavily skewed towards a small minority of the data set the list stores, 
        contains can be very fast (potentially O(1) depending on how skewed the workload is).
    The keys must be FreqKey objects, because the frequency with which they are 
        checked for containment matters to the order in which the list stores them.
    In order for the frequency ordering to be effective, keys should be unique,
        but for efficiency reasons, this condition is not checked.
    It is up to the user to ensure key-uniqueness.
    '''

    def __init__(self):
        '''
        Creates a new empty list.
        __head refers to the first node in the list,
        __tail refers to the last node in the list,
        and __length is the number of key-value pairs stored in the list.
        '''
        self.__head = None
        self.__tail = None
        self.__length = 0

    def __repr__(self):
        '''
        Returns a string representation of this LinkedList.
        Parameters:
            None
        Returns a string representation of this LinkedList.
        '''
        c = self.__head
        answer = ""
        while c is not None:
            answer += str(c) + ","
            c = c.get_next()
        return answer[0:-1]

    def __len__(self):
        '''
        Returns the number of key-value pairs stored in the list.
        Parameters:
            None
        Returns:
            The number of key-value pairs stored in the list.
        '''
        return self.__length

    def _str_tail(self):
        # for debugging, returns the last node in the list as a string.
        return str(self.__tail)

    def _str_head(self):
        # for debugging, returns the first node in the list as a string.
        return str(self.__head)

    def __iter__(self):
        '''
        Allows the list to be looped over:
        for _ in <LinkedList reference>:
           etc.
        Puts all the data of this list into a regular Python list, in order.
        Then returns the iter() of that computed list.
        Parameters:
            None
        Returns:
            an iterator over a Python list containing exactly what was in this
                list when this method was called.
        '''
        answer = []
        c = self.__head
        while c is not None:
            answer.append(c.get_value())
            c = c.get_next()
        return iter(answer)

    @classmethod
    def from_list(cls, a_list):
        '''
        Creates a LinkedList from a regular Python list by inserting each value
            of the Python list into a new LinkedList.
        Parameters:
            a_list: a Python list.
        Returns:
            a LinkedList containing exactly the key-value pairs that were in the Python
                 list.
        '''
        answer = LinkedList()
        for element in a_list:
            answer.insert(element)
        return answer

    @classmethod
    def __reinsert_based_on_frequency(cls, a_list, entry):
        '''
        Reinserts an entry (key-value pair) into the list, in ascending order of
            frequency of that entry's FreqKey. (entry[0]).
        Parameters:
            a_list: a LinkedList.
            entry: a key-value pair that needs to be re-inserted into the list because 
                its frequency has changed because it was looked up.
        Returns:
            None.
        '''
        if a_list.__head is None:
            a_list.__head = LinkedNode(entry)
            a_list.__tail = a_list.__head
            return
        #only ever called if there is at least one thing in the list.
        if entry[0].get_frequency() >= a_list.__head.get_value()[0].get_frequency():
            h = LinkedNode(entry, a_list.__head)
            if a_list.__head == a_list.__tail:
                a_list.__tail = a_list.__head
            a_list.__head = h
            return
        p = None
        n = a_list.__head
        while n is not None and\
                entry[0].get_frequency() < n.get_value()[0].get_frequency():
            p = n
            n = n.get_next()
        if n is None:
            p.set_next(LinkedNode(entry))
            a_list.__tail = p.get_next()
        else:
            p.set_next(LinkedNode(entry, n))
        pass #end of function

    def __contains__(self, key):
        '''
        Returns True if and only if the given key (just a single value) is in the list.
        Parameters:
            key: a singleton (i.e., not a FreqKey) id to search the list for.
        Returns: True if key is a key of a key-value pair in the list, False otherwise.
        '''
        c = self.__head
        if c == None:
            return False
        if c == self.__tail:
            if c.get_value()[0].get_key() == key:
                c.get_value()[0].touch()
                return True
        if self.__head.get_value()[0].get_key() == key:
            self.__head.get_value()[0].touch()
            return True
        # at least two nodes in the list...
        p = None
        while c is not None:
            if c.get_value()[0].get_key() == key:
                entry = c.get_value()
                entry[0].touch()
                if entry[0].get_frequency() < p.get_value()[0].get_frequency():
                    return True  # already in the right place!
                if c.get_next() is None:
                    self.__tail = p
                p.set_next(c.get_next())
                LinkedList.__reinsert_based_on_frequency(self, entry)
                return True
            p = c
            c = c.get_next()
        pass # end of function.

    def insert(self, entry):
        '''
        Inserts a new entry (i.e., a key-value pair) at the end of the list.
        Parameters:
            entry ((FreqKey, ANYTHING) pair): inserts the given key-value pair into
                the list at the end.
        Returns:
            None
        '''
        self.__length += 1
        entry[0].touch()
        c = self.__head
        if c == None:
            self.__head = LinkedNode(entry)
            self.__tail = self.__head
            return
        self.__tail.set_next(LinkedNode(entry))
        self.__tail = self.__tail.get_next()

    def remove(self, key):
        '''
        Removes a key from the list.
        The key given is just a bare key (not a FreqKey).
        Parameters:
            key: a singleton (i.e., not a FreqKey) id to search for and remove from the list.
        Returns:
            None
        '''
        if self.__head == None:
            return #nothing to remove
        if self.__head == self.__tail:
            if self.__head.get_value()[0].get_key() == key:
                self.__length -= 1
                self.__head = None
                self.__tail = None
            return #singleton list, containing target, set to empty.
        if self.__head.get_value()[0].get_key() == key:
            self.__head = self.__head.get_next()
            self.__length -= 1
            return
        #else: #not an empty or singleton list...
        c = self.__head
        while c.get_next() is not None:
            if c.get_next().get_value()[0].get_key() == key:
                if c.get_next() == self.__tail:
                    self.__tail = c
                c.set_next(c.get_next().get_next())
                self.__length -= 1
                return
            c = c.get_next()

    pass #end of class

def smoke_test():
    random.seed(5799121)
    n = LinkedNode()
    print(n)
    a_list = LinkedList()
    print("empty:" , a_list)
    a_list.insert((FreqKey(6), "cat"))
    print("after insert 6:", a_list)
    a_list.insert((FreqKey(3), "dog"))
    print("after insert 3:", a_list)
    a_list.insert((FreqKey(5), "fish"))
    print("after insert 5:", a_list)
    for i in range(5):
        x = random.randint(0, 50)
        a_list.insert((FreqKey(x), f"dog{x}"))
        print(f"after insert {x}", a_list)
    a_list.remove(23)
    print("after remove 23:", a_list)
    a_list.remove(6)
    print("after remove 6:", a_list)
    a_list.remove(37)
    print("after remove 37:", a_list)
    print("tail:", a_list._str_tail())
    print("head:", a_list._str_head())
    print("length:", len(a_list))
    print(31 in a_list)
    print("after in:", a_list)
    print("tail:", a_list._str_tail())
    print("head:", a_list._str_head())
    print("length:", len(a_list))
    print(31 in a_list)
    print("after in:", a_list)
    print("tail:", a_list._str_tail())
    print("head:", a_list._str_head())
    print("length:", len(a_list))
    print(5 in a_list)
    print("after in:", a_list)
    print("tail:", a_list._str_tail())
    print("head:", a_list._str_head())
    print("length:", len(a_list))
    print(list(a_list))
    actual_list = []
    expected_list = LinkedList()
    for i in range(100):
        x = random.randrange(0, 100)
        y = random.randrange(3)
        if y == 0: #insert
            entry = (FreqKey(x), f"x{x}")
            print("INSERT", entry[0].get_key())
            expected_list.insert(entry)
            if entry not in actual_list:
                actual_list.append(entry[0].get_key())
            print(list(expected_list), actual_list)
        if y == 1 and len(actual_list) > 0:
            key = actual_list[random.randrange(0, len(actual_list))]
            print("REMOVE", key)
            expected_list.remove(key)
            actual_list.remove(key)
            print(list(expected_list), actual_list)
        if y == 2 and len(actual_list) > 0:
            key = actual_list[random.randrange(0, len(actual_list))]
            print("CONTAINS", key)
            eb = key in expected_list
            ab = key in actual_list
            print(eb, ab)




if __name__ == "__main__":
    smoke_test()