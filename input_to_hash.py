#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
a = ((((((((0x3F & (((SymVar_0 - 0xE8D4346) & 0xFFFFFFFFFFFFFFFF) | (((SymVar_0 << (0x39 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) | (SymVar_0 >> (0x7 & 0x3F))))) << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) | (((SymVar_0 << (0x39 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) | (SymVar_0 >> (0x7 & 0x3F)))) >> (((((0xF & (((((SymVar_0 << (0x35 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) | (SymVar_0 >> (0xB & 0x3F))) - ((((((SymVar_0 << (0x39 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) | (SymVar_0 >> (0x7 & 0x3F))) + 0x2D4AF89B) & 0xFFFFFFFFFFFFFFFF) & 0x1D5ABF66)) & 0xFFFFFFFFFFFFFFFF)) | 0x1) & 0xFFFFFFFF) & 0xFF) & 0x3F)) | ((((((0x3F & (((SymVar_0 - 0xE8D4346) & 0xFFFFFFFFFFFFFFFF) | (((SymVar_0 << (0x39 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) | (SymVar_0 >> (0x7 & 0x3F))))) << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) | (((SymVar_0 << (0x39 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) | (SymVar_0 >> (0x7 & 0x3F)))) << (((((0x40 - (0x1 | (0xF & (((((SymVar_0 << (0x35 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) | (SymVar_0 >> (0xB & 0x3F))) - ((((((SymVar_0 << (0x39 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) | (SymVar_0 >> (0x7 & 0x3F))) + 0x2D4AF89B) & 0xFFFFFFFFFFFFFFFF) & 0x1D5ABF66)) & 0xFFFFFFFFFFFFFFFF)))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF)) << ((((0x1 | (0x7 & (((((((((((SymVar_0 << (0x35 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) | (SymVar_0 >> (0xB & 0x3F))) - ((((((SymVar_0 << (0x39 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) | (SymVar_0 >> (0x7 & 0x3F))) + 0x2D4AF89B) & 0xFFFFFFFFFFFFFFFF) & 0x1D5ABF66)) & 0xFFFFFFFFFFFFFFFF) >> ((((0x1 | (0xF & (((((0x3F & (((SymVar_0 - 0xE8D4346) & 0xFFFFFFFFFFFFFFFF) | (((SymVar_0 << (0x39 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) | (SymVar_0 >> (0x7 & 0x3F))))) << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) | (((SymVar_0 << (0x39 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) | (SymVar_0 >> (0x7 & 0x3F)))) >> (0x1 & 0x3F)))) & 0xFFFFFFFF) & 0xFF) & 0x3F)) | (((((((SymVar_0 << (0x35 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) | (SymVar_0 >> (0xB & 0x3F))) - ((((((SymVar_0 << (0x39 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) | (SymVar_0 >> (0x7 & 0x3F))) + 0x2D4AF89B) & 0xFFFFFFFFFFFFFFFF) & 0x1D5ABF66)) & 0xFFFFFFFFFFFFFFFF) << (((((0x40 - (0x1 | (0xF & (((((0x3F & (((SymVar_0 - 0xE8D4346) & 0xFFFFFFFFFFFFFFFF) | (((SymVar_0 << (0x39 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) | (SymVar_0 >> (0x7 & 0x3F))))) << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) | (((SymVar_0 << (0x39 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) | (SymVar_0 >> (0x7 & 0x3F)))) >> (0x1 & 0x3F))))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF)) - ((SymVar_0 - ((0x20453EE3 + (((SymVar_0 << (0x39 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) | (SymVar_0 >> (0x7 & 0x3F)))) & 0xFFFFFFFFFFFFFFFF)) & 0xFFFFFFFFFFFFFFFF)) & 0xFFFFFFFFFFFFFFFF) | ((SymVar_0 - ((0x20453EE3 + (((SymVar_0 << (0x39 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) | (SymVar_0 >> (0x7 & 0x3F)))) & 0xFFFFFFFFFFFFFFFF)) & 0xFFFFFFFFFFFFFFFF)) >> (0x1 & 0x3F)))) & 0xFFFFFFFF) & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF)
print a & 0xffffffffffffffff
