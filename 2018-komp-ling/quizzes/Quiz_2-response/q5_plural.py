import sys

if len(sys.argv) > 1:
    instream = open(sys.argv[1])
else:
    instream = sys.stdin

pl = ''


def plural(words):
    for word in words:
        word = word.strip('\n')
        if word.endswith(('ch', 'x', 'z', 's', 'sh')):
            pl = word + 'es'
            print(pl)
        else:
            pl = word + 's'
            print(pl)
    return pl


print(plural(instream))
