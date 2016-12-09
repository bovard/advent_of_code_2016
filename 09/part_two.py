
with open('input.txt') as f:
    instructions = f.readlines()[0].strip()

def expand_string(string):
    # base case
    if string == '':
        return 0

    # find all the characters as the beginning of the string
    chrs = 0
    while chrs < len(string) and string[chrs] != '(':
        chrs += 1

    # if it's only characters, return the length
    if chrs == len(string):
        return chrs

    # find the instructions
    j = chrs
    while j < len(string) and string[j] != ")":
        j += 1

    # break apart instructions
    command = string[chrs+1:j]
    chars = int(command.split('x')[0])
    repeat = int(command.split('x')[1])
    to_repeat = string[j+1:j+chars+1]
    # recurse on characters to repeat, and tail
    return chrs + repeat * expand_string(to_repeat) + expand_string(string[j+chars+1:])


print expand_string(instructions)

