Regular expressions

>>> import re
>>> s = 'Привет мир!'
>>> re.search(r'м[а-я]+', s)
<_sre.SRE_Match object; span=(7, 10), match='мир'>
>>> m = re.search(r'м[а-я]+', s)
>>> m.group()
'мир'
>>> m.span()
(7, 10)
>>> 
>>> re.sub('[а-я]', 'р', s)
'Пррррр ррр!'
>>> 


ElementTree

terminal response:


aika$ cat isl-ex.xml | python3 gloss.py
xigt-corpus
(Þau) Jón og María eru vinir.
they.NEUT Jón og María are friends
Jón and María are friends.


scikit learn

Answers:
Code:
pronunciation.py 
pronunciation_exercise.py with data split into training and test, where accuracy: 0.9945 
The classifier makes errors if ‘ь’ is at the end of a word, so to improve accuracy one might consider ‘ь’ at the end of the word as simply the end of the word (#).

Terminal:

python3 pronunciation_exercise.py
/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/sklearn/linear_model/stochastic_gradient.py:152: DeprecationWarning: n_iter parameter is deprecated in 0.19 and will be removed in 0.21. Use max_iter and tol instead.
DeprecationWarning)
- 0 ('#хоругвь#', '[xɐˈrukfʲ]', 1)
- 0 ('#церковь#', '[ˈt͡sɛrkəfʲ]', 1)
- 0 ('#червь#', '[t͡ɕerfʲ]', 1)
- 0 ('#явь#', '[jæfʲ]', 1)
727
731
0.9945280437756497


Screenscraping


----> The given command didn’t work, so I wgetted the file another way:

python3 -m wget "http://ru.wiktionary.org/wiki/страх"
100% [........................................................] 248307 / 248307
Saved under страх



----> After using the function (strip_html.py), terminal output:

страх

Существительное, неодушевлённое, мужской род, 2-е склонение&#32;(тип склонения 3a  по классификации А.&#160;А.&#160;Зализняка).

Корень: -страх-.



Произношение

МФА: ед.&#160;ч.&#160;&#91;strax&#93;(файл) мн.&#160;ч.&#160;&#91;ˈstraxʲɪ&#93;


----> After running the script wiktionary.py (I had to alter the given code a bit, as my ‘страх’ file is a bit different), terminal output:

(venv) bash-3.2$ cat страх | python3 wiktionary.py
-страх-        3a      strax


----> After running the script wiktionary.py for дерево, terminal:

(venv) bash-3.2$ cat дерево | python3 wiktionary.py
-дерев-; окончание     1a^     ˈdʲerʲɪvə
--     по      ˈd̪ɛ.rɛ̝.wɔ



Tagger.py


The tagger I’ve made you can find in the tagger folder. It takes two arguments (model.tsv and imputes.tsv), its output.tsv is also there.
