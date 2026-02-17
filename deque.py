from collections import deque

printer_queue = deque()

printer_queue.append("Poster")
printer_queue.append("Photocard")
printer_queue.append("A3")

# print(printer_queue)

while len(printer_queue) > 0: 
    document = printer_queue.popleft()
    print(f"Printing: {document}")

n = 6 
binary = deque()
empty_list = []
binary_list = []
result = []

for i in range(1, n+1): 
    empty_list.append(i)

for y in empty_list: 
    binary_list.append(bin(y)[2:])

for x in binary_list: 
    binary.append(x)

while len(binary) > 0: 
    document = int(binary.popleft())
    result.append(document)

print(result)
