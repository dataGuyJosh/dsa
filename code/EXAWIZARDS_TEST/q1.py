def decode(encoded):
    e = list(map(int, encoded))
    e.reverse()
    result = ''
    # create dictionary of ascii
    ascii_map = {}

    def char_range(c1, c2):
        return (chr(n) for n in range(ord(c1), ord(c2) + 1))
    ascii_idx = 65
    for c in list(char_range('A', 'z')):
        ascii_map[ascii_idx] = c
        ascii_idx += 1
    ascii_map[32] = ' '
    # convert encoded to individual indexes
    e_lst = []
    i = 0
    # for i in range(len(e)):
    while i < len(e):
        num = int(''.join(map(str, e[i:i+2])))

        if num == 32 or num >= 65:
            e_lst.append(num)
            i += 2
        else:
            e_lst.append(int(''.join(map(str, e[i:i+3]))))
            i += 3

    # decode
    for i in e_lst:
        result += ascii_map[i]

    return result


tests = [
    '23511011501782351112179911801562340161171141148', # Truth Always Wins
    '2312179862310199501872379231018117927', # Have a Nice Day
    '1219950180111108236115111016623101401611235115012312161151110101111127' # Honesty is the Best Policy
]

results = []

for encoded in tests:
    results.append(decode(encoded))

print(results)
