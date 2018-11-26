Question:

What do you think we would get if we set the argument reverse to False ?

Answer: 

We'll get the less frequent words first, not the most frequent.



import sys

vocab = {} # dict to store frequency list

# for each of the lines of input
for line in sys.stdin.readlines():
	# if there is no tab character, skip the line
	if '\t' not in line:
		continue
	# make a list of the cells in the row
	row = line.split('\t')
	# if there are not 10 cells, skip the line
	if len(row) != 10:
		continue
	# the form is the value of the second cell
	form = row[1]
	# if we haven't seen it yet, set the frequency count to 0
	if form not in vocab:
		vocab[form] = 0
	vocab[form] = vocab[form] + 1

freq = []
# print out the frequency listΩ≈
for w in vocab:
    freq.append((vocab[w], w))

freq.sort(reverse=True)

#for w in freq:
#    print('%d\t%s' % (w[0], w[1]))

fd = open('freq.txt', 'w+')
for w in vocab:
	fd.write('%d\t%s\n' % (vocab[w], w))
fd.close()

fd = open('freq.txt', 'r')
for line in fd.readlines():
	line = line.strip('\n')
	(f, w) = line.split('\t')
	freq.append((int(f), w))
fd.close()

print(freq)


------------------------Terminal response

MacBook-Air-orangejuice:Compling_2018 orangejuice$ cat transliteration_input.txt | python transliteration.py
1       течение
1       следует
1       Это
MacBook-Air-orangejuice:Compling_2018 orangejuice$ cat transliteration_input.txt | python transliteration.py
[(1, 'течение'), (1, 'следует'), (1, 'Это')]





rank.py______________

import sys

freq = []

fd = open('freq.txt', 'r')
for line in fd.readlines():
	line = line.strip('\n')
	(f, w) = line.split('\t')
	freq.append((int(f), w))

print(len(freq))

rank = 1
min = freq[0][0]
ranks = []
for i in range(0, len(freq)):
	if freq[i][0] < min:
		rank = rank + 1
		min = freq[i][0]
	ranks.append((rank, freq[i][0], freq[i][1]))
	print('%d\t%d\t%s' % (ranks[i][0], ranks[i][1], ranks[i][2])) # to make more efficient

#for w in ranks:
#    print('%d\t%d\t%s'%(w[0],w[1],w[2]))


------------------------Terminal response

MacBook-Air-orangejuice:Compling_2018 orangejuice$ cat transliteration_input.txt | python rank.py
3
1       1       Это
1       1       течение
1       1       следует

