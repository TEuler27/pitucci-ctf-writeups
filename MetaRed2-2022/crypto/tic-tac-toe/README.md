# Tic Tac Toe

## Solution

We are given a string:  
`CT0N_2TR2_T4F411HFUNT243A21NT}{P0T_`
Since it starts with `C` and the `{` is at the end, it is probably a transposition. The length of 6 is suggested in the description of the challenge, but can easily be guessed by manually splitting the string. We get
```
CT0N_2
TR2_T4
F411HF
UNT243
A21NT}
{P0T_
```
which read vertically gives `CTFUA{TR4N2P021T10N_12NT_TH4T_24F3}`.