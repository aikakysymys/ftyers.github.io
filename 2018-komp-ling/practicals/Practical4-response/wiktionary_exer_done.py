import sys
import re


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


stem = '_'
zkod = '_'
ipa = '_'
h1 = '_'
for line in sys.stdin.readlines():
    line = line.strip()
    text = strip_html(line);

    if line.count('<h1>') > 0:
        h1 = strip_html(line)

    if h1 != 'Русский':
        continue
    if text.count('окончание') > 0: # getting rid of 'окончание'
        text = re.sub('окончание', '', text)
    if text.count('Корень:') > 0:
        stem = text.split(':')[1].strip('.')
    if text.count('МФА') > 0:
        ipa = text.split('&#91;')[1].split('&')[0] # I had to change this line a bit due to the differences in the html file
    if text.count('тип склонения') > 0:
        zkod = text.split('тип склонения')[1].strip().split(' ')[0]

    if stem != '_' and zkod != '_' and ipa != '_':
        print('%s\t%s\t%s' % (stem, zkod, ipa))
        stem = '_'
        zkod = '_'
        ipa = '_'

