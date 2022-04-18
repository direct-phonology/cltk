"""Middle Chinese phonology module. Sources:
- https://en.wikipedia.org/wiki/Middle_Chinese#Phonology
- A Handbook of Old Chinese Phonology by William H. Baxter (1992)
- Wuyun Pan and Hongming Zhang, "Middle Chinese Phonology and Qieyun," in The Oxford Handbook of Chinese Linguistics, ed. by William S-Y. Wang and Chaofen Sun (Oxford: OUP, 2015), DOI: 10.1093/oxfordhb/9780199856336.013.0016 

"""

## GDR: add back to orthophonology.py:
## labio-velars
## tones

from cltk.phonology.orthophonology import (
    Aspirated,
    Consonant,
    Roundedness,
    Height,
    Backness,
    Length,
    Vowel,
    Place,
    Manner,
    PositionedPhoneme,
)

__author__ = [
    "Nick Budak <budak@stanford.edu>",
    "Gian Duri Rominger <gianr@princeton.edu>",
]

## Consonants

# Labials
p = Consonant(Place.bilabial, Manner.stop, False, "p")
ph = Consonant(Place.bilabial, Manner.stop, False, "pʰ", aspirated=Aspirated.pos)
b = Consonant(Place.bilabial, Manner.stop, True, "b")
m = Consonant(Place.bilabial, Manner.nasal, False, "m")

# Dentals/alveolar stops, nasal, and lateral
t = Consonant(Place.labio_dental, Manner.stop, False, "t")
th = Consonant(Place.labio_dental, Manner.stop, False, "tʰ", aspirated=Aspirated.pos)
d = Consonant(Place.alveolar, Manner.stop, True, "d")
n = Consonant(Place.alveolar, Manner.nasal, False, "n")
l = Consonant(Place.dental, Manner.approximant, False, "l")
## note: Baxter 1992: 49 classifies as dental, lists lateral separately; Pan and Zhang 2015: 85 group dentals ("t", "th", "d", "n") and lateral ("l") together as alveolar stops, nasal, and lateral
## "It is unclear whether these should be regarded as dental or alveolar in articulation ..." (Baxter 1992: 49).

# Retroflex stops
tr = Consonant(Place.retroflex, Manner.stop, False, "ʈ")
trh = Consonant(Place.retroflex, Manner.stop, False, "ʈʰ", aspirated=Aspirated.pos)
dr = Consonant(Place.retroflex, Manner.stop, True, "ɖ")
nr = Consonant(Place.retroflex, Manner.nasal, False, "ɳ")

# dental/alveolar sibilants
ts = Consonant(Place.dental, Manner.affricate, False, "ts")
tsh = Consonant(Place.dental, Manner.affricate, False, "tsʰ", aspirated=Aspirated.pos)
dz = Consonant(Place.dental, Manner.affricate, True, "dz")
s = Consonant(Place.dental, Manner.fricative, False, "s")
z = Consonant(Place.dental, Manner.fricative, True, "z")
## note: Baxter 1992: 51 classifies as dental sibilants; Pan and Zhang 2015: 85 classify as alveolar fricatives and affricates

# Retroflex fricatives and affricates
tsr = Consonant(Place.dental, Manner.affricate, False, "ʈʂ")
tsrh = Consonant(Place.dental, Manner.affricate, False, "ʈʂʰ", aspirated=Aspirated.pos)
dzr = Consonant(Place.dental, Manner.affricate, True, "ɖʐ")
sr = Consonant(Place.dental, Manner.fricative, False, "ʂ")
zr = Consonant(Place.dental, Manner.fricative, True, "ʐ")

# Palatals
tsy = Consonant(Place.palatal, Manner.affricate, False, "tɕ")
tsyh = Consonant(Place.palatal, Manner.affricate, False, "tɕʰ", aspirated=Aspirated.pos)
dzy = Consonant(Place.palatal, Manner.affricate, True, "dʑ")
ny = Consonant(Place.palatal, Manner.nasal, False, "ɲ")
sy = Consonant(Place.palatal, Manner.fricative, False, "ɕ")
zy = Consonant(Place.palatal, Manner.fricative, True, "ʑ")
y = Consonant(Place.palatal, Manner.approximant, False, "j")

