# Day 7

### Author

[Steven](https://twitter.com/StevenVanAcker)

### Description

 Santa has hidden a secret message on the backside of a jigsaw puzzle that he completed. Sadly, one of his elves dropped the completed puzzle, shuffling all the pieces. Can you verify that it is indeed impossible for the Grinch to recover this message? 
 
 ## Solution
 
 First of all we downloaded the .tar archive and we unpacked it. We saw that tha archive contained 667 pictures of the pieces of a jigsaw puzzle. Running ```exiftool``` on any of the pictures we found that they contain a comment similar to ```Secret data: 'xG'``` so we stripped all of the pieces of the secret data with ```python```. After some time we realized that the pieces need to be ordered by modification date. We put all the secret messages in the order given by modification date and obtained the following string
 
 ```
IC4gICAgICAgLiAgICAgICAgXytfICAgICAgICAuICAgICAgICAgICAgICAgICAgLiAgICAgICAgICAgICAuCiAgICAgICAgICAgICAgICAgIC98XAogICAgICAgLiAgICAgICAgICAgKiAgICAgLiAgICAgICAuICAgICAgICAgICAgLiAgICAgICAgICAgICAgICAgICAuCi4gICAgICAgICAgICAgICAgaS98XGkgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC4gICAgICAgICAgICAgICAuCiAgICAgIC4gICAgLiAgICAgLy8gXFwqICAgICAgICAgICAgICBTYW50YSB3aXNoZXMgZXZlcnlvbmUgYWxsCiAgICAgICAgICAgICAgICAqLyggKVxcICAgICAgLiAgICAgICAgICAgdGhlIGJlc3QgZm9yIDIwMjIgICAgICAgLgogICAgICAgIC4gICAgICBpLyovIFwgXGkgICAgICAgICAgICAgKioqKioqKioqKioqKioqKioqKioqKioqKioqCiAuICAgICAgICAgICAgIC8gLyogKlwrXCAgICAgICAgICAgICBIb3BlZnVsbHkgeW91IGNhbiB1c2UgdGhpczogICAuCiAgICAgIC4gICAgICAgKi8vLyArIFwqXFwqICAgICAgIEFPVFd7U200bGxfcDFlYzNzX21hazNfNF9iMWdfcGljN3VyZX0gICAgICAgLgogICAgICAgICAgICAgaS8gIC9eICBeXCAgXGkgICAgLiAgICAgICAgICAgICAgIC4uLiAuIC4uLgouICAgICAgICAuICAgLyAvKy8gKCleICpcIFwgICAgICAgICAgICAgICAgIC4uLi4uLi4uIC4KICAgICAgICAgICAgaS8vKi9fXi0gLSAgXCpcaSAgICAgICAgICAgICAgLi4uICAuLiAgLi4gICAgICAgICAgICAgICAuCiAgICAuICAgICAgIC8gLy8gKiBeIFwgKiBcIFwgICAgICAgICAgICAgLi4KICAgICAgICAgIGkvIC8qICBeICAqIF4gKyBcIFxpICAgICAgICAgIC4uICAgICBfX18gICAgICAgICAgICBfX19fX19fX18KICAgICAgICAgIC8gLyAvLyAvIHwgXCBcICBcICpcICAgICAgICAgPlVfX19eX1tbX118ICBfX19fX18gIHxffF98X3xffF98CiAgIF9fX18ofClfX19fICAgIHx8fCAgICAgICAgICAgICAgICAgIFtfX19fX19fX19ffD18X19fX19ffD18X3xffF98X3xffD0KICB8X19fX198X19fX198ICAgfHx8ICAgICAgICAgICAgICAgICAgIG9vIE9PT08gb28gICBvbyAgb28gICBvLW8gICBvLW8KIC18ICAgICB8ICAgICB8LS4tfHx8Li0uLS4tLi0uLS4tLi0uLS4tLi0u
 ```
 
 This string is a ```base64``` encoding. Using ```basecrack``` we got the flag
 
 ```
 .       .        _+_        .                  .             .                      
                  /|\                                                                                        
       .           *     .       .            .                   .                                          
.                i/|\i                                   .               .                                   
      .    .     // \\*              Santa wishes everyone all                                               
                */( )\\      .           the best for 2022       .                                           
        .      i/*/ \ \i             ***************************                                             
 .             / /* *\+\             Hopefully you can use this:   .                                         
      .       */// + \*\\*       AOTW{Sm4ll_p1ec3s_mak3_4_b1g_pic7ure}       .                               
             i/  /^  ^\  \i    .               ... . ...                                                     
.        .   / /+/ ()^ *\ \                 ........ .                                                       
            i//*/_^- -  \*\i              ...  ..  ..               .                                        
    .       / // * ^ \ * \ \             ..                                                                  
          i/ /*  ^  * ^ + \ \i          ..     ___            _________                                      
          / / // / | \ \  \ *\         >U___^_[[_]|  ______  |_|_|_|_|_|                                     
   ____(|)____    |||                  [__________|=|______|=|_|_|_|_|_|=                                    
  |_____|_____|   |||                   oo OOOO oo   oo  oo   o-o   o-o                                      
 -|     |     |-.-|||.-.-.-.-.-.-.-.-.-.-. 
 ```
