stage 1——————

Multichar_Symbols

%<n%>                ! Имя существительное
%<pl%>               ! Множественное число

%>                   ! Граница морфемы

LEXICON Root

Nouns ; 

LEXICON PLURAL

             # ; 
%<pl%>:%>сем # ;

LEXICON N 

%<n%>: PLURAL ;

LEXICON Nouns

урам:урам N ;     ! "улица"
пакча:пакча N ;   ! "сад"
хула:хула N ;     ! "город"


terminal: resulting forms——————

Root...1 PLURAL...2 N...1 Nouns...
урам<n>:урам
урам<n><pl>:урам>сем
пакча<n>:пакча
пакча<n><pl>:пакча>сем
хула<n>:хула
хула<n><pl>:хула>сем


stage 2——————

Multichar_Symbols

%<n%>                ! Имя существительное
%<pl%>               ! Множественное число

%>                   ! Граница морфемы

LEXICON Root

Nouns ; 

LEXICON CASES-BACK

%<ins%>:%>па # ; 

LEXICON CASES-FRONT

%<ins%>:%>пе # ; 

LEXICON CASES

CASES-FRONT ;
CASES-BACK ;

LEXICON PLURAL

             # ; 
%<pl%>:%>сем # ;

LEXICON N 

%<n%>: PLURAL ;
%<n%>: CASES ;

LEXICON Nouns

урам:урам N ;     ! "улица"
пакча:пакча N ;   ! "сад"
хула:хула N ;     ! "город"


terminal: resulting forms——————

Root...1 CASES-BACK...1 CASES-FRONT...1 CASES...2 PLURAL...2 N...2 Nouns...
пакча<n>:пакча
пакча<n><pl>:пакча>сем
пакча<n><ins>:пакча>пе
пакча<n><ins>:пакча>па
урам<n>:урам
урам<n><pl>:урам>сем
урам<n><ins>:урам>пе
урам<n><ins>:урам>па
хула<n>:хула
хула<n><pl>:хула>сем
хула<n><ins>:хула>пе
хула<n><ins>:хула>па



stage 3——————

Multichar_Symbols

%{A%}		     ! Архифонема для Ins
%<n%>                ! Имя существительное
%<pl%>               ! Множественное число

%>                   ! Граница морфемы

LEXICON Root

Nouns ; 

LEXICON CASES

%<ins%>:%>п%{A%} # ;

LEXICON PLURAL

             CASES ; 
%<pl%>:%>сем CASES ;

LEXICON N 

%<n%>: PLURAL ;
%<n%>: CASES ;

LEXICON Nouns

урам:урам N ;     ! "улица"
пакча:пакча N ;   ! "сад"
хула:хула N ;     ! "город"


terminal: resulting forms——————

Root...1 CASES...1 PLURAL...2 N...2 Nouns...
пакча<n><pl><ins>:пакча>сем>п{A}
пакча<n><ins>:пакча>п{A}
урам<n><pl><ins>:урам>сем>п{A}
урам<n><ins>:урам>п{A}
хула<n><pl><ins>:хула>сем>п{A}
хула<n><ins>:хула>п{A}


stage 4 ——————

Alphabet
  а ӑ е ё ӗ и о у ӳ ы э ю я б в г д ж з к л м н п р с ҫ т ф х ц ч ш щ й ь ъ
  А Ӑ Е Ё Ӗ И О У Ӳ Ы Э Ю Я Б В Г Д Ж З К Л М Н П Р С Ҫ Т Ф Х Ц Ч Ш Щ Й Ь Ъ 
 %{A%}:а %{A%}:е
;

Rules 

"Remove morpheme boundary"
%>:0 <=> _ ;


terminal: resulting forms——————

./hfst-fst2strings chv.gen.hfst
пакча<n><ins>:пакчапа
пакча<n><ins>:пакчапе
пакча<n><pl><ins>:пакчасемпа
пакча<n><pl><ins>:пакчасемпе
урам<n><ins>:урампа
урам<n><ins>:урампе
урам<n><pl><ins>:урамсемпа
урам<n><pl><ins>:урамсемпе
хула<n><ins>:хулапа
хула<n><ins>:хулапе
хула<n><pl><ins>:хуласемпа
хула<n><pl><ins>:хуласемпе

stage 5 ——————

Alphabet
  а ӑ е ё ӗ и о у ӳ ы э ю я б в г д ж з к л м н п р с ҫ т ф х ц ч ш щ й ь ъ
  А Ӑ Е Ё Ӗ И О У Ӳ Ы Э Ю Я Б В Г Д Ж З К Л М Н П Р С Ҫ Т Ф Х Ц Ч Ш Щ Й Ь Ъ 
 %{A%}:а %{A%}:е
 %{Ă%}:ӑ %{Ă%}:ӗ %{Ă%}:0
 %{м%}:м %{м%}:0

;

Sets 

BackVow = ӑ а ы о у я ё ю ;

FrontVow = ӗ э и ӳ ; 

Cns = б в г д ж з к л м н п р с ҫ т ф х ц ч ш щ й ь ъ ; 

ArchiCns = %{м%} ;

Rules 

"Remove morpheme boundary"
%>:0 <=> _ ;

"Back vowel harmony for archiphoneme {A}"
%{A%}:а <=> BackVow: [ Cns: | %>: ]+ _ ; 

"Back vowel harmony for archiphoneme {Ă}"
%{Ă%}:ӑ <=> BackVow: [ ArchiCns: | Cns: | %>: ]+ _ ;
        except
                                     %{м%}: %>:  _ н ; 

