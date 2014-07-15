Name: German Intercepts

Description: The year is 1941. America is entrenched in World War Two, and
you've managed to get your hands on an intercepted message from the Germans.
It's been heavily encrypted, but as America's finest cryptographer of the era,
you feel up to the challenge. You know this cipher is the one the German's call
Übchi, and that the same keyword has been applied twice. You don't know what
the keyword it, however it shouldn't be any longer than 15 characters.

To build: No building necessary. To generate run:
 ./src/gen_ciphertext.sh

How to Solve: This one relies on the ability to research and intimately
understand techniques used for determining algorithms. The previous algorithm's
flag will give away a hint to help the users determine the precise method used,
however after they've determined the algorithm, they still have to bruteforce
the column width in order to determine the final message. To see a good
document on cracking, reference
http://www.nku.edu/~christensen/section%209%20transposition.pdf

What to Distribute: ./src/ciphertext.txt

Flag: MCA-4445532E (Points to DES)
