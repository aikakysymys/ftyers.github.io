stage 1——————









stage 2——————

define Vow [ ӑ | а | ы | о | у | я | ё | ю | ӗ | э | и | ӳ ] ;

define Cns [ б | в | г | д | ж | з | к | л | м | н | п | р | с | ҫ | т | ф | х | ц | ч | ш | щ | й | ь | ъ ] ;

define Syll [ Cns+ Vow Cns* ] ;

define Stem [ Syll+ ]  ;

regex Stem ;


terminal: resulting forms——————

MacBook-Air-orangejuice:bin orangejuice$ echo -e "source chv.stem.regex\nsave stack chv.stem.hfst\nhyvästi" | ./hfst-xfst
 Defined
 'Vow'
Defined
 'Cns'
Defined
 'Syll'
Defined
 'Stem'
? bytes. 4 states, 120 arcs, ? paths
.
MacBook-Air-orangejuice:bin orangejuice$ 



MacBook-Air-orangejuice:bin orangejuice$ ./hfst-lexc chv.lexc -o chv.lexc.hfst
./hfst-lexc: warning: Defaulting to OpenFst tropical type
Root...2 Guesser...1 SUBST...1 CASES...3 DER-N...1 PLURAL...2 N...3 Nouns...
MacBook-Air-orangejuice:bin orangejuice$ ./hfst-substitute -i chv.lexc.hfst -o chv.lexc_guesser.hfst  -f '🂡:🂡' -T chv.stem.hfst
MacBook-Air-orangejuice:bin orangejuice$ echo "ва<guess><n><ins>" | ./hfst-lookup -qp chv.lexc.hfst
ва<guess><n><ins>	ва<guess><n><ins>+?	inf


MacBook-Air-orangejuice:bin orangejuice$ echo "ва<guess><n><ins>" | ./hfst-lookup -qp chv.lexc_guesser.hfst
ва<guess><n><ins>	ва>п{A}	0.000000


MacBook-Air-orangejuice:bin orangejuice$ ./hfst-compose-intersect -1 chv.lexc_guesser.hfst -2 chv.twol.hfst -o chv.gen_guesser.hfst
MacBook-Air-orangejuice:bin orangejuice$ echo "лайк<guess><n><pl><ins>" | ./hfst-lookup -qp chv.gen_guesser.hfst
лайк<guess><n><pl><ins>	лайксемпе	0.000000




______________chv.restrict.regex

