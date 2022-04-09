"""Middle Chinese phonology module. Sources:
- https://en.wikipedia.org/wiki/Middle_Chinese#Phonology
- A Handbook of Old Chinese Phonology by William H. Baxter (1992)
- Wuyun Pan and Hongming Zhang, "Middle Chinese Phonology and Qieyun," in The Oxford Handbook of Chinese Linguistics, ed. by William S-Y. Wang and Chaofen Sun (Oxford: OUP, 2015), DOI: 10.1093/oxfordhb/9780199856336.013.0016 

"""

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

# Alveolar stops, nasal, and lateral ##double-check Baxter against Pan and Zhang 2015, esp. place of articulation; nasal; lateral
t = Consonant(Place.labio_dental, Manner.stop, False, "t")
th = Consonant(Place.labio_dental, Manner.stop, False, "tʰ", aspirated=Aspirated.pos)
d = Consonant(Place.alveolar, Manner.stop, True, "d")
n = Consonant(Place.alveolar, Manner.nasal, False, "n")
l = Consonant(Place.dental, Manner.approximant, False, "l")

# Retroflex stops
tr = Consonant(Place.retroflex, Manner.stop, False, "ʈ")
trh = Consonant(Place.retroflex, Manner.stop, False, "ʈʰ", aspirated=Aspirated.pos)
dr = Consonant(Place.retroflex, Manner.stop, True, "ɖ")
nr = Consonant(Place.retroflex, Manner.nasal, False, "ɳ")

# Alveolar fricatives and affricatives ##double-check Baxter against Pan and Zhang 2015, esp. place of articulation; terms: sibilant vs. fricatives/affricatices
ts = Consonant(Place.dental, Manner.affricate, False, "ts")
tsh = Consonant(Place.dental, Manner.affricate, False, "tsʰ", aspirated=Aspirated.pos)
dz = Consonant(Place.dental, Manner.affricate, True, "dz")
s = Consonant(Place.dental, Manner.fricative, False, "s")
z = Consonant(Place.dental, Manner.fricative, True, "z")

# Retroflex fricatives and affricatives
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
y = Consonant(Place.palatal, Manner.approximant, False, "j")  #double-check Baxter's ASCII-friendly "y" against Pan and Zhang 2015: 85; IPA as "j" or "y"? ["j" as consonantal appears correct]

# Velars
k = Consonant(Place.velar, Manner.stop, False, "k")
kh = Consonant(Place.velar, Manner.stop, False, "kʰ", aspirated=Aspirated.pos)
g = Consonant(Place.velar, Manner.stop, True, "g")
ng = Consonant(Place.velar, Manner.nasal, False, "ŋ")

# Laryngeals
ʔ = Consonant(Place.glottal, Manner.stop, False, "ʔ")
x = Consonant(Place.glottal, Manner.fricative, False, "x") #double-check Baxter against Pan and Zhang 2015: 85; IPA as "x" or "h"?
h = Consonant(Place.glottal, Manner.fricative, True, "ɣ") #double-check Baxter against Pan and Zhang 2015: 85; IPA as "h" or "ɦ"?

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

#Nick's original proposal
i = Vowel(Height.close, Backness.front, Roundedness.neg, Length.long, "i")
ɨ = Vowel(Height.close, Backness.central, Roundedness.neg, Length.long, "ɨ") #DOUBLE-CHECK: this does not occur in MC? or is this Baxter's "+"?
u = Vowel(Height.close, Backness.back, Roundedness.neg, Length.long, "u")
e = Vowel(Height.close_mid, Backness.front, Roundedness.neg, Length.long, "e")
o = Vowel(Height.mid, Backness.back, Roundedness.neg, Length.long, "o")
ea = Vowel(Height.open_mid, Backness.front, Roundedness.neg, Length.long, "ɛ")
ae = Vowel(Height.near_open, Backness.front, Roundedness.neg, Length.long, "æ")
a = Vowel(Height.open, Backness.front, Roundedness.neg, Length.long, "a")

#Gian's notes  4/6/2022; based on Pan and Zhang 2015: 88-89
##NOTE: Length appears not to be distinguished in MC, hence could be omitted here (if necessary for class Vowel, set as eigher long or short across all vowels)

##may need BasePhonologicalRule to define vowel's acc. to Pan and Zhang 2015: 88-89; see esp. vowel chart and Table 6.4 on p. 88. Baxter's notation marks most of these (but "j" + "a" == "jɑ"). 
##double-check whether to include BasePhonologicalRule to define palatal + "j" cases, like 車 "tsyh" + "jae" == "tsyhae" (in Baxter's notation) [dropped "j" in notation only?]

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
w = Consonant(Place.velar, Manner.approximant, True, "w") #check if there is a way to specify labial-velar approximant
#jwi =
#wi = 
#jw =
#Note that Pan and Zhang 2015 represent medials as "ɤ", "ɣ", and "i"
#NOTE: are there any jj/jjw? [there shouldn't be, I think]

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
