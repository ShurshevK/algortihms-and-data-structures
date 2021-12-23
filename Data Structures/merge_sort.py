def merge_sort(list):
    """
    Sorts a list in a ascending order
    """

    if len(list) <= 1:
        return list
    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(list):
    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]
    return left, right
     
def merge(left, right):
    l = []
    ri = 0
    li = 0

    while li < len(left) and ri < len(right):
        if left[li] < right[ri]:
            l.append(left[li])
            li += 1
        else:
            l.append(right[ri])
            ri+= 1

    l += left[li:]
    l += right[ri:]

    return l


def verify(list):
    n = len(list)

    if n == 0 or n == 1:
        return True
    return list[0] < list[1] and verify(list[1:])

alist = [54, 4, 57, 32, 46, 76, 88, 1, 44, 55]

l = merge_sort(alist)

a = verify(l)
print(a)


