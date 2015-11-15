#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Loan Calculator"""


from decimal import Decimal


N = raw_input('What is your name? ')
P = int(raw_input('What is the amount of your principal'
                  '(the amount being borrowed)? $').replace(',', ''))
Y = int(raw_input('For how many years is this loan being borrowed? '))
PRE_Q = 'Are you pre-qualified for this loan? '

ANS_Q = raw_input(PRE_Q)[:1].lower()


if ANS_Q == 'y':
    if 0 < P <= 199999:
        if 0 < Y < 16:
            INTEREST = Decimal('0.0363')
        elif 15 < Y < 21:
            INTEREST = Decimal('0.0404')
        elif 20 < Y < 31:
            INTEREST = Decimal('0.0577')
        else:
            INTEREST = None
    elif P >= 200000 and P <= 999999:
        if 0 < Y < 16:
            INTEREST = Decimal('0.0302')
        elif 15 < Y < 21:
            INTEREST = Decimal('0.0327')
        else:
            INTEREST = Decimal('0.0466')
    elif P > 999999:
        if 0 < Y < 16:
            INTEREST = Decimal('0.0205')
        elif 15 < Y < 21:
            INTEREST = Decimal('0.0262')
    else:
        INTEREST = None
        print 'Error on years of loan being borrowed must be 20yrs or less.'
elif ANS_Q == 'n':
    if 0 < P <= 199999:
        if 0 < Y < 16:
            INTEREST = Decimal('0.0465')
        elif 15 < Y < 21:
            INTEREST = Decimal('0.0498')
        elif 20 < Y < 31:
            INTEREST = Decimal('0.0639')
        else:
            INTEREST = None
            print 'Sorry, not pre-approved.'
    elif P >= 200000 and P <= 999999:
        if 0 < Y < 16:
            INTEREST = Decimal('0.0398')
        elif 15 < Y < 21:
            INTEREST = Decimal('0.0408')
        else:
            INTEREST = None
            print 'Sorry, not pre-approved.'
    else:
        INTEREST = None
        print 'Sorry, not pre-approved.'
else:
    INTEREST = None

if INTEREST is None:
    TOTAL = None

else:
    TOTAL = int(round(P * (1 + INTEREST / 12) ** (12 * Y)))

REPORT = ('Loan Report for: {} \n'
          '------------------------------------------------------------------\n'
          '      Principal:         ${}\n'
          '      Duration:             {}yrs\n'
          '      Pre-qualified?:         {}\n'
          '\n'
          '      Total:             ${}').format(N, P, Y, ANS_Q, TOTAL)

print REPORT
