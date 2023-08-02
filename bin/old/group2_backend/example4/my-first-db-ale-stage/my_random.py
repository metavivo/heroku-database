#########################################################################
#                      IMPORT

import random

##############################################################################
#                     GLOBAL VARIABLES

#########################################################################
#                      PARAMETERS

#########################################################################
#                      CLASSES

#########################################################################
#                      FUNCTIONS
#*****************************************************************************
#                  get_random

# Generates a random integer between 0 and the input number.

def get_random(n):
    """Generates a random integer between 0 and the input number.

    :param n: Input integer
    :type n: int
    :returns: integer -- the random number.

    :examples:
      >>> get_random(0)
      0
      >>> get_random(1)
      1
      >>> get_random(3)
      0
      >>> get_random(3)
      1
      >>> get_random(3)
      >>> get_random(3)

    """ 
    if n == 0:
        return 0
    else:
        return random.randint(0, n - 1)

#*****************************************************************************
#                     get_random_element

def get_random_elem(l):
    """Get a list as input and selects a random element.

    :param l: Input list
    :type l: list
    :returns: object -- the selected element.

    :examples:
      >>> get_random_elem(['a', 'b', 'c', 'd', 'e'])
      'b'

    """ 
    return random.choice(l)

#*****************************************************************************
#                     randomize_list

# Get a list as input and return the randomized list.

def randomize_list(l):
    """Get a list as input and return the randomized list.

    :param l: input list
    :type l: list
    :returns: list -- the randomized list

    :examples:

    >>> randomize_list([1,2,3])
    [3, 1, 2]

    >>> randomize_list([1,2,3])
    [2, 1, 3]

    >>> randomize_list([1,2,3])
    [3, 2, 1]

    """ 
    i = len(l)
    accum = []
    consume_list = l
    while i > 0:
        random_position = get_random(i)
        random_elem = consume_list[random_position]
        consume_list = consume_list[0:random_position] + \
                       consume_list[random_position+1:i]
        accum = accum + [random_elem]
        i = i - 1
    return accum

#*****************************************************************************
#                     get_random_sublist

def get_random_sublist(l, n):
    """Given a list, select a random sublist with the fixed length.

    :param l: input list
    :type l: list
    :param n: length of the sublist
    :type n: int
    :returns: object -- the randomized sublist

    :examples:
      >>> get_random_sublist(['a', 'b', 'c', 'd', 'e'], 2)
      ['b', 'e']

    """ 
    if n > len(l):
        return randomize_list(l)
    else:
        return randomize_list(l)[0:n]

#########################################################################
#                      INSTRUCTIONS

#------------------------------------------------------------------------

