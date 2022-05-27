#-----------The Self Taught Computer Scientist Algorithm Exercises-----------

# Print the numbers from 1 to 10 recursively
def num_counter(start, end):
    if start > end:
        return
    print(start)
    return num_counter(start + 1, end)

# num_counter(1, 10)