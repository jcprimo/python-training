# tuples
# you can not add elements
# nor change the value of it. as you declare it is as how it will stay.
data = ("hey", "you")

# is a list the same as an array? (no!)
list_example = []

# list with integers
list_example = [1, 2]

tuple0 = 1, 4, 'three'
print("tuple0=", tuple0)

# empty tuple
empty_tuple = ()
print("empty_tuple =", empty_tuple)

# using the tuple() function
func_tuple = tuple([1, 3, 'three'])
print("func_tuple", func_tuple)

func_str_tuple = tuple('tuple')
print("string 'tuple' using tuple()=", func_str_tuple)

digits_tuple = tuple('123')
print("digits tuple = ", digits_tuple)

# Count the elements in a tuple
print("how big is it? = ", len(digits_tuple))

count_same_numbers = (1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 3, 2)
print("how many 2's? = ", count_same_numbers.count(2))
print("how many 4's? = ", count_same_numbers.count(4))

# Access tuple elements
tuple_unpacking = (1, 'two', [3, 3, 3], {'four': 4})
a, b, c, d = tuple_unpacking
print("int={0}\nstring={1}\ntuple={2}\ndict={3}".format(a, b, c, d))

# remove duplicates and return which ones were not duplicated
list_with_dups = [9, 8, 5, 1, 2, 1, 3, 4, 1, 3, 5, 6, 2, 6, 8, 9, 8, 0, 0, 5, 4]
to_remove = [1, 2, 3]
removed_dups = list(set(list_with_dups))
# after removal
not_repeated = list(set(list_with_dups) - set(to_remove))
print("removed_dups=", removed_dups)
print("\nnot_repeated=", not_repeated)

# find dups in list
# [:i] - tells at what index to stop
find_dups = [x for i, x in enumerate(list_with_dups) if x in list_with_dups[:i]]

# easy join
str1 = "I love "
str2 = "Python"
res = ''.join([str1, str2])
print('after join = ', res)

# Java way to concatenate
strs = ['Life', 'is', 'short,', 'I', 'use', 'Python']


def join_strs(strs):
    result = ''
    for s in strs:
        result += ' ' + s
    return result[1:]


# Pythonic way to join
# Elegant at is best
def join_pythonic_way(strings):
    return ' '.join(strings)


print(join_strs(strs))
print("Now the pythonic way:\n", join_pythonic_way(strs))
