#!/usr/bin/env python

import sys
import transposition
import itertools
import numpy
import numpy as np
import time
import pp

jobServer = pp.Server()
jobs = []

def main():
    ciphertext   = open('./ciphertext.txt', 'r').read()[:-1]
    cipherlength = len(ciphertext)
    for item in get_factors(cipherlength):
        keysize = item[0]
        if keysize <= 10:
            print keysize
            for order in get_order(keysize):
                jobs.append(
                        jobServer.submit(cycle_decrypt,
                                        (keysize, order,
                                            cycle_decrypt(keysize,
                                                          order,
                                                          ciphertext)
                                            ),
                                        (lambda a: a, lambda b: b),
                                        ('numpy', 'sys'))
                        )
    for job in jobs:
        print job()
    jobServer.print_stats()

def get_order(keysize):
    '''
    Gets the order
    '''
    order = [(1, x) for x in range(keysize)]
    return itertools.permutations(order)

def get_factors(number):
    '''
    Get factors of thing
    '''
    for divisor in range(2, number):
        if number % divisor == 0:
            yield (divisor, number / divisor)

def cycle_decrypt(keysize, order, message, show=False):
    '''
    Perform the decryption algorithm on the given ciphertext. Note, since this
    is an asymmetric encoding algorithm we need two different operations.
    :param string: key
    :param string; message
    '''
    plaintext      = ''
    size           = keysize
    message_length = len(message)
    column_length  = message_length / size
    words          = [message[x:x + column_length] for x in range(0, len(message), column_length)]
    grid           = numpy.zeros(((message_length / size), size))  # Create zero grid
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
        string_grid = numpy.chararray(grid.shape)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                string_grid[i, j] = chr(int(grid[i, j]))
        print string_grid
    return plaintext

if __name__ == "__main__":
    sys.exit(main())
