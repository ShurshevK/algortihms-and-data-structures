def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = (len(list))//2

        if list[midpoint] == target:
            return True
        else:
            if list[midpoint]<target:
                return recursive_binary_search(list[midpoint + 1:], target)
            else:
                return recursive_binary_search(list[: midpoint], target)


def verify(result):
    print("Target found :", result)

list = [i for i in range(1, 10)]

result = recursive_binary_search(list, 10)
verify(result)


result = recursive_binary_search(list, 4)
verify(result)