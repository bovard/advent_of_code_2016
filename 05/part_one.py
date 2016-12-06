import hashlib
string = 'uqwqemis'

codes = [0,0,0,0,0,0,0,0]
used = []
i = 0
found = 0
while found < 8:
    m = hashlib.md5()
    to_hash = "{}{}".format(string, i)
    m.update(to_hash)
    anser = m.hexdigest()
    if anser[:5] == '00000':
        print anser
        print found
        pos = anser[5]
        ans = anser[6]
        print pos, ans
        if not pos.isalpha() and int(pos) < 8 and int(pos) not in used:
            found += 1
            used.append(int(pos))
            codes[int(pos)] = ans
    i += 1

print len(codes)
print codes
