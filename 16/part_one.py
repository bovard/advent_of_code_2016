start = "10010000000110000"


def build_checksum(string):
    if len(string) % 2 == 1:
        return string
    result = ''
    for i in range(0, len(string), 2):
        if string[i] == string[i+1]:
            result += "1"
        else:
            result += "0"
    return build_checksum(result)


def build_filler(string, n):
    if len(string) >= n:
        return string[:n]

    reversed = string[::-1]
    new_r = ''
    for i in range(len(reversed)):
        if reversed[i] == '0':
            new_r += '1'
        else:
            new_r += '0'

    return build_filler("{}0{}".format(string, new_r), n)

print "part one"
filler = build_filler(start, 272)
chk = build_checksum(filler)
print chk

print "part two"
filler = build_filler(start, 35651584)
chk = build_checksum(filler)
print chk


