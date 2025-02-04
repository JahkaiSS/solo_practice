output = ""

for i in range(101):
    if i % 3 == 0 and i % 5 != 0: #IS DIV BY 3, 
        #but not 5
        output = 'fizz'
        print(output)

    elif i % 5 == 0 and i % 3 != 0: # IS DIV BY 5, 
        # but NOT 3
        output = 'buzz'
        print(output)

    elif i % 15 == 0 and i > 0: # IS DIV BY 15
        # 15 is DIV by 5 and 3
        # 0 % 15 == 0 returns true
        output = 'fizzBuzz'
        print(output)
    
    else: #IS NOT DIV BY 3 OR 5
        print(i)
