'''
Given a string of numbers,
numbers=123
find how many unique expressions exists.

e.g. solution example
1+2+3 = 6  //this is an expression and is unique
1+2-3 = 0 // this is unique too
1-2+3 = 0 // non unique
1-2-3 = -6 // si es unique

correct answer:
there are 3 unique solutions
'''


def unique_expression(numbers):
    return 0


# def find_unique_expressions(simple_nums):


numbers = "1234"
signs = "+-"
nums = {1, 2, 3, 4}

simple_nums = {1, 2, 3}
# find_unique_expressions(simple_nums)

#Zips the two lists into pairs
# '1 2 3 4' and '+ -'
# result = '1 + 2 -'
pairs = list(zip(numbers, signs))
print("pairs=\n", pairs)

#.join()
temp=[]
for sub in pairs:
    temp.append(''.join(sub))
print("temp=",temp)



#.join() again
output = ''.join(temp)
print("result=",output)

#another approach
out1 = ''
for i, c in enumerate(nums):
    #Reset the counter to prevent out of bounds
    if i >= len(signs):
        i = 0

    out1 += str(c) + signs[i]
print("another approach results = ", out1)