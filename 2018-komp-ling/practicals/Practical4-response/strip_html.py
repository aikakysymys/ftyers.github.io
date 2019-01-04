import sys


def strip_html(h):
	o = ''
	inTag = False
	for c in h: 
		if c == '<':
			inTag = True
			continue
		if c == '>':
			inTag = False
			continue
		if not inTag:
			o = o + c
	return o


for line in sys.stdin.readlines():
    print(strip_html(line))
