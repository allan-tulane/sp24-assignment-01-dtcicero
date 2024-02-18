"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    if x <= 1:
        return x
    else:
        ra = foo(x - 1)
        rb = foo(x - 2)
        return ra + rb

def longest_run(myarray, key):
    max_count = 0
    current_count = 0

    for num in myarray:
        if num == key:
            current_count += 1
        else:
            max_count = max(max_count, current_count)
            current_count = 0

    return max(max_count, current_count)


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    

def to_value(v):
    """
    if it is a Result object, return longest_size.
    else return v
    """
    if type(v) == Result:
        return v.longest_size
    else:
        return int(v)
        

def longest_run_recursive_helper(myarray, key, start, end):
    if start == end:
        size = 1 if myarray[start] == key else 0
        return Result(size, size, size, size == 1)

    mid = (start + end) // 2
    left_result = longest_run_recursive_helper(myarray, key, start, mid)
    right_result = longest_run_recursive_helper(myarray, key, mid + 1, end)
    left_size = left_result.left_size
    right_size = right_result.right_size

    if myarray[mid] == key and myarray[mid + 1] == key:
        cross_size = left_result.right_size + right_result.left_size
    else:
        cross_size = 0

    longest_size = max(left_size, right_size, cross_size)
    is_entire_range = (left_result.is_entire_range and right_result.is_entire_range
                       and myarray[mid] == key and myarray[mid + 1] == key)

    return Result(left_size, right_size, longest_size, is_entire_range)

def longest_run_recursive(myarray, key):
    if not myarray:
        return Result(0, 0, 0, False)

    return longest_run_recursive_helper(myarray, key, 0, len(myarray) - 1).longest_size



