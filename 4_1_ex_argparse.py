#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3
import argparse

parser = argparse.ArgumentParser(prog = 'top',
    description = 'Show top lines from each file')
parser.add_argument('filenames', nargs='+')
parser.add_argument('-l', '--lines', type=int, default=10)
args = parser.parse_args()
print(args)

print(f'{args.filenames=}')
print(f'{args.lines=}')
