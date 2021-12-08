# Day 7

### Author

[Steven](https://twitter.com/StevenVanAcker)

### Description

 Santa has hidden a secret message on the backside of a jigsaw puzzle that he completed. Sadly, one of his elves dropped the completed puzzle, shuffling all the pieces. Can you verify that it is indeed impossible for the Grinch to recover this message? 
 
 ## Solution
 
 First of all we downloaded the .tar archive and we unpacked it. We saw that tha archive contained 667 pictures of the pieces of a jigsaw puzzle. Running ```exiftool``` on any of the pictures we found that they contain a comment similar to ```Secret data: 'xG'``` so we stripped all of the pieces of the secret data with ```python```. After some time we realized that the pieces need to be ordered by modification date. We put all the secret message in the order given by modification date and obtained the following string
 
 ``` ```
 
 This string is a ```base64``` encoding. Using ```basecrack``` we got the flag
 
 ``` ```
