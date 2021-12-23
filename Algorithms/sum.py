import time
numbers = [3,4,5,7,7,8]

def sum(numbers):
    
 
    total = 0
    for number in numbers:
        total += number
    return total
    

start = time.time()
print(sum(numbers))
end = time.time()
print("The time of execution of above program is :", end-start)