"No surface {Ă} in plural genitive"
%{Ă%}:0 <=> %{м%}: %>: _ н ;

——————

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


LEXICON CASES 

%<nom%>:         # ; 
%<ins%>:%>п%{A%} # ;
%<gen%>:%>%{Ă%}н # ;

LEXICON PLURAL

             CASES ;
%<pl%>:%>се%{м%} CASES ;

LEXICON N

%<n%>: PLURAL ;

LEXICON Nouns

урам:урам N ;     ! "улица"
пакча:пакча N ;   ! "сад"
хула:хула N ;     ! "город"
канаш:канаш N ;   ! "совет"

terminal: resulting forms——————

./hfst-fst2strings chv.gen.hfst
канаш<n><nom>:канаш
канаш<n><ins>:канашпа
канаш<n><gen>:канашӑн
канаш<n><pl><nom>:канашсе
канаш<n><pl><ins>:канашсепе
канаш<n><pl><gen>:канашсен
канаш<n><pl><nom>:канашсем
канаш<n><pl><ins>:канашсемпе
канаш<n><pl><gen>:канашсемн
пакча<n><nom>:пакча
пакча<n><ins>:пакчапа
пакча<n><gen>:пакчаӑн
пакча<n><pl><nom>:пакчасе
пакча<n><pl><ins>:пакчасепе
пакча<n><pl><gen>:пакчасен
пакча<n><pl><nom>:пакчасем
пакча<n><pl><ins>:пакчасемпе
пакча<n><pl><gen>:пакчасемн
урам<n><nom>:урам
урам<n><ins>:урампа
урам<n><gen>:урамӑн
урам<n><pl><nom>:урамсе
урам<n><pl><ins>:урамсепе
урам<n><pl><gen>:урамсен
урам<n><pl><nom>:урамсем
урам<n><pl><ins>:урамсемпе
урам<n><pl><gen>:урамсемн
хула<n><nom>:хула
хула<n><ins>:хулапа
хула<n><gen>:хулаӑн
хула<n><pl><nom>:хуласе
хула<n><pl><ins>:хуласепе
хула<n><pl><gen>:хуласен
хула<n><pl><nom>:хуласем
хула<n><pl><ins>:хуласемпе
хула<n><pl><gen>:хуласемн





stage 6 ——————

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


LEXICON CASES 

%<nom%>:         # ; 
%<ins%>:%>п%{A%} # ;
%<gen%>:%>%{Ă%}н # ;

LEXICON PLURAL

             CASES ;
%<pl%>:%>се%{м%} CASES ;

LEXICON N

%<n%>: PLURAL ;

LEXICON Nouns

урам:урам N ;     ! "улица"
пакча:пакча N ;   ! "сад"
хула:хула N ;     ! "город"
канаш:канаш N ;   ! "совет"





Alphabet
  а ӑ е ё ӗ и о у ӳ ы э ю я б в г д ж з к л м н п р с ҫ т ф х ц ч ш щ й ь ъ
  А Ӑ Е Ё Ӗ И О У Ӳ Ы Э Ю Я Б В Г Д Ж З К Л М Н П Р С Ҫ Т Ф Х Ц Ч Ш Щ Й Ь Ъ 
 %{A%}:а %{A%}:е
 %{Ă%}:ӑ %{Ă%}:ӗ %{Ă%}:0
 %{м%}:м %{м%}:0

;

Sets 

BackVow = ӑ а ы о у я ё ю ;

FrontVow = ӗ э и ӳ ; 

Cns = б в г д ж з к л м н п р с ҫ т ф х ц ч ш щ й ь ъ ; 

Vow = а ӑ е ё ӗ и о у ӳ ы э ю я ;

ArchiCns = %{м%} ;

Rules 

"Remove morpheme boundary"
%>:0 <=> _ ;

"Back vowel harmony for archiphoneme {A}"
%{A%}:а <=> BackVow: [ Cns: | %>: ]+ _ ; 

"No surface {Ă} in plural genitive"
%{Ă%}:0 <=> %{м%}: %>: _ н ;

"Non surface {м} in plural genitive"
%{м%}:0 <=> _ %>: %{Ă%}: н ;

"No surface {Ă} in singular genitive if after a vowel"
%{Ă%}:0 <=> Vow: %>: _ ;

"Back vowel harmony for archiphoneme {Ă}"
%{Ă%}:ӑ <=> BackVow: Cns: %>: _ ;


terminal: resulting forms——————

make
./hfst-lexc chv.lexc -o chv.lexc.hfst
./hfst-lexc: warning: Defaulting to OpenFst tropical type
Root...1 CASES...3 PLURAL...2 N...1 Nouns...
./hfst-twolc chv.twol -o chv.twol.hfst
Reading input from chv.twol.
Writing output to chv.twol.hfst.
Reading alphabet.
Reading sets.
Reading rules and compiling their contexts and centers.
Compiling rules.
Storing rules.
./hfst-compose-intersect -1 chv.lexc.hfst -2 chv.twol.hfst -o chv.gen.hfst
MacBook-Air-orangejuice:bin orangejuice$ ./hfst-fst2strings chv.gen.hfst | grep gen
канаш<n><gen>:канашӑн
канаш<n><pl><gen>:канашсен
пакча<n><gen>:пакчан
пакча<n><pl><gen>:пакчасен
урам<n><gen>:урамӑн
урам<n><pl><gen>:урамсен
хула<n><gen>:хулан
хула<n><pl><gen>:хуласен

