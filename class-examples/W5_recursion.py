# This file is not documented because the code is too ecletic and incohesive to benefit from a systematized
# documentation.
# Instead, here is a list of the RECURSIVE things you will find in this document:
# 1. a factorial function (mathematics: n! = n * (n - 1) * (n - 2) * ... * 1).
# 2. the LinkedNode class (see *_LinkedList.py for more details).
# 3. A simplified version of LinkedList (see *_LinkedList.py for more details) with methods for...
#     A. printing the list
#     B. moving the largest element in the list to the end of the list.
# 4. A function for executing a selection sort on a list.
# 5. (advanced) a back-tracking algorithm for finding the smallest number divisible by 113 given 
#     some additional constraints.
def factorial(n):
    if n == 0:
        return 1
    if n > 0:
        return n * factorial(n - 1)
    raise ValueError(f"{n} is a negative parameter to factorial.") 
    
print("\n************* Testing factorial ****************")
parameter = int(input("Enter a number and try to be positive"))
try:
    print(factorial(parameter))
except ValueError:
    print("No factorials for you!")

class LinkedNode:
    # keys should be unique, but this object doesn't check that
    # it is up to the programmer to verify that keys are unique
    # before insertion.
    def __init__(self, value = None, next = None):
        self.__value = value
        self.__next = next

    def get_value(self):
        return self.__value

    def get_next(self):
        return self.__next

    def set_value(self, value = None):
        self.__value = value

    def set_next(self, next = None):
        self.__next = next

    def __repr__(self):
        rest = "nothing" if next is None else "etc"
        return f"LinkedNode[{self.__value},{rest}]"

    pass #end of class

class LinkedList:
    def __init__(self):
        self.__head = None
    
    @classmethod
    def from_list(cls, a_list):
        h = LinkedNode(a_list[-1])
        for i in range(-2, -(len(a_list) + 1), -1):
            h = LinkedNode(a_list[i], h)
        answer = LinkedList()
        answer.__head = h
        return answer
        
    @classmethod
    def print_list_helper(cls, h):
        if h is None:
            print("None")
            return
        print(f"{h}-->", end="")
        LinkedList.print_list_helper(h.get_next())
        
    @classmethod 
    def __move_largest_to_end_helper(cls, h):
        if h is None or h.get_next() is None:
            return h
        if h.get_value() > h.get_next().get_value():
            x = h.get_next()
            h.set_next(h.get_next().get_next())
            x.set_next(LinkedList.__move_largest_to_end_helper(h))
            return x
        h.set_next(LinkedList.__move_largest_to_end_helper(h.get_next()))
        return h
        
    def move_largest_to_end(self):
        self.__head = LinkedList.__move_largest_to_end_helper(self.__head)
        
    def print_list(self):
        LinkedList.print_list_helper(self.__head)

print("\n************* Testing move_largest_to_end ****************")
h = LinkedList.from_list([4, 2, 5, 1, 0])
print("initial list...")
h.print_list()
h.move_largest_to_end()

print("\naltered list:")
h.print_list()

def smallest_index(a_list):
    if len(a_list) == 0:
        return None
    smallest_index = 0
    for i,e in enumerate(a_list):
        if e < a_list[smallest_index]:
            smallest_index = i
    return smallest_index
    
def selection_sort(unsorted_list, sorted_list):
    if len(unsorted_list) == 0:
        return #no more items to move!
    target_index = smallest_index(unsorted_list)
    next_element = unsorted_list[target_index]
    unsorted_list.pop(target_index)
    sorted_list.append(next_element)
    selection_sort(unsorted_list, sorted_list)
    
print("\n************* Testing selection_sort ****************")
an_unsorted_list = [5, 3, 4, 2, 1]
print("unsorted: ", an_unsorted_list)
a_sorted_list = []
selection_sort(an_unsorted_list, a_sorted_list)
print("sorted: ", a_sorted_list)

def smallest_number_divisible_by_113(length, a, b, num_as_string):
    if len(num_as_string) < length:
        first_try = num_as_string + str(a)
        second_try = num_as_string + str(b)
        potential_solution = smallest_number_divisible_by_113(length, a, b, first_try)
        if potential_solution > -1:
            return potential_solution
        potential_solution = smallest_number_divisible_by_113(length, a, b, second_try)
        if potential_solution > -1:
            return potential_solution
        return -1 # -1 is a sentinel meaning there was no solution with num_as_string as the first digits.
    potential_solution = int(num_as_string)
    if potential_solution % 113 == 0: 
        return potential_solution
    return -1 # no solutions with num_as_string as the first digits.
    
print("\n************* Testing smallest_number_divisible_by_113 ****************")
print(smallest_number_divisible_by_113(10, 2, 7, ""))
