stage 1——————

Multichar_Symbols

%<n%>                ! Имя существительное
%<pl%>               ! Множественное число
%<nom%>              ! Именительный падеж
%<ins%>              ! Творительный падеж

%>                   ! Граница морфемы

%{A%}                ! Архифонема [а] или [е]
%{Ă%}		     ! ӑ-ӗ archiphoneme
%{м%}		     ! gen archiphoneme



LEXICON Root

Nouns ;

LEXICON SUBST 

PLURAL ;

LEXICON CASES 

%<nom%>:         # ; 
%<ins%>:%>п%{A%} # ;
%<gen%>:%>%{Ă%}н # ;

LEXICON DER-N

%<der_лӑх%>:%>л%{Ă%}х SUBST "weight: 1.0" ; 

LEXICON PLURAL

             CASES ;
%<pl%>:%>се%{м%} CASES ;

LEXICON N

%<n%>: SUBST ;
%<n%>: DER-N ;
%<n%>: PLURAL ;

LEXICON Nouns

урам:урам N ;     ! "улица"
пакча:пакча N ;   ! "сад"
хула:хула N ;     ! "город"
канаш:канаш N ;   ! "совет"
тӗс:тӗс N ;       ! "вид"
патша:патша N ;   ! "царь"
куҫ:куҫ N ;       ! "глаз"




terminal: resulting forms——————

MacBook-Air-orangejuice:bin orangejuice$ make
./hfst-lexc chv.lexc -o chv.lexc.hfst
./hfst-lexc: warning: Defaulting to OpenFst tropical type
Root...1 SUBST...1 CASES...3 DER-N...1 PLURAL...2 N...3 Nouns...
./hfst-twolc chv.twol -o chv.twol.hfst
Reading input from chv.twol.
Writing output to chv.twol.hfst.
Reading alphabet.
Reading sets.
Reading rules and compiling their contexts and centers.
Compiling rules.
Storing rules.
./hfst-compose-intersect -1 chv.lexc.hfst -2 chv.twol.hfst -o chv.gen.hfst
MacBook-Air-orangejuice:bin orangejuice$ ./hfst-compose-intersect -1 chv.lexc.hfst -2 chv.twol.hfst -o chv.gen.hfst
MacBook-Air-orangejuice:bin orangejuice$ ./hfst-invert chv.gen.hfst -o chv.mor.hfst
MacBook-Air-orangejuice:bin orangejuice$ ./hfst-fst2strings chv.mor.hfst
канаш:канаш<n><nom>
канашпа:канаш<n><ins>
канашӑн:канаш<n><gen>
канашлӗх:канаш<n><der_лӑх><nom>
канашлӗхпе:канаш<n><der_лӑх><ins>
канашлӗхӗн:канаш<n><der_лӑх><gen>
канашлӗхсен:канаш<n><der_лӑх><pl><gen>
канашлӗхсем:канаш<n><der_лӑх><pl><nom>
канашлӗхсемпе:канаш<n><der_лӑх><pl><ins>
канашсен:канаш<n><pl><gen>
канашсем:канаш<n><pl><nom>
канашсемпе:канаш<n><pl><ins>
куҫ:куҫ<n><nom>
куҫпа:куҫ<n><ins>
куҫӑн:куҫ<n><gen>
куҫлӗх:куҫ<n><der_лӑх><nom>
куҫлӗхпе:куҫ<n><der_лӑх><ins>
куҫлӗхӗн:куҫ<n><der_лӑх><gen>
куҫлӗхсен:куҫ<n><der_лӑх><pl><gen>
куҫлӗхсем:куҫ<n><der_лӑх><pl><nom>
куҫлӗхсемпе:куҫ<n><der_лӑх><pl><ins>
куҫсен:куҫ<n><pl><gen>
куҫсем:куҫ<n><pl><nom>
куҫсемпе:куҫ<n><pl><ins>
пакча:пакча<n><nom>
пакчапа:пакча<n><ins>
пакчан:пакча<n><gen>
пакчалӗх:пакча<n><der_лӑх><nom>
пакчалӗхпе:пакча<n><der_лӑх><ins>
пакчалӗхӗн:пакча<n><der_лӑх><gen>
пакчалӗхсен:пакча<n><der_лӑх><pl><gen>
пакчалӗхсем:пакча<n><der_лӑх><pl><nom>
пакчалӗхсемпе:пакча<n><der_лӑх><pl><ins>
пакчасен:пакча<n><pl><gen>
пакчасем:пакча<n><pl><nom>
пакчасемпе:пакча<n><pl><ins>
патша:патша<n><nom>
патшапа:патша<n><ins>
патшан:патша<n><gen>
патшалӗх:патша<n><der_лӑх><nom>
патшалӗхпе:патша<n><der_лӑх><ins>
патшалӗхӗн:патша<n><der_лӑх><gen>
патшалӗхсен:патша<n><der_лӑх><pl><gen>
патшалӗхсем:патша<n><der_лӑх><pl><nom>
патшалӗхсемпе:патша<n><der_лӑх><pl><ins>
патшасен:патша<n><pl><gen>
патшасем:патша<n><pl><nom>
патшасемпе:патша<n><pl><ins>
тӗс:тӗс<n><nom>
тӗспе:тӗс<n><ins>
тӗсӗн:тӗс<n><gen>
тӗслӗх:тӗс<n><der_лӑх><nom>
тӗслӗхпе:тӗс<n><der_лӑх><ins>
тӗслӗхӗн:тӗс<n><der_лӑх><gen>
тӗслӗхсен:тӗс<n><der_лӑх><pl><gen>
тӗслӗхсем:тӗс<n><der_лӑх><pl><nom>
тӗслӗхсемпе:тӗс<n><der_лӑх><pl><ins>
тӗссен:тӗс<n><pl><gen>
тӗссем:тӗс<n><pl><nom>
тӗссемпе:тӗс<n><pl><ins>
урам:урам<n><nom>
урампа:урам<n><ins>
урамӑн:урам<n><gen>
урамлӗх:урам<n><der_лӑх><nom>
урамлӗхпе:урам<n><der_лӑх><ins>
урамлӗхӗн:урам<n><der_лӑх><gen>
урамлӗхсен:урам<n><der_лӑх><pl><gen>
урамлӗхсем:урам<n><der_лӑх><pl><nom>
урамлӗхсемпе:урам<n><der_лӑх><pl><ins>
урамсен:урам<n><pl><gen>
урамсем:урам<n><pl><nom>
урамсемпе:урам<n><pl><ins>
хула:хула<n><nom>
хулапа:хула<n><ins>
хулан:хула<n><gen>
хулалӗх:хула<n><der_лӑх><nom>
хулалӗхпе:хула<n><der_лӑх><ins>
хулалӗхӗн:хула<n><der_лӑх><gen>
хулалӗхсен:хула<n><der_лӑх><pl><gen>
хулалӗхсем:хула<n><der_лӑх><pl><nom>
хулалӗхсемпе:хула<n><der_лӑх><pl><ins>
хуласен:хула<n><pl><gen>
хуласем:хула<n><pl><nom>
хуласемпе:хула<n><pl><ins>



