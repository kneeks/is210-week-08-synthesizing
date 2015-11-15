#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Alarm Clock"""


DAY = (raw_input('What day is it? ')).lower()[:3]
TIME = int(raw_input('What time is it? '))

SNOOZE = True if DAY == 'sat' or DAY == 'sun' or TIME < 600 else False

if not SNOOZE:
    print 'Beep! ' * 5
