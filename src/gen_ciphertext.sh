#!/bin/bash

#PAD='x'

#cat plaintext.txt | head -n 3 > plain0.txt
#cat plaintext.txt | head -n 6 | tail -n 3 > plain1.txt
#echo $PAD >> plain1.txt
#cat plaintext.txt | head -n 9 | tail -n 3 > plain2.txt
#echo $PAD >> plain2.txt
#cat plaintext.txt | head -n 12 | tail -n 3 > plain3.txt
#cat plaintext.txt | head -n 15 | tail -n 3 > plain4.txt
#
#for FILE in `find . -type f | grep -e "plain[0-9]\.txt" | sort`; do
#    NUMBER=`echo $FILE | cut -c 8`;
#    ./transposition.py -k mitre -q flaghunt -f $FILE > cipher$NUMBER.txt;
#done
#
#rm plain[0-9]\.txt cipher[0-9]\.txt

./transposition.py -k desnext -q desnext -f ./plaintext.txt > ./ciphertext.txt;
