#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module runs a while loop."""

BASE = ['Seattle Gray', 'Manatee']
ACCENTS = ['Ceramic Glaze', 'Cumulus Nimbus', 'Platinum Mist', 'Spartan Sage']
HIGHLIGHTS = ['Basically White', 'White', 'Off-White', 'Paper White',
              'Bone White', 'Just White', 'Fractal White', 'Not White']

F_Q = raw_input('Which base color, "Seattle Gray" or "Manatee"?: ').lower()

if F_Q == 'manatee':
    BASE = 'Manatee'
    ACCENTS = ACCENTS[2:]
    HIGHLIGHTS = HIGHLIGHTS[5:]
else:
    BASE = 'Seattle Gray'
    ACCENTS = ACCENTS[:1]
    HIGHLIGHTS = HIGHLIGHTS[:4]

S_Q = ('Which accent color, "{}" or "{}"?: ').format(ACCENTS[0],
                                                     ACCENTS[1])

ACCENT = raw_input(S_Q)

for index, color in enumerate(ACCENTS):
    if ACCENT == color:
        start = 2 * (index)
        end = start + 2
        HIGHLIGHTS = HIGHLIGHTS[start:end]
        break

T_Q = 'Which highlight color, "{}" or "{}"?: '.format(HIGHLIGHTS[0],
                                                      HIGHLIGHTS[1])
HIGHLIGHT = raw_input(T_Q)

RETSTR = 'Your selected colors are, {}, {}, and {}.'

print RETSTR.format(BASE, ACCENT, HIGHLIGHT).title()
