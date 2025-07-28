from sys import argv, stderr, exit

RED = r'\033[91m'
RESET = r'\033[0m'

with open(argv[1], 'r') as f:
    code = f.read()

accumulator = 0

for item in code:
    if item == '+':
        accumulator += 1
    elif item == '!':
        print(chr(accumulator))
    elif item == '~':
        accumulator = 0
    else:
        print(f'{RED}Error...{RESET}', file=stderr)
        exit(1)