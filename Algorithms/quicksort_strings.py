
#Linear
line_text = ["Ronna",
"Ronni",
"Noella",
"Noelle",
"Noellyn",
"Noelyn"]

name = ["Ronna", "Ronna"]
	
def index_of_item(collection, target):
    for i in range(0, len(collection)):
        if target == collection[i]:
            return i
    return None


  

for n in name:

  index = index_of_item(line_text, n)
  # Lastly, we print the index we got back.
  print(index)

def binary_search(collection, target):
    first = 0
    last = len(collection)
    while first <= last:
        midpoint = (first + last) // 2
        if collection[midpoint] == target:
            return midpoint 
        elif collection[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint -1 
        return None

for n in name:
    index = binary_search(line_text, n)
    print(index)

        
