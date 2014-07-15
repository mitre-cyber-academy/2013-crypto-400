#!/usr/bin/env python

import sys
import unittest
import transposition

class TestDES(unittest.TestCase):
    def test_cycle_encrypt(self):
        string1 = 'test string'
        string2 = 'Hello World!'
        string3 = 'THE QUICK BROWN FOX'
        string4 = 'L3Pt 0V3R tH3 L4Zy D0G'
        string5 = '23140951230991320459-'
        key1    = 'your king'
        key2    = 'your queen'
        key3    = 'FINE2134'
        key4    = 'Breathe Sl0wly'
        key5    = 'NULL4'
        assert(transposition.cycle_encrypt(key1, string1) == 'xxixtxsxrxegtxsxtn')
        assert(transposition.cycle_encrypt(key2, string2) == 'oxoxrxlxe!xxlxlxWxHd')
        assert(transposition.cycle_encrypt(key3, string3) == 'UWxQOxINxCxxxRxTKFHxOEBX')
        assert(transposition.cycle_encrypt(key4, string4) == '3GtxLLRxtyPZV00Dxx3x34xxHxxx')
        assert(transposition.cycle_encrypt(key5, string5) == '0339x1194x4215x2902-3590x')

    def test_cycle_decrypt(self):
        key1    = 'your king'
        key2    = 'your queen'
        key3    = 'FINE2134'
        key4    = 'Breathe Sl0wly'
        key5    = 'NULL4'
        string1 = 'xxixtxsxrxegtxsxtn'
        string2 = 'oxoxrxlxe!xxlxlxWxHd'
        string3 = 'UWxQOxINxCxxxRxTKFHxOEBX'
        string4 = '3GtxLLRxtyPZV00Dxx3x34xxHxxx'
        string5 = '0339x1194x4215x2902-3590x'
        assert(transposition.cycle_decrypt(key1, string1) == 'testxstringxxxxxxx')
        assert(transposition.cycle_decrypt(key2, string2) == 'HelloxWorld!xxxxxxxx')
        assert(transposition.cycle_decrypt(key3, string3) == 'THExQUICKxBROWNxFOXxxxxx')
        assert(transposition.cycle_decrypt(key4, string4) == 'L3Ptx0V3RxtH3xL4ZyxD0Gxxxxxx')
        assert(transposition.cycle_decrypt(key5, string5) == '23140951230991320459-xxxx')

    def test_method(self):
        message1   = 'the quick brown fox lept over the lazy dog'
        e_message  = 'xcrxxtehadxhuxwoeoxxygtqkoflxrezoeibnxpvtlxx'
        ee_message = 'rhuotloxxxaxxqxepxxdwxkrivxxtxoyoebtcehegfznl'
        dmessage  = 'thexquickxbrownxfoxxleptxoverxthexlazyxdogxx'
        key11      = 'king'
        key12      = 'queen'
        assert(transposition.encrypt(message1, key11, None)    == e_message)
        assert(transposition.decrypt(e_message, key11, None)   == dmessage)
        assert(transposition.encrypt(message1, key11, key12)   == ee_message)
        assert(transposition.decrypt(ee_message, key11, key12) == dmessage)


if __name__ == "__main__":
    unittest.main()
