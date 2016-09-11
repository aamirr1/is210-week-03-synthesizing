#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains expectations."""


import inquisition


OLDWORD = 'Spanish'
NEWWORD = 'Flemish'
STRING_LENGH = len(OLDWORD)
INDEXED = inquisition.SPANISH.index(OLDWORD)
REMOVE = INDEXED + STRING_LENGH
BEFORE = inquisition.SPANISH[:INDEXED]
AFTER = inquisition.SPANISH[REMOVE:]

FLEMISH = BEFORE + NEWWORD + AFTER