# Velars
k = Consonant(Place.velar, Manner.stop, False, "k")
kh = Consonant(Place.velar, Manner.stop, False, "kʰ", aspirated=Aspirated.pos)
g = Consonant(Place.velar, Manner.stop, True, "g")
ng = Consonant(Place.velar, Manner.nasal, True, "ŋ")

# Labiovelars
# based on Baxter 1992: 62
## NOTE: needs to be added back to orthophonology.py
wk = Consonant(Place.labio_velar, Manner.stop, False, "kʷ")
wng = Consonant(Place.labio_velar, Manner.nasal, True, "ŋʷ")

# Laryngeals
ʔ = Consonant(Place.glottal, Manner.stop, False, "ʔ")
x = Consonant(Place.glottal, Manner.fricative, False, "x") ## note: may represent "x" or "h" due to dialect divergences (Baxter 1992: 58); Pan and Zhang 2015: 85 classify as "h"
h = Consonant(Place.glottal, Manner.fricative, True, "ɣ") ## note: may represent "ɣ" or "ɦ" due to dialect divergences (Baxter 1992: 58); Pan and Zhang 2015: 85 classify as "ɦ"

CONSONANTS = set(
    [
        p,
        ph,
        b,
        m,
        t,
        th,
        d,
        n,
        l,
        tr,
        trh,
        dr,
        nr,
        ts,
        tsh,
        dz,
        s,
        z,
        tsr,
        tsrh,
        dzr,
        sr,
        zr,
        tsy,
        tsyh,
        dzy,
        ny,
        sy,
        zy,
        k,
        kh,
        g,
        ng,
        ʔ,
        x,
        h,
    ]
)

## Vowels ###double-check Baxter's vowels against Pan and Zhang 2015: 88-89
i = Vowel(Height.close, Backness.front, Roundedness.neg, Length.long, "i")
ɨ = Vowel(Height.close, Backness.central, Roundedness.neg, Length.long, "ɨ") ##note: Baxter 1992: 61 renders "ɨ" as "+" // this would cause issues
u = Vowel(Height.close, Backness.back, Roundedness.neg, Length.long, "u")
e = Vowel(Height.close_mid, Backness.front, Roundedness.neg, Length.long, "e")
o = Vowel(Height.mid, Backness.back, Roundedness.neg, Length.long, "o")
ea = Vowel(Height.open_mid, Backness.front, Roundedness.neg, Length.long, "ɛ")
ae = Vowel(Height.near_open, Backness.front, Roundedness.neg, Length.long, "æ")
a = Vowel(Height.open, Backness.front, Roundedness.neg, Length.long, "a")

# Gian's notes  4/6/2022; based on Pan and Zhang 2015: 88-89
## NOTE: Length appears not to be distinguished in MC, hence could be omitted here (if necessary for class Vowel, set as either long or short across all vowels)

VOWELS = set(
    [
        i,
        ɨ,
        u,
        e,
        o,
        ea,
        ae,
        a,
    ]
)

## Medials

j = Consonant(Place.palatal, Manner.approximant, False, "j")
w = Consonant(Place.labio_velar, Manner.approximant, True, "w")



## Chongniu 重紐 distinctions
## "The chóngniǔ distinction  has been interpreted by some as a difference in the medial, by others asa difference in the main vowel; [Baxter's] notation is a compromise intended to represent the distinction graphically while leaving its phonological interpretation open" (Baxter 1992: 63).
## "It is quite possible that both the medial solution and the main-vowel solution are correct, but for different dialects or different time periods" (Baxter 1992: 285).
## "...[Baxter's notation] is merely a graphic device and should not be taken as a phonological interpretation" (Baxter 1992: 79).
## For more, compare Baxter 1992: 75-81; 282-286.
## Pan and Zhang 2015: 86-87 adopt the medial solution. 

#Note that Pan and Zhang 2015 represent medials as "ɤ", "ɣ", and "i"
#NOTE: are there any jj/jjw? [there shouldn't be, I think]

## since chongniu-distinction is only a graphic device in Baxter --> same medials as above
# division-IV chongniu (only division-IV uses both "j" and "i") // Type A
#jwi = Consonant(Place.labio_velar, Manner.approximant, True, "w")
#ji = Consonant(Place.palatal, Manner.approximant, False, "j")


##may need BasePhonologicalRule to define medials & vowels acc. to Pan and Zhang 2015: 88-89; see esp. vowel chart and Table 6.4 on p. 88. Baxter's notation marks most of these (but "j" + "a" == "jɑ"). 

