
with open('input.txt') as f:
    instructions = f.readlines()[0].strip()

def expand_string(string):
    if string == '':
        return 0
    chrs = 0
    while chrs < len(string) and string[chrs] != '(':
        chrs += 1

    if chrs == len(string):
        return chrs

    j = chrs
    while j < len(string) and string[j] != ")":
        j += 1

    command = string[chrs+1:j]
    chars = int(command.split('x')[0])
    repeat = int(command.split('x')[1])
    to_repeat = string[j+1:j+chars+1]
    return chrs + repeat * expand_string(to_repeat) + expand_string(string[j+chars+1:])


print expand_string(instructions)