~[?* "<guess>" "<n>" "<nom>" ] .o. [  [..] -> "<guess>" || "<guess>" ?* _ .#. .o. "<guess>" -> 0 || _ ?* "<guess>" .#. ];

added to chv.lexc:


LEXICON Root

Nouns ;
Guesser ;

LEXICON Guesser

🂡%<guess%>:🂡 N ;




terminal: resulting forms——————

MacBook-Air-orangejuice:bin orangejuice$ ./hfst-regexp2fst chv.restrict.regex -o chv.restrict.hfst
MacBook-Air-orangejuice:bin orangejuice$ ./hfst-invert chv.gen_guesser.hfst | ./hfst-compose -1 - -2 chv.restrict.hfst -o chv.mor_guesser.hfst
MacBook-Air-orangejuice:bin orangejuice$ echo "лайксемпе" | ./hfst-lookup -qp chv.mor_guesser.hfst
лайксемпе	лайк<guess><n><pl><ins>	0.000000



Weighting___________

 added to chv.lexc:

LEXICON N/сть

%<n%>:ҫ SUBST "weight: 0.5" ;
%<n%>%<nom%>:сть # "weight: 1.0" ;


обла:обла N/сть ; ! область


terminal: resulting forms——————

MacBook-Air-orangejuice:bin orangejuice$ cat chv.crp.txt  | sed 's/[^а-яӑӗăĕҫçА-ЯӐӖĂĔҪÇ]\+/ /g' | tr ' ' '\n' | sort -f | uniq -c | sort -gr  > chv.freq.txtt
MacBook-Air-orangejuice:bin orangejuice$ cat chv.freq.txt | python3 freq2prob.py | ./hfst-strings2fst -j -o chv.surweights.hfst
MacBook-Air-orangejuice:bin orangejuice$ echo "область" | ./hfst-lookup -qp chv.surweights.hfst
область	область+?	inf



MacBook-Air-orangejuice:bin orangejuice$ ./hfst-fst2strings chv.lexc.hfst
🂡<guess><n><der_лӑх><gen>:🂡>л{Ă}х>{Ă}н
🂡<guess><n><der_лӑх><nom>:🂡>л{Ă}х
🂡<guess><n><der_лӑх><ins>:🂡>л{Ă}х>п{A}
🂡<guess><n><der_лӑх><pl><gen>:🂡>л{Ă}х>се{м}>{Ă}н
🂡<guess><n><der_лӑх><pl><nom>:🂡>л{Ă}х>се{м}
🂡<guess><n><der_лӑх><pl><ins>:🂡>л{Ă}х>се{м}>п{A}
🂡<guess><n><gen>:🂡>{Ă}н
🂡<guess><n><nom>:🂡
🂡<guess><n><ins>:🂡>п{A}
🂡<guess><n><pl><gen>:🂡>се{м}>{Ă}н
🂡<guess><n><pl><nom>:🂡>се{м}
🂡<guess><n><pl><ins>:🂡>се{м}>п{A}
специалист<n><der_лӑх><gen>:специалист{ъ}>л{Ă}х>{Ă}н
специалист<n><der_лӑх><nom>:специалист{ъ}>л{Ă}х
специалист<n><der_лӑх><ins>:специалист{ъ}>л{Ă}х>п{A}
специалист<n><der_лӑх><pl><gen>:специалист{ъ}>л{Ă}х>се{м}>{Ă}н
специалист<n><der_лӑх><pl><nom>:специалист{ъ}>л{Ă}х>се{м}
специалист<n><der_лӑх><pl><ins>:специалист{ъ}>л{Ă}х>се{м}>п{A}
специалист<n><gen>:специалист{ъ}>{Ă}н
специалист<n><nom>:специалист{ъ}
специалист<n><ins>:специалист{ъ}>п{A}
специалист<n><pl><gen>:специалист{ъ}>се{м}>{Ă}н
специалист<n><pl><nom>:специалист{ъ}>се{м}
специалист<n><pl><ins>:специалист{ъ}>се{м}>п{A}
тӗс<n><der_лӑх><gen>:тӗс>л{Ă}х>{Ă}н
тӗс<n><der_лӑх><nom>:тӗс>л{Ă}х
тӗс<n><der_лӑх><ins>:тӗс>л{Ă}х>п{A}
тӗс<n><der_лӑх><pl><gen>:тӗс>л{Ă}х>се{м}>{Ă}н
тӗс<n><der_лӑх><pl><nom>:тӗс>л{Ă}х>се{м}
тӗс<n><der_лӑх><pl><ins>:тӗс>л{Ă}х>се{м}>п{A}
тӗс<n><gen>:тӗс>{Ă}н
тӗс<n><nom>:тӗс
тӗс<n><ins>:тӗс>п{A}
тӗс<n><pl><gen>:тӗс>се{м}>{Ă}н
тӗс<n><pl><nom>:тӗс>се{м}
тӗс<n><pl><ins>:тӗс>се{м}>п{A}
патша<n><der_лӑх><gen>:патша>л{Ă}х>{Ă}н
патша<n><der_лӑх><nom>:патша>л{Ă}х
патша<n><der_лӑх><ins>:патша>л{Ă}х>п{A}
патша<n><der_лӑх><pl><gen>:патша>л{Ă}х>се{м}>{Ă}н
патша<n><der_лӑх><pl><nom>:патша>л{Ă}х>се{м}
патша<n><der_лӑх><pl><ins>:патша>л{Ă}х>се{м}>п{A}
патша<n><gen>:патша>{Ă}н
патша<n><nom>:патша
патша<n><ins>:патша>п{A}
патша<n><pl><gen>:патша>се{м}>{Ă}н
патша<n><pl><nom>:патша>се{м}
патша<n><pl><ins>:патша>се{м}>п{A}
пакча<n><der_лӑх><gen>:пакча>л{Ă}х>{Ă}н
пакча<n><der_лӑх><nom>:пакча>л{Ă}х
пакча<n><der_лӑх><ins>:пакча>л{Ă}х>п{A}
пакча<n><der_лӑх><pl><gen>:пакча>л{Ă}х>се{м}>{Ă}н
пакча<n><der_лӑх><pl><nom>:пакча>л{Ă}х>се{м}
пакча<n><der_лӑх><pl><ins>:пакча>л{Ă}х>се{м}>п{A}
пакча<n><gen>:пакча>{Ă}н
пакча<n><nom>:пакча
пакча<n><ins>:пакча>п{A}
пакча<n><pl><gen>:пакча>се{м}>{Ă}н
пакча<n><pl><nom>:пакча>се{м}
пакча<n><pl><ins>:пакча>се{м}>п{A}
хула<n><der_лӑх><gen>:хула>л{Ă}х>{Ă}н
хула<n><der_лӑх><nom>:хула>л{Ă}х
хула<n><der_лӑх><ins>:хула>л{Ă}х>п{A}
хула<n><der_лӑх><pl><gen>:хула>л{Ă}х>се{м}>{Ă}н
хула<n><der_лӑх><pl><nom>:хула>л{Ă}х>се{м}
хула<n><der_лӑх><pl><ins>:хула>л{Ă}х>се{м}>п{A}
хула<n><gen>:хула>{Ă}н
хула<n><nom>:хула
хула<n><ins>:хула>п{A}
хула<n><pl><gen>:хула>се{м}>{Ă}н
хула<n><pl><nom>:хула>се{м}
хула<n><pl><ins>:хула>се{м}>п{A}
урам<n><der_лӑх><gen>:урам>л{Ă}х>{Ă}н
урам<n><der_лӑх><nom>:урам>л{Ă}х
урам<n><der_лӑх><ins>:урам>л{Ă}х>п{A}
урам<n><der_лӑх><pl><gen>:урам>л{Ă}х>се{м}>{Ă}н
урам<n><der_лӑх><pl><nom>:урам>л{Ă}х>се{м}
урам<n><der_лӑх><pl><ins>:урам>л{Ă}х>се{м}>п{A}
урам<n><gen>:урам>{Ă}н
урам<n><nom>:урам
урам<n><ins>:урам>п{A}
урам<n><pl><gen>:урам>се{м}>{Ă}н
урам<n><pl><nom>:урам>се{м}
урам<n><pl><ins>:урам>се{м}>п{A}
куҫ<n><der_лӑх><gen>:куҫ>л{Ă}х>{Ă}н
куҫ<n><der_лӑх><nom>:куҫ>л{Ă}х
куҫ<n><der_лӑх><ins>:куҫ>л{Ă}х>п{A}
куҫ<n><der_лӑх><pl><gen>:куҫ>л{Ă}х>се{м}>{Ă}н
куҫ<n><der_лӑх><pl><nom>:куҫ>л{Ă}х>се{м}
куҫ<n><der_лӑх><pl><ins>:куҫ>л{Ă}х>се{м}>п{A}
куҫ<n><gen>:куҫ>{Ă}н
куҫ<n><nom>:куҫ
куҫ<n><ins>:куҫ>п{A}
куҫ<n><pl><gen>:куҫ>се{м}>{Ă}н
куҫ<n><pl><nom>:куҫ>се{м}
куҫ<n><pl><ins>:куҫ>се{м}>п{A}
канаш<n><der_лӑх><gen>:канаш>л{Ă}х>{Ă}н
канаш<n><der_лӑх><nom>:канаш>л{Ă}х
канаш<n><der_лӑх><ins>:канаш>л{Ă}х>п{A}
канаш<n><der_лӑх><pl><gen>:канаш>л{Ă}х>се{м}>{Ă}н
канаш<n><der_лӑх><pl><nom>:канаш>л{Ă}х>се{м}
канаш<n><der_лӑх><pl><ins>:канаш>л{Ă}х>се{м}>п{A}
канаш<n><gen>:канаш>{Ă}н
канаш<n><nom>:канаш
канаш<n><ins>:канаш>п{A}
канаш<n><pl><gen>:канаш>се{м}>{Ă}н
канаш<n><pl><nom>:канаш>се{м}
канаш<n><pl><ins>:канаш>се{м}>п{A}
обла<n><gen>:облаҫ>{Ă}н
обла<n><nom>:облаҫ
обла<n><ins>:облаҫ>п{A}
обла<n><pl><gen>:облаҫ>се{м}>{Ă}н
обла<n><pl><nom>:облаҫ>се{м}
обла<n><pl><ins>:облаҫ>се{м}>п{A}
обла<n><nom>:область

_______________

in python:


in:

import hfst

ifs = hfst.HfstInputStream('chv.gen.hfst') # set up an input stream
transducer = ifs.read()                    # read the first transducer
transducer.invert()                        # invert the transducer
transducer.lookup('урамӑн')

out:

(('урам<n><gen>', 0.0),)