##double-check whether to include BasePhonologicalRule to define palatal + "j" cases, like 車 "tsyh" + "jae" == "tsyhae" (in Baxter's notation) [dropped "j" in notation only?]

MEDIALS = set(
    [
        j,
        w,
    ]
)


### Phonemes


## Initials

# Classes
P = set([PositionedPhoneme(i, syllable_initial=True) for i in [p, ph, b, m]])
T = set([PositionedPhoneme(i, syllable_initial=True) for i in [t, th, d, n]])
Tr = set([PositionedPhoneme(i, syllable_initial=True) for i in [tr, trh, dr, nr]])
K = set([PositionedPhoneme(i, syllable_initial=True) for i in [k, kh, g, ng, ʔ, x, h]])
TS = set([PositionedPhoneme(i, syllable_initial=True) for i in [ts, tsh, dz, s, z]])
TSr = set(
    [PositionedPhoneme(i, syllable_initial=True) for i in [tsr, tsrh, dzr, sr, zr]]
)
TSy = set(
    [PositionedPhoneme(i, syllable_initial=True) for i in [tsy, tsyh, dzy, ny, sy, zy]]
)

# Simple
SIMPLE_INITIALS = set(
    [
        PositionedPhoneme(i, syllable_initial=True)
        for i in [
            p,
            ph,
            b,
            m,
            t,
            th,
            d,
            n,
            l,
            ts,
            tsh,
            dz,
            s,
            k,
            kh,
            ng,
            ʔ,
            x,
            h,
        ]
    ]
)

# Complex
COMPLEX_INITIALS = set(
    [
        PositionedPhoneme(i, syllable_initial=True)
        for i in [
            tr,
            trh,
            dr,
            nr,
            z,
            tsr,
            tsrh,
            dzr,
            sr,
            zr,
            tsy,
            tsyh,
            dzy,
            ny,
            sy,
            zy,
            y,
            g,
        ]
    ]
)

INITIALS = SIMPLE_INITIALS | COMPLEX_INITIALS

## Codas
#can consist of Zero coda, ng, m, n, j, or w

# Zero coda
ZERO_CODA = set(PositionedPhoneme(a, syllable_final=True), PositionedPhoneme())

# Palatal glide coda

# Labial-velar glide coda

# Labial coda

# Dental coda

# Velar coda

NUCLEI = VOWELS

CODAS = set()


## Finals
##NOTE: Best to add traditional rhyme categories in notes when listing finals

FINALS = set()

MIDDLE_CHINESE = INITIALS | FINALS

## Tones

"""
Tones are fundamental frequency modulations with phonemic contrast. As suprasegmentals, they denote the use of pitch in languages per syllable to distinguish lexical or grammatical meaning.
For IPA notation, use Chao tone letters; see https://www.internationalphoneticassociation.org/content/ipa-tones-and-word-accents and https://en.wikipedia.org/wiki/Tone_letter#Chao_tone_letters_(IPA) 
"""

## NOTE: need to create new class to implement tones, as underlying CLTK does not contain this feature
#class Tone()


""" Middle Chinese Tones 
MC features four tones;  level (平 píng), rising (上 shǎng), departing (去 qù), and entering (入 rù). 
In Baxter 1992, level (平) is  unmarked; rising (上) marked by final X; departing (去) by H; and entering (入) unmarked but distinguishable from level through final -k/t/p
"Little is known about the true value of the tones in Middle Chinese. ... their tonal values may be reconstructed as ˧33, ˧˥35, ˥˩51, ˧3ʔ, respectively" (Pan and Zhang 2015: 84) [Note that entering tone may end on any eligible final stop consonant, i.e. k/t/p]
- For more, compare https://en.wikipedia.org/wiki/Four_tones_(Middle_Chinese)
"""

##Voice quality (occurring often as a secondary characteristic of tones; examples include creaky voice, breathy voice, etc.)
###NOTE: Does not appear to occur in MC, but could be implemented as new class analogous to Tone for future work on dialects etc.



## Syllable structure

"""
MC syllables, expressed through individual Chinese characters, consist of the following:
initial (I); medial (M); nucleus (N) [which consists of onglide (G) and vowel (V)]; and coda (C) or ending (E); as well as tone (T)
Any syllable can hence be represented as I(M)(G)V(C)T [optional material in parentheses]
"""
