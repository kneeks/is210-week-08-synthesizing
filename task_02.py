#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Alarm Clock"""


QUESTION = 'What day is it? '
QUESTION2 = 'What time is it? '
DAYS = ('Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat')

DAY = raw_input(QUESTION)[:3].lower()
TIME = raw_input(QUESTION2)
if TIME.isdigit():
    if int(TIME[:2]) in range(25) and int(TIME[2:]) in range(60):
        SNOOZE = True if (DAY == 'sat' or DAY == 'sun') or TIME < 600 else False
        if not SNOOZE:
            print 'Beep! Beep! Beep! Beep! Beep!'
