# Vigenere

## Solution
 
We are targeting an alternative vigenere cipher. The description provides us most of the insights we need to solve it:
- the plaintext and the ciphertext are bytes that can go from 0 to 256;
- the key, however, is composed only by alphabetic chars from `a` to `z`;
- the plaintext is not english, but instead a foreign language that must be detected as a part of the flag.

As a classic Vigenere, the first thing to find out is keylength. To do so, we try for every possibility from 2 to 30. For each possible lenght `l`, we split the ciphertext in chunks of length `l` and analize all the characters encrypted with the same key letter at once. 
For each position we guess the best key bit and than see for which length we get a better result. Of course, since we are not dealing with english but instead with an unknown language, we cannot rely on letter frequencies. However, we can see how many characters are sent from each possible key in an alphabetic character, since they must still be the most frequent. Another aspect to take into consideration is that we are told that the cipher is additive, hence for example `a` moves the byte value by one, `b` by two and so on, instead of the usual XOR. To decrypt we must hence subtract.   
With the `guess_keysize()` function, we obtain the best result for `l=11`. The correspondent key is `odiabpcsetf` and the text, which is filled with some random bytes, is detected by Google Translate as Hungarian. The flag is hence `CTFUA{11_odiabpcsetf_Hungarian}`.