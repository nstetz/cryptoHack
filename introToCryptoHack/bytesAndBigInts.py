#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 15:54:33 2021

@author: dantes
"""

from Crypto.Util.number import long_to_bytes

longInt = 11515195063862318899931685488813747395775516287289682636499965282714637259206269

result = long_to_bytes(longInt)

print(result)