./hfst-lexc chv.lexc -o chv.lexc.hfst
./hfst-twolc chv.twol -o chv.twol.hfst
./hfst-compose-intersect -1 chv.lexc.hfst -2 chv.twol.hfst -o chv.gen.hfst
./hfst-invert chv.gen.hfst -o chv.mor.hfst
echo патшалӑх | ./hfst-lookup -qp chv.mor.hfst 
патшалӑх	патшалӑх+?	inf


/bin/echo -n "$b " патшалӑх | ./hfst-lookup -qp chv.mor.hfst       работает! но echo тоже
патшалӑх	патшалӑх+?	inf

MacBook-Air-orangejuice:bin orangejuice$ echo "тӗслӗх" |./hfst-lookup -qp -b 0 chv.mor.hfst
тӗслӗх	тӗс<n><der_лӑх><nom>	1.000000

MacBook-Air-orangejuice:bin orangejuice$ echo патша | ./hfst-lookup -qp -b 0 chv.mor.hfst
патша	патша<n><nom>	0.000000




stage 2——————


chv.crp.txt



Çурхи тěнче вăраннă чух:
Хаваслă кун шăраннă чух,
Чун савăнать: чěре сикет,
Çěршывăм çинчен юрлас килет

припев:
Тăван çěршыв,
Тăван çěршыв,
Асран кайми
Юратнă çěршыв.
Тăван çěршыв,
Тăван çěршыв,
Мухтав сана,
Çуралнă çěршыв!

