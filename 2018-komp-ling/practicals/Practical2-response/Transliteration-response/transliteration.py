import sys

#je jo ju ja ts ch sh sch  ;; сч - sch
keys = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
kl = list(keys + keys.upper())
values = 'abvgdeozzijklmnoprstufhtcss\'i\'eua'
vl = list(values + values.upper())
coder = dict(zip(kl, vl))

fd = open('dict.txt', 'w+')
for w in coder:
	fd.write('%s\t%s\n' % (w, coder[w]))
fd.close()

freq = []

fd = open('dict1.txt', 'r')
for line in fd.readlines():
	line = line.strip('\n')
	(f, w) = line.split('\t')
	freq.append((f, w))
fd.close()


for letter in sent: # шифруем предложение побуквенно
    if letter in coder:
        u.append(coder[letter])
    elif letter not in coder:
        u.append(letter)


freq = []


fd = open('text.txt', 'r')
for line in fd.readlines():
	line = line.strip('\n')
	(f, w) = line.split('\t')
	freq.append((f, w))




