import sys

if len(sys.argv) != 2:
    sys.exit(1)
else:
    title = sys.argv[1]
    print(str(title))