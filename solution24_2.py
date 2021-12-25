with open('input24_1.txt') as fp:
    lines = fp.read().split('\n')
data = list(zip(
    [int(x.split()[-1]) for x in lines[4::18]],
    [int(x.split()[-1]) for x in lines[5::18]],
    [int(x.split()[-1]) for x in lines[15::18]]))

def recursive(params, order=lambda x: x, z=0, number=()):
    if not params:
        return number if z == 0 else None
    a, b, c = params[0]
    if a == 26:
        if not (1 <= (z%26)+b <= 9): return None
        return recursive(params[1:], order, z//a, number + ((z%26)+b,))
    for i in order(range(1, 10)):
        result = recursive(params[1:], order, z//a*26+i+c, number+(i,))
        if result is not None: return result

print('Part 1:', recursive(data, order=reversed))
print('Part 2:', recursive(data))