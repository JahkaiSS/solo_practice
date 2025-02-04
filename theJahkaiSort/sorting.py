import random
l = list([22,1,5,6,100,8])
for i in range(100):
    l.append(random.randint(1,15000))

for i in range(len(l) - 1):
    for i in range(len(l) - 1):
        # current val = temp
        # next val = l[i + 1]
        temp = l[i]
        next = l[i + 1]
        case1 = temp > next
        case2 = temp <= next
        # case 1 -> curr > next
        # SWAP THEM
        # case 2 -> curr < next
        # DO NOTHING
        # HOW TO SWAP
        # l[i], l[i+1] = l[i+1], l[i]
        if case1:
            l[i], l[i+1] = l[i+1], l[i]
        # Check through list n times
        # where n is the length of the list
print(l)

# Time complexity of 
# O(n^2)