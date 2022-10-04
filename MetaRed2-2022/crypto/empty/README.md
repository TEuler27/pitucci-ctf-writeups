# Empty

## Solution

We are given a corrupted PDF file called `empty.pdf`. We know that every valid PDF file must start with bytes `%PDF-`, so we try to XOR them against the first five bytes of the file. What we get is the byte `\x16` repeated five times, so we guess that this is a single byte XOR with key `\x16`. XORing it against all the file we obtain a more reasonable, but still corrupted PDF file. At the end of it we find the flag: `CTFUA{16_8s_a_mag8c_number}`.