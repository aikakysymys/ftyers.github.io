import sys
import re

"""
Russian letters -> Latin letters

#quick draft dict preparation (this dict needed adjustment, became dict1)
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
"""


dict_code = {} # dict to store frequency list
coder = open('dict1.txt', 'r')

for line in coder.readlines():
	if '\t' not in line:
		continue
	row = line.split('\t')
	# if there are not 2 cells, skip the line
	if len(row) != 2:
		continue
	# the sourse letter is the value of the first cell
	sourse = row[0]
	# the target letter is the value of the second cell
	dict_code[sourse] = row[1].strip('\n')

coder.close()


def transliterator():
	vow = list('аоуиыэеёюя\n ')
	u = []
	for line in sys.stdin.readlines():
		line = re.sub(r'([аоуиыэеёюя\n ])([еёюя])', r'\1j\2', line)
		print(line)
		for letter in line:  # letter turns into another letter 
			if letter in dict_code:
				u.append(dict_code[letter])
			elif letter not in dict_code:
				u.append(letter)
	result = ''.join(u)
	return result


print(transliterator())


