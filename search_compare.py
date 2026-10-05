import time
import random


def get_me_random_list(n):
    """Generate list of n elements in random order
    
    :params: n: Number of elements in the list
    :returns: A list with n elements in random order
    """
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list


def sequential_search(a_list, item):
    start = time.time()

    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1
    time_spent = time.time() - start
    return found, time_spent


def ordered_sequential_search(a_list, item):
    start = time.time()
    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos + 1
    time_spent = time.time() - start
    return found, time_spent


def binary_search_iterative(a_list,item):
    start = time.time()
    first = 0

    last = len(a_list) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    time_spent = time.time() - start
    return found, time_spent
    
    
def binary_search_recursive(a_list, item, start=None):
    if start is None:
        start = time.time()

    if len(a_list) == 0:
        time_spent = time.time() - start
        return False, time_spent
    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            time_spent = time.time() - start
            return True, time_spent
        else:
            if item < a_list[midpoint]:
                return binary_search_recursive(a_list[:midpoint], item, start)
            else:
                return binary_search_recursive(a_list[midpoint + 1:], item, start)

if __name__ == "__main__":
    """Main entry point"""
    for the_size in [500, 1000, 5000]:
        sequential_total = 0
        ordered_total = 0
        iterative_total = 0

        recursive_total = 0

        for i in range(100):
            mylist = get_me_random_list(the_size)

            check, time_spent = sequential_search(mylist, 99999999)
            sequential_total += time_spent

            mylist = sorted(mylist)

            check, time_spent = ordered_sequential_search(mylist, 99999999)
            ordered_total += time_spent

            check, time_spent = binary_search_iterative(mylist, 99999999)
            iterative_total += time_spent

            check, time_spent = binary_search_recursive(mylist, 99999999)
            recursive_total += time_spent


        avg_time = sequential_total / 100
        print(f"Sequential Search took {avg_time:10.7f} seconds to run, on average for a list of {the_size} elements")
        avg_time = ordered_total / 100
        print(f"Ordered Sequential Search took {avg_time:10.7f} seconds to run, on average for a list of {the_size} elements")

        avg_time = iterative_total / 100
        print(f"Binary Search Iterative took {avg_time:10.7f} seconds to run, on average for a list of {the_size} elements")

        avg_time = recursive_total / 100
        print(f"Binary Search Recursive took {avg_time:10.7f} seconds to run, on average for a list of {the_size} elements")