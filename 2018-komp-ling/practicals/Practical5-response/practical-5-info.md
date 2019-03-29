Xrenner


1. Preparation:

I have used the existing example and an additional paragraph in conllu.

2. Xrenner text, eng

With some fixes, Xenner srarted and I could test it on the existing exaple file, and I got the coref_new_zealand_new.html file, which is just slightly different ( "flag" is not within one entity, as in the original file).

3. Xrenner rus

I tested the files I prepared (in the rus folder) on two files, the results are "paragraph_new.html" and "pushkin_new.html".

Though the files are in the rus folder here, but let me show you what you can find in them here:


pronouns:

я    1sg
меня    1sg
он    male
Вас    2
Вы    2
Его    male
вас    2
вы    2
его    male
Они    plural
они    plural
им    plural
это    inanim
Это    inanim
то    inanim
себя    obj
себя    Acc


entities:

Пушкин    person    person/male@    0
Тагор    person    person/male    0
друг    person    person/male    0
Рабиндранат Тагор    person    person/male    0
жена    person    person/female    0
письмо    object    object/inanim@    0
Саша    person    person/male    0
Рабиндранат    person    person/male    0
Рабиндранату    person    person/male    0
Александр Нилл    person    person/male    0
организатор    person    person/male    0
школа    organization    organization@    0
ученик    person    person/male    0
Эти слова    abstract    abstract    0
школьник    person    person/male@    0
все    person    person/plural    0
Взрослые    person    person/plural    0
дети    person    person/plural    0
мастерская    place    place/inanim    0
ученики    person    person/male    0
младшие воспитанники    person    person/plural    0
ученики    person    person/plural    0
Саммерхилл    organization@    organization    0
свободная школа    organization    organization@    0
Англия    place    place/inanim@    0
воспитанник    person    person/male@    0
школ    organization    organization/plural    0
им    person    person/plural    0
Александр    person    person/male@    0


open_close_punct:

\"    \"
'    '
(    )
[    ]
{    }
“    ”
‘    ’
``    ''
-    -
--    --
, —    , —
—    —


stops:

при этом
что
При этом
предоставлять возможность
самостоятельно решать
в порядке вещей
заниматься обустройством
любого возраста
к тому, что
тому что
одно и то же время
что-то
с трудом
считать девизом






4. Coreference rules:

Without this rule "Александр Нилл, организатор школы "Саммерхилл" в Англии" are not recognized as an entity, so I edden it:

#propagate entity type across apposition
func=/appos/;child=$1&anytext&anyagree&takefirst;0;propagate
func="appos_pat";child=$1&anytext&anyagree&anyentity&anycardinality&takefirst;0;propagate


These ones didn't prove useful for my files:

#pronouns of same and other explicit speaker
form="pronoun"&text=/^([Яя]|[Мм](еня)|[Вв]ы|[Вв]ас)/&speaker!="";form="pronoun"&text=/(Я|я|меня)/&samespeaker&agree=$1&anytext;100;nopropagate
form="pronoun"&text=/^([Яя]|[Мм](еня))/&speaker!="";form="pronoun"&text=/^([Вв]ы|[Вв]ас)/&!samespeaker&anytext&anyagree;100;nopropagate
form="pronoun"&text=/^([Вв]ы|[Вв]ас)/&speaker!="";form="pronoun"&text=/^([Яя]|[Мм](еня))/&!samespeaker&anytext&anyagree;100;nopropagate
#allow coreference between quoted first person and unquoted third person
form="pronoun"&text=/^([Яя]|[Мм](еня))/&quoted=True;func=/nsubj(pass)?/&text=/[Оо]н/&anytext&anyagree&quoted=False;0;nopropagate

The others are standard, from the udx file.
