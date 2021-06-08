# Functions for set shattering.
import itertools

def powerset(input_set):
    '''Takes a set as input argument and outputs the powerset of that set.'''
    
    # Initialize 
    powerset_iterator = {}
    
    # Range over combination iterators, and chain them together.
    for r in range(len(input_set)+1):
        powerset_iterator = itertools.chain(itertools.combinations(input_set,r),powerset_iterator)
        
    # Create initial temporary set (evaluating iterator).
    powerset_temp = set(powerset_iterator)
    
    # Convert elements in powerset_temp to actual sets (using frozenset).
    powerset = set()
    for i in powerset_temp:
        powerset.add(frozenset(i))
    
    # Sanity prints.
    print('A powerset of the set {} has been constructed with {} elements.'.format(input_set, len(powerset)))
    if len(powerset) == 2**(len(input_set)):
        print('This is sane: len(powerset) == 2**(len(input_set)), i.e. {} = {}.'.format(len(powerset),2**(len(input_set))))
    else:
        print('Something is insane.')
        
    return powerset


def shatter_check(set_to_shatter, class_of_sets):
    '''
    This function takes two arguments as input.
    The first argument is a set to shatter.
    The second argument is a set of sets (class).
    
    The function checks whether all subsets of 
    the powerset of the set to shatter are in
    the class (i.e. the intersections exist in the 
    class and can construct the powerset).
    '''
    # First calculate the powerset.
    pwrset = powerset(set_to_shatter)
    
    if all(i in class_of_sets for i in pwrset):
        return print("Shattered.  The size of the class {} is greater or equal to the size of the set to be shattered {} and it's powerset's size {}.".format(len(class_of_sets),len(set_to_shatter),len(pwrset)))
    
    else:
        return print('Not Shattered')