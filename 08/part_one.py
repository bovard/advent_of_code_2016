
with open('input.txt') as f:
    instructions = f.readlines()

HEIGHT = 6
WIDTH = 50

display = []
for i in range(HEIGHT):
    row = []
    for j in range(WIDTH):
        row.append(0)
    display.append(row)


def rect(display, x, y):
    for i in range(x):
        for j in range(y):
            display[j][i] = 1

def rotate_row(display, y, d):
    display[y] = display[y][-d:] + display[y][:(WIDTH - d)]

def rotate_column(display, x, d):
    column = []
    for i in range(HEIGHT):
        column.append(display[i][x])

    column = column[-d:] + column[:(HEIGHT - d)]

    for i in range(HEIGHT):
        display[i][x] = column[i]

def print_display(display):
    for i in range(HEIGHT):
        row = display[i]
        string = ""
        for i in range(len(row)):
            if row[i] == 1:
                string += "#"
            else:
                string += " "
        print string



for line in instructions:
    if line.startswith('rect'):
        inst = line.split(' ')[1]
        x = int(inst.split('x')[0])
        y = int(inst.split('x')[1])
        rect(display, x, y)
    elif line.startswith('rotate row'):
        y = int(line.split('=')[1].split(' ')[0])
        d = int(line.split(' ')[-1])
        rotate_row(display, y, d)
    elif line.startswith('rotate column'):
        x = int(line.split('=')[1].split(' ')[0])
        d = int(line.split(' ')[-1])
        rotate_column(display, x, d)


count = 0
for i in range(HEIGHT):
    count += sum(display[i])

print count

print_display(display)


