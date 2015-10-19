#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Loan Calculator"""

import decimal


N = raw_input('What is your name? ')
P = int(raw_input('What is the amount of your principal'
                  '(the amount being borrowed)? $').replace(',', ''))
Y = int(raw_input('For how many years is this loan being borrowed? '))
PRE_Q = 'Are you pre-qualified for this loan? '

ANS_Q = raw_input(PRE_Q)[:1].lower()


if ANS_Q == 'y':
    if 0 < Y < 16:
        if P <= (199999):
            INTEREST = 3.63
        elif P >= 200000 and P <= 999999:
            INTEREST = 3.02
        else:
            INTEREST = 2.05
    elif 15 < Y < 21:
        if P <= 199999:
            INTEREST = 4.04
        elif P >= 200000 and P <= 999999:
            INTEREST = 3.27
        else:
            INTEREST = 2.62
    else:
        if P <= 199999:
            INTEREST = 5.77
        elif P >= 200000 and P <= 999999:
            INTEREST = 4.66
        else:
            print 'Error on years of loan being borrowed must be 20yrs or less.'
else:
    if 0 < Y < 16:
        if P <= (199999):
            INTEREST = 4.65
        elif P >= 200000 and P <= 999999:
            INTEREST = 3.98
        else:
            print 'Sorry, not pre-approved.'
    elif 15 < Y < 21:
        if P <= 199999:
            INTEREST = 4.98
        elif P >= 200000 and P <= 999999:
            INTEREST = 4.08
        else:
            print 'Sorry, not pre-approved.'
    else:
        if P <= 199999:
            INTEREST = 6.39
        elif P >= 200000 and P <= 999999:
            print 'Sorry, not pre-approved.'
        else:
            print 'Sorry, not pre-approved.'

R = decimal.Decimal(INTEREST / 100)

TOTAL = int(round(P * ((1 + (decimal.Decimal(R / 12))) ** (12 * Y))))

REPORT = ('Loan Report for: {} \n'
          '------------------------------------------------------------------\n'
          '      Principal:         ${}\n'
          '      Duration:             {}yrs\n'
          '      Pre-qualified?:         {}\n'
          '\n'
          '      Total:             ${}').format(N, P, Y, ANS_Q, TOTAL)

print REPORT