Тăвансемпе пěрлешнě чух,
Чăваш тěнчи çěкленнě чух,
Чун савăнать: чěре сикет,
Татах та хастар пулас килет.

Яшсем-херсем вылянă чух,
Атте-анне ăс панă чух,
Чун савăнать: чěре сикет,
Татах та нумай пурнас килет


terminal: resulting forms——————

cat ./chv.crp.txt  | sed 's/[^а-яӑӗăĕҫçА-ЯӐӖĂĔҪÇ]\+/ /g' | tr ' ' '\n' | sort -f | uniq -c | sort -gr
   5 чух,
   4 Тăван
   4 çěршыв,
   3 савăнать:
   3 сикет,
   3 чěре
   3 Чун
   3 
   2 килет
   2 Татах
   2 та
   1 Тăвансемпе
   1 пěрлешнě
   1 шăраннă
   1 вăраннă
   1 Хаваслă
   1 припев:
   1 хастар
   1 пурнас
   1 вылянă
   1 Юратнă
   1 Мухтав
   1 килет.
   1 Яшсем-херсем
   1 юрлас
   1 тěнчи
   1 тěнче
   1 пулас
   1 нумай
   1 кайми
   1 Чăваш
   1 Асран
   1 Атте-анне
   1 сана,
   1 панă
   1 чух:
   1 кун
   1 ăс
   1 çěкленнě
   1 çěршыв.
   1 çěршыв!
   1 çинчен
   1 Çěршывăм
   1 Çуралнă
   1 Çурхи



stage 2——————

Alphabet
  а ӑ е ё ӗ и о у ӳ ы э ю я б в г д ж з к л м н п р с ҫ т ф х ц ч ш щ й ь ъ
  А Ӑ Е Ё Ӗ И О У Ӳ Ы Э Ю Я Б В Г Д Ж З К Л М Н П Р С Ҫ Т Ф Х Ц Ч Ш Щ Й Ь Ъ 
 %{A%}:а %{A%}:е
 %{Ă%}:ӑ %{Ă%}:ӗ %{Ă%}:0
 %{м%}:м %{м%}:0

;

Sets 

BackVow = ӑ а ы о у я ё ю %{ъ%} ;

FrontVow = ӗ э и ӳ ; 

Cns = б в г д ж з к л м н п р с ҫ т ф х ц ч ш щ й ь ъ ; 

Vow = а ӑ е ё ӗ и о у ӳ ы э ю я ;

ArchiCns = %{м%} ;

Rules 

"Remove morpheme boundary"
%>:0 <=> _ ;

"Back vowel harmony for archiphoneme {A}"
%{A%}:а <=> BackVow: [ Cns: | %>: ]+ _ ; 

"Non surface {м} in plural genitive"
%{м%}:0 <=> _ %>: %{Ă%}: н ;

"Back vowel harmony for archiphoneme {Ă}"
%{Ă%}:ӑ <=> BackVow: [ ArchiCns: | Cns: | %>: ]+ _ ;




Multichar_Symbols

%<n%>                ! Имя существительное
%<pl%>               ! Множественное число
%<nom%>              ! Именительный падеж
%<ins%>              ! Творительный падеж

%>                   ! Граница морфемы

%{A%}                ! Архифонема [а] или [е]
%{Ă%}		     ! ӑ-ӗ archiphoneme
%{м%}		     ! gen archiphoneme



LEXICON Root

Nouns ;

LEXICON SUBST 

PLURAL ;

LEXICON CASES 

%<nom%>:         # ; 
%<ins%>:%>п%{A%} # ;
%<gen%>:%>%{Ă%}н # ;

LEXICON DER-N

%<der_лӑх%>:%>л%{Ă%}х SUBST "weight: 1.0" ; 

LEXICON PLURAL

             CASES ;
%<pl%>:%>се%{м%} CASES ;

LEXICON N

%<n%>: SUBST ;
%<n%>: DER-N ;
%<n%>: PLURAL ;

LEXICON Nouns

урам:урам N ;     ! "улица"
пакча:пакча N ;   ! "сад"
хула:хула N ;     ! "город"
канаш:канаш N ;   ! "совет"
тӗс:тӗс N ;       ! "вид"
патша:патша N ;   ! "царь"
куҫ:куҫ N ;       ! "глаз"
специалист:специалист%{ъ%} N ; ! "специалист"




