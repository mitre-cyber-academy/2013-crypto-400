#!/usr/bin/env python

'''
I know one of my arguments is 'qey'.  Phonetically it's probably the same as
'key'.  It was that or a number, and I like qey better.

This could also be expanded to accept a list of keys and cycle through the
encryption algorithm for as many keys as are given.
'''

import sys
import argparse
import numpy as np
import re

np.set_printoptions(threshold=np.nan)

def main():
    args = get_args()
    if args.encrypt:
        result = encrypt(args.message,
                        args.key,
                        args.qey,
                        args.showgrid)
    else:
        result = decrypt(args.message,
                        args.key,
                        args.qey,
                        args.showgrid)
    print result

def encrypt(message, key, qey, show=False):
    '''
    Encrypt the message
    :param dictionary: args
    '''
    ciphertext = cycle_encrypt(key, message, show)
    if qey:
        ciphertext = cycle_encrypt(qey, ciphertext, show)
    return ciphertext

def cycle_encrypt(key, message, show=False):
    '''
    Perform the transposition algorithm on the given message
    :param string: key
    :param string: message
    '''
    # Remove all nasties with regular expressions (newlines, whitespace, etc.).
    # I'm leaving in different characters though, because this cipher doesn't
    # depend on set algorithms, just column width.
    ciphertext     = ''
    size           = len(key)
    clean_message  = re.sub('[^a-zA-Z0-9_,.!-]', 'x', message)
    shift_xs       = len(key) - (len(clean_message) % len(key))
    if shift_xs == size:
        shift_xs = 0
    clean_message += shift_xs * 'x'  # Append 'x's to get to good length
    message_length = len(clean_message)
    grid           = np.zeros(((message_length / size), size))  # Create zero grid for enc
    rows           = [clean_message[x:x + size] for x in range(0, message_length, size)]
    order          = [(ord(key[x]), x) for x in range(size)]
    order.sort(key=lambda tup: tup[0])
    for i in range(message_length / size):
        row     = rows[i]
        letters = list(row)
        for j in range(size):
            grid[i, j] = ord(letters[j])
    for item in order:
        column_id = item[1]
        current   = grid[:, column_id]
        text      = ''
        for letter in current:
            text += chr(int(letter))
        ciphertext += text
    if show:
        string_grid = np.chararray(grid.shape)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                string_grid[i, j] = chr(int(grid[i, j]))
        print string_grid
    return ciphertext


def decrypt(message, key, qey, show=False):
    '''
    Decrypt the message
    :param dictionary: args
    '''
    if qey:
        plaintext = cycle_decrypt(key,
                        cycle_decrypt(qey, message, show), show)
    else:
        plaintext = cycle_decrypt(key, message, show)
    return plaintext

def cycle_decrypt(key, message, show=False):
    '''
    Perform the decryption algorithm on the given ciphertext. Note, since this
    is an asymmetric encoding algorithm we need two different operations.
    :param string: key
    :param string; message
    '''
    plaintext      = ''
    size           = len(key)
    message_length = len(message)
    column_length  = message_length / size
    words          = [message[x:x + column_length] for x in range(0, len(message), column_length)]
    grid           = np.zeros(((message_length / size), size))  # Create zero grid
    order          = [(ord(key[x]), x) for x in range(size)]
    order.sort(key=lambda tup: tup[0])
    for i in range(size):
        column = words[i]
        letters = list(column)
        position = order[i][1]
        for j in range(message_length / size):
            grid[j, position] = ord(letters[j])
    for row in grid:
        chunk = ''
        for column in row:
            chunk += chr(int(column))
        plaintext += chunk
    if show:
        string_grid = np.chararray(grid.shape)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                string_grid[i, j] = chr(int(grid[i, j]))
        print string_grid
    return plaintext

def get_args():
    #message_default = 'the quick brown fox lept over the lazy dog'
    parser          = argparse.ArgumentParser()
    parser.add_argument('-k', '--key',
                        type=str, default='king',
                        help='Keyword for cipher')
    parser.add_argument('-q', '--qey',
                        type=str, default=None,
                        help='Second key for double transposition')
    parser.add_argument('-f', '--file',
                        type=str, default=None,
                        help='File to encrypt')
    parser.add_argument('-m', '--message',
                        type=str, default=None,  # message_default,
                        help='Message to encrypt/decrypt')
    parser.add_argument('-e', '--encrypt',
                        action='store_true', help='Encrypt?')
    parser.add_argument('-s', '--showgrid',
                        action='store_true', help='Show Grid?')
    parser.add_argument('-d', '--decrypt',
                        action='store_true', help='Decrypt?')
    args = parser.parse_args()
    if not args.encrypt and not args.decrypt:
        args.encrypt = True
    if args.file:
        args.message = (open(args.file, 'r').read())[:-1]
    return args

if __name__ == "__main__":
    sys.exit(main())
