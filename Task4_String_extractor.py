import argparse

parser = argparse.ArgumentParser(description='Process a string.')
parser.add_argument('string', metavar='S', type=str,
                    help='an input string')
args = parser.parse_args()

# extract float, odd, and even values from input string
floatList = []
oddList = []
evenList = []
current = ''
for c in args.string:
    if c.isdigit() or c == '.':
        current += c
    else:
        if current:
            try:
                value = float(current)
                if value.is_integer():
                    if int(value) % 2 == 0:
                        evenList.append(int(value))
                    else:
                        oddList.append(int(value))
                else:
                    floatList.append(value)
            except ValueError:
                pass
        current = ''
# append the last value if it's a number
if current:
    try:
        value = float(current)
        if value.is_integer():
            if int(value) % 2 == 0:
                evenList.append(int(value))
            else:
                oddList.append(int(value))
        else:
            floatList.append(value)
    except ValueError:
        pass

# print results
print(f'floatList: {floatList}')
print(f'oddList: {oddList}')
print(f'evenList: {evenList}')