terminal: resulting forms——————

./hfst-lexc chv.lexc -o chv.lexc.hfst
MacBook-Air-orangejuice:bin orangejuice$ ./hfst-twolc chv.twol -o chv.twol.hfst
Reading input from chv.twol.
Writing output to chv.twol.hfst.
Reading alphabet.
Reading sets.
Reading rules and compiling their contexts and centers.
Compiling rules.
Storing rules.
MacBook-Air-orangejuice:bin orangejuice$ ./hfst-compose-intersect -1 chv.lexc.hfst -2 chv.twol.hfst -o chv.gen.hfst
MacBook-Air-orangejuice:bin orangejuice$ ./hfst-invert chv.gen.hfst -o chv.mor.hfst


MacBook-Air-orangejuice:bin orangejuice$ ./hfst-fst2strings chv.lexc.hfst | grep специалист | grep gen
специалист<n><der_лӑх><gen>:специалист{ъ}>л{Ă}х>{Ă}н
специалист<n><der_лӑх><pl><gen>:специалист{ъ}>л{Ă}х>се{м}>{Ă}н
специалист<n><gen>:специалист{ъ}>{Ă}н
специалист<n><pl><gen>:специалист{ъ}>се{м}>{Ă}н



total=`cat chv.crp.txt  | sed 's/[^а-яӑӗăĕҫçА-ЯӐӖĂĔҪÇ]\+/ /g' | tr ' ' '\n'  | grep -v '^$' | wc -l`
unknown=`cat chv.crp.txt  | sed 's/[^а-яӑӗăĕҫçА-ЯӐӖĂĔҪÇ]\+/ /g' | tr ' ' '\n'  | grep -v '^$' | ./hfst-lookup -qp chv.mor.hfst  | grep 'inf' | wc -l`
MacBook-Air-orangejuice:bin orangejuice$ calc "(($total-$unknown)/$total)*100"
	0

____________Generating paradigms

MacBook-Air-orangejuice:bin orangejuice$ echo "у р а м %<n%> ?*" | ./hfst-regexp2fst -o uram.hfst
MacBook-Air-orangejuice:bin orangejuice$ ./hfst-compose-intersect -2 chv.gen.hfst -1 uram.hfst | ./hfst-fst2strings
./hfst-compose-intersect: warning: 
Found output symbols (e.g. "@_IDENTITY_SYMBOL_@") in transducer in
file uram.hfst which will be filtered out because they are
not found on the input tapes of transducers in file
chv.gen.hfst.
урам<n><nom>:урам
урам<n><ins>:урампа
урам<n><gen>:урамӑн
урам<n><der_лӑх><nom>:урамлӑх
урам<n><der_лӑх><ins>:урамлӑхпе
урам<n><der_лӑх><gen>:урамлӑхн
урам<n><der_лӑх><gen>:урамлӑхӗн
урам<n><der_лӑх><pl><gen>:урамлӑхсен
урам<n><der_лӑх><pl><gen>:урамлӑхсеӗн
урам<n><der_лӑх><pl><nom>:урамлӑхсем
урам<n><der_лӑх><pl><ins>:урамлӑхсемпе
урам<n><pl><gen>:урамсен
урам<n><pl><gen>:урамсеӗн
урам<n><pl><nom>:урамсем
урам<n><pl><ins>:урамсемпе





MacBook-Air-orangejuice:bin orangejuice$ cat noun-paradigm.tx
%<n%> %<nom%>
%<n%> %<gen%>
%<n%> %<ins%>
%<n%> %<pl%> %<gen%>
%<n%> %<pl%> %<nom%>
%<n%> %<pl%> %<ins%>MacBook-Air-orangejuicat noun-paradigm.txt | sed "s/^/у р аsм /g"  | ./hfst-regexp2fst -j > uram.hfst 
MacBook-Air-orangejuice:bin orangejuice$ ./hfst-compose-intersect -2 chv.gen.hfst -1 uram.hfst | ./hfst-fst2strings 
./hfst-compose-intersect: warning: 
Found output symbols (e.g. "<gen>") in transducer in
file uram.hfst which will be filtered out because they are
not found on the input tapes of transducers in file
chv.gen.hfst.
урам<n><nom>:урам
урам<n><ins>:урампа
урам<n><pl><nom>:урамсем
урам<n><pl><ins>:урамсемпе


