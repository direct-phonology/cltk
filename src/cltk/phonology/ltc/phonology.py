"""Middle Chinese phonology module. Sources:
- https://en.wikipedia.org/wiki/Middle_Chinese#Phonology
- A Handbook of Old Chinese Phonology by William H. Baxter (1992)

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

# Dentals
t = Consonant(Place.labio_dental, Manner.stop, False, "t")
th = Consonant(Place.labio_dental, Manner.stop, False, "tʰ", aspirated=Aspirated.pos)
d = Consonant(Place.alveolar, Manner.stop, True, "d")
n = Consonant(Place.alveolar, Manner.nasal, False, "n")

# Lateral
l = Consonant(Place.dental, Manner.approximant, False, "l")

# Retroflex stops
tr = Consonant(Place.retroflex, Manner.stop, False, "ʈ")
trh = Consonant(Place.retroflex, Manner.stop, False, "ʈʰ", aspirated=Aspirated.pos)
dr = Consonant(Place.retroflex, Manner.stop, True, "ɖ")
nr = Consonant(Place.retroflex, Manner.nasal, False, "ɳ")

# Dental sibilants
ts = Consonant(Place.dental, Manner.affricate, False, "ts")
tsh = Consonant(Place.dental, Manner.affricate, False, "tsʰ", aspirated=Aspirated.pos)
dz = Consonant(Place.dental, Manner.affricate, True, "dz")
s = Consonant(Place.dental, Manner.fricative, False, "s")
z = Consonant(Place.dental, Manner.fricative, True, "z")

# Retroflex sibilants
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
y = Consonant(Place.palatal, Manner.approximant, False, "y")

# Velars
k = Consonant(Place.velar, Manner.stop, False, "k")
kh = Consonant(Place.velar, Manner.stop, False, "kʰ", aspirated=Aspirated.pos)
g = Consonant(Place.velar, Manner.stop, True, "g")
ng = Consonant(Place.velar, Manner.nasal, False, "ŋ")

# Laryngeals
ʔ = Consonant(Place.glottal, Manner.stop, False, "ʔ")
x = Consonant(Place.glottal, Manner.fricative, False, "x")
h = Consonant(Place.glottal, Manner.fricative, True, "ɣ")

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

## Vowels

i = Vowel(Height.close, Backness.front, Roundedness.neg, Length.long, "i")
ɨ = Vowel(Height.close, Backness.central, Roundedness.neg, Length.long, "ɨ")
u = Vowel(Height.close, Backness.back, Roundedness.neg, Length.long, "u")
e = Vowel(Height.close_mid, Backness.front, Roundedness.neg, Length.long, "e")
o = Vowel(Height.mid, Backness.back, Roundedness.neg, Length.long, "o")
ea = Vowel(Height.open_mid, Backness.front, Roundedness.neg, Length.long, "ɛ")
ae = Vowel(Height.near_open, Backness.front, Roundedness.neg, Length.long, "æ")
a = Vowel(Height.open, Backness.front, Roundedness.neg, Length.long, "a")

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

# Zero coda
ZERO_CODA = set(PositionedPhoneme(a, syllable_final=True), PositionedPhoneme())

# Palatal glide coda

# Labial-velar glide coda

# Labial coda

# Dental coda

# Velar coda

NUCLEI = set()

CODAS = set()


## Finals

FINALS = set()

MIDDLE_CHINESE = INITIALS | FINALS
