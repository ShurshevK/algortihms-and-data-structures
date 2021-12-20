def linear_search(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i 

    return None

def verify (index):
    if index is not None:
        print("target found at index: ", index)
    else:
        print("taget is not in the list")

numbers =list( [i for i in range(0, 10)])

result = linear_search(numbers, 4)
verify = verify(result)

