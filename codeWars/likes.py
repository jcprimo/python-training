def likes(names):
    res = " like this"
    if not names:
        return "no one" + " likes this"
    if len(names) == 1:
        return names[0] + " likes this"
    if len(names) == 2:
        return names[0] + " and " + names[1] + res
    if len(names) == 3:
        return names[0] + ", " + names[1] + " and " + names[2] + res
    if len(names) >= 4:
        return names[0] + ", " + names[1] + " and " + str(len(names) - 2) + " others" + res


# make a dictionary d of all the possible answers. Keys are the respective number
# of people who liked it.
def alternative_likes(names):
    # {} indicate placeholders. They do not need any numbers but are simply replaced/formatted
    # in the order the arguments in names are given to format
    # {others} can be replaced by its name; below the argument "others = length - 2"
    # is passed to str.format()
    d = {
        0: "no one likes this",
        1: "{} likes this",
        2: "{} and {} like this",
        3: "{}, {} and {} like this",
        4: "{}, {} and {others} others like this"
    }
    length = len(names)
    # d[min(4, length)] insures that the appropriate string is called from the dictionary
    # and subsequently returned. Min is necessary as len(names) may be > 4

    # The * in *names ensures that the list names is blown up and that format is called
    # as if each item in names was passed to format individually, i. e.
    # format(names[0], names[1], .... , names[n], others = length - 2
    return d[min(4, length)].format(*names, others=length - 2)


if __name__ == '__main__':
    print(likes(['Max', 'John', 'Mark']))
