# compare numbers and return the larger
# keep functions single-responsibility: each function do one job only (SRP)
# reuse simple helper to avoid repeating logic (DRY)
# avoid adding extra features now, YAGNI - keep this tiny and focused

def max_of_two(x, y):
    # return the larger of two values
    # inputs: x, y (numbers)
    # output: the larger value (same type as inputs)
    if x > y:
        return x
    return y

def max_of_three(x, y, z):
    #return the largest of three values by reusing max_of_two (DRY)

    return max_of_two(max_of_two(y, z),x)

print(max_of_three(3, 6, -5))