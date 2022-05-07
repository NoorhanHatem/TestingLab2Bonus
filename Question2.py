
def findMax(array):
    maximum = None
    for x in array:
        if maximum is None or x > maximum:
            maximum = x
    return maximum

def findMin(array):
    minimum = None
    for x in array:
        if minimum is None or x < minimum:
            minimum = x
    return minimum