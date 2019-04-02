>> Functions

Code (changed to work for me)
==

freq = [[1, 'a'], [2, 'absorbed'], [8, 'all'], [4, 'and'], [5, 'another'], [6, 'opo']]

def is_palindrome(s):
	"""Return True if the given string is a palindrome."""
	rev = ''
	if len(s) == 1:
		return False
	for j in range(1, len(s) + 1):
		rev = rev + s[-j]
	if s == rev:
		return True
	return False


for i in freq:
	if is_palindrome(i[1]):
		print('%s\t%d' % (i[1], i[0]))
		
Output
==

(...)/orangejuice/PycharmProjects/Compling_2018/args.py
opo	6

Process finished with exit code 0


>> Implementing n dimensional matrices with dict

The original code works for me.

Question:
Why do we need end='' passed to the print() statement ? What would happen if we didn't have it ?
Answer: 
We'd get all zeros on new lines,  as every print() statement ends with \n by default.


>> Passing arguments from the command line

if the code of args.py is meant to be:
==

import sys


rus = ['бы', 'вас', 'видит', 'всего', 'вы']
eng = ['a', 'absorbed', 'all', 'and', 'another']

m = {}

for w1 in rus:
	if w1 not in m:
		m[w1] = {}
	for w2 in eng:
		m[w1][w2] = 0

print('\t' + '\t'.join(eng))
for w1 in m:
        print('%s\t' % (w1), end='')
        for w2 in m[w1]:
                print('%d\t' % (m[w1][w2]), end='')
        print('')

print(sys.argv)


then the outout is
==

MacBook-Air-orangejuice:Compling_2018 orangejuice$ python3 args.py a b c
        a       absorbed        all     and     another
всего   0       0       0       0       0       
бы      0       0       0       0       0       
вы      0       0       0       0       0       
вас     0       0       0       0       0       
видит   0       0       0       0       0       
['args.py', 'a', 'b', 'c']
 
That is:

Question:
$ python3 args.py a b c 
What output do you get ?
Answer: 
I'd get all the due output and a list made of filename and characters I mentioned in the command line. (strange)


Question:
What might be a simple improvement to the language model for languages with orthographic case ?
Answer:
If, like in German, where nouns are always upper-case, some part of speech is marked with capital letter, this feature could be used to give more weight to the corresponding to capitalisation class (if the word is not the first in the sentence).

