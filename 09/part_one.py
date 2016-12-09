
with open('input.txt') as f:
    instructions = f.readlines()[0].strip()

result_str = instructions

pas = 0
result = 0
while "(" in result_str:
    pas += 1
    print pas
    i = 0
    result = 0
    instructions = result_str
    result_str = ""
    while i < len(instructions):
        # print instructions[i:min(i+10, len(instructions))]
        if instructions[i] == "(":
            j = i + 1
            while instructions[j] != ")":
                j += 1
            command = instructions[i+1:j]
            chars = int(command.split('x')[0])
            repeat = int(command.split('x')[1])
            to_repeat = instructions[j+1:j+chars+1]
            #print "===== to_repeat ======="
            #print to_repeat
            #print "===== to_repeat ======="
            #print len(to_repeat), chars
            #print ""

            for i in range(repeat):
                result_str += to_repeat

            result += (chars * repeat)

            i = j + chars + 1
        else:
            result += 1
            result_str += instructions[i]
            i += 1


# print result_str
print result

