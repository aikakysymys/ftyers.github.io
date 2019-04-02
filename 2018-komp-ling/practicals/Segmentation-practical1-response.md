1.
 I used NLTK’s sent_tokenize and MorphAdorner's default sentence splitter.
NLTK’s sent_tokenize uses PunktSentenceTokenizer from the NLTK. tokenize.punkt module. It is based on Neurasl Network analysis.

MorphAdorner's default sentence splitter first desansambles the sentence into tokens with punctuation marks, the assembles them into sentences. Rule based.

2.
 Due to different treatment of ‘:’ before capitalised words, which I consider a sentence divisor and which is frequent in wiki texts, NLTK’s sent_tokenize wins by about 15\%.

3.
 NLTK successfully deals with fractions like ‘3.5’, ‘2.4’ (so does MorphAdorner's default sentence splitter.):


Di oules fasl maikruob-laik objek dem diet bak tu 3.5 Ga (bilian ier uol), jos a fyuu onjrid milian ier yongga dan di ort.
Bai 2.4 Ga, di riesho a stiebl aisotup fi kaaban, aiyan, ahn solfa shuo di akshan a livin tingz pahn inaagyanik minaral ahn sediment ahn di molekyula baiyomaaka dem indikiet fuotosintesis, we shuo se laif pahn ort wehn kaman bai da taim ya.


And also with ‘:’ it works correctly: in numbers it leaves ‘:’ intact:
Aajentiina:
Abuja a di kyapital fi Naijiiria.

But before capitalised tokens it recognises ‘:’ as a splitter:

Di 1907 Kinston oertkwiek we shiekop di kiapital a di ailan a Jumieka wid magnityuud 6.5 pah di muoment magnityuud skiel pah Monde 14 Janiweri, about 3:30 pm luokal taim (20:36 UTC), eh-kansida bai nof raita a di taim fi bi wan a di wol dedlies oertkwiek rikaad ina ischri.



Tokenisation


\section{1}

There are two of maxmatches in the provided .ipynb, one time and the other I found on the Internet. One starts to collect tokens from the longest last word (mine), the other starts with the longest first word. I had a hypothesis that there might be some difference in their performance, but it proved to be wrong: the output is identical, providing the dictionary is the same.

\section{2}

To use it, open your files, readline() them and feed lines to maxmatch line by line. The output will be a list of tokens per each line.

\section{3}. 

In general, it works very well on Japanese. I tried to tokenise sentences with a full dictionary, and there were no mistakes the the output.
 However, if the dictionary does not contain the words needed, tokenisation quality does. Wer.py shows roughly 40\% accuracy on the small chunks I managed to feed it.
 As I can see, provided the words are in the dictionary, all of them are recognised. You can imagine mistakes of the type: a longer and a shorter word in the dict, maxmatch takes the longest one when the shorter one is needed, and makes al least two mistakes: the first word is to long, the one next to it too short. I haven’t encountered such mistakes in the Japanese files I used, maybe because the data was limited.

MorphAdorner's default sentence splitter always keeps ‘:’ within a sentence, even if the next word is not capitalised:

Deso, Abraham enta ina wan kovnant: ina exchienj fi rekanaiz Yaawe az Gad, im uda get bles wid nof pitni ah di lan uda bilangx tu dem.
Aajentiina: Abuja a di kyapital fi Naijiiria.
1907 Kinston oertkwiek: Abalishanizam wehna muuvment fi "h" en di slieb chried ahn "h" imansipiet di sliebdem ina westan Yuurop ahn di Amorkadem.

Concerning fractions: it doesn’t split them by ‘\n’ also, but time expressed with ‘:’ gets a space (’ ’), which is unnecessary:

2010 Kinston anres: Aagianik kimischri: Abaiyojenisis: Aachitecha: Di 1907 Kinston oertkwiek we shiekop di kiapital a di ailan a Jumieka wid magnityuud 6.5 pah di muoment magnityuud skiel pah Monde 14 Janiweri, about 3: 30 pm luokal taim (20: 36 UTC), eh-kansida bai nof raita a di taim fi bi wan a di wol dedlies oertkwiek rikaad ina ischri.


\end
