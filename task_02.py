#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Alarm Clock"""


QUESTION = 'What day is it? '
QUESTION2 = 'What time is it? '
DAYS = ('Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat')

DAY = raw_input(QUESTION)[:3].lower()
TIME = raw_input(QUESTION2)
HR = int(TIME[:2])
MIN = int(TIME[2:])

if (0 <= HR <= 24) and (0 <= MIN < 60):
    SNOOZE = True if (DAY == 'sat' or DAY == 'sun') or TIME < 600 else False
    if not SNOOZE:
        SNOOZE = True
        print 'Beep! Beep! Beep! Beep! Beep!'
else:
    print 'Error, re-evaluate.'
