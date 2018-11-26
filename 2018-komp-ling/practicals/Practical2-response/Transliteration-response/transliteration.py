import sys
"""
Russian letters -> Latin letters

#quick draft dict preparation
#je jo ju ja ; сч - sch
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

print(dict_code)

coder.close()
vow = list('аоуиыэеёюя\n ')

u = []

for line in sys.stdin.readlines():
	for letter in line:  # шифруем предложение побуквенно
		if letter in dict_code:
			if letter in vow:
				if letter in list('еёюя'):
					if letter[-1] in list('aouie\n '):
						u.append('j')
				elif letter in list('еёюя'.upper()):
					u.append('J')
			u.append(dict_code[letter])
		elif letter not in dict_code:
			u.append(letter)


c_s = ''.join(u)
print(c_s)


