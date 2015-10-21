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
    if 0 < Y < 16:
        if P <= (199999):
            INTEREST = Decimal('3.63')
        elif P >= 200000 and P <= 999999:
            INTEREST = Decimal('3.02')
        else:
            INTEREST = Decimal('2.05')
    elif 15 < Y < 21:
        if P <= 199999:
            INTEREST = Decimal('4.04')
        elif P >= 200000 and P <= 999999:
            INTEREST = Decimal('3.27')
        else:
            INTEREST = Decimal('2.62')
    else:
        if P <= 199999:
            INTEREST = Decimal('5.77')
        elif P >= 200000 and P <= 999999:
            INTEREST = Decimal('4.66')
        else:
            INTEREST = None
            print 'Error on years of loan being borrowed must be 20yrs or less.'
else:
    if 0 < Y < 16:
        if P <= (199999):
            INTEREST = Decimal('4.65')
        elif P >= 200000 and P <= 999999:
            INTEREST = Decimal('3.98')
        else:
            INTEREST = None
            print 'Sorry, not pre-approved.'
    elif 15 < Y < 21:
        if P <= 199999:
            INTEREST = Decimal('4.98')
        elif P >= 200000 and P <= 999999:
            INTEREST = Decimal('4.08')
        else:
            INTEREST = None
            print 'Sorry, not pre-approved.'
    else:
        if P <= 199999:
            INTEREST = Decimal('6.39')
        elif P >= 200000 and P <= 999999:
            INTEREST = None
            print 'Sorry, not pre-approved.'
        else:
            INTEREST = None
            print 'Sorry, not pre-approved.'

R = (INTEREST / 100)

TOTAL = int(round(P * (1 + R / 12) ** (12 * Y)))

REPORT = ('Loan Report for: {} \n'
          '------------------------------------------------------------------\n'
          '      Principal:         ${}\n'
          '      Duration:             {}yrs\n'
          '      Pre-qualified?:         {}\n'
          '\n'
          '      Total:             ${}').format(N, P, Y, ANS_Q, TOTAL)

print REPORT
