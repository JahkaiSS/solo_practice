# convert list of characters into
# numbers
import random

l_of_letters = []
for i in range(500):
    l_of_letters.append(chr(random.randint(65,100)))
store = []

# store has number reps of letters
for i in range(len(l_of_letters) - 1):
    if i >= 0:
        store.append(ord(l_of_letters[i]))
    if i > 1 and i < len(l_of_letters) - 1:
        store.append(ord(l_of_letters[i + 1]))

for i in range(len(store)):
    for i in range(len(store) - 1):
        
    
        # Do a jahkai sort on the numbers
        case1 = store[i] > store[i + 1]
        if case1:
            store[i], store[i + 1] = store[i + 1], store[i]

# convert back into letters     
# # using 'chr()' 
#       
for i in range(len(store)):
    store[i] = chr(store[i])
    
print(store)

