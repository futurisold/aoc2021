with open('assert.txt') as f:
    raw = f.read()
    commands = [tuple(x.split(' ')) for x in raw.split('\n') if x]


def navigate(cmds):
    h, d = 0, 0
    for cmd in cmds:
        if cmd[0] == 'forward':
            h += int(cmd[1])
        elif cmd[0] == 'down':
            d += int(cmd[1])
        elif cmd[0] == 'up':
            d -= int(cmd[1])
        else:
            raise ValueError
    return h * d


def navigate_correction(cmds):
    h, d, a = 0, 0, 0
    for cmd in cmds:
        if cmd[0] == 'forward':
            h += int(cmd[1])
            d += (a*int(cmd[1]))
        elif cmd[0] == 'down':
            a += int(cmd[1])
        elif cmd[0] == 'up':
            a -= int(cmd[1])
        else:
            raise ValueError
    return h * d


assert navigate(commands) == 150
assert navigate_correction(commands) == 900

with open('input.txt') as f:
    raw = f.read()
    commands = [tuple(x.split(' ')) for x in raw.split('\n') if x]

print(navigate(commands))
print(navigate_correction(commands))

