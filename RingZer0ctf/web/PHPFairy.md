# PHP Fairy

### Author

nic-Lovin

### Description

No description
 
## Solution
 
Opening the challenge page we got a login form asking for a password. The challenge gave us also the source code of the server. Particularly interesting is the line:
```
$pass = md5("admin1674227342");
if ((((((((($_GET['pass'] == $pass)))) && (((($pass !== $_GET['pass']))))) || ((((($pass == $_GET['pass'])))) && ((($_GET['pass'] !== $pass))))))))
```
Indeed, this if condition seems to be always false. Browsing a bit the php documentation we got this interesting information:
```
md5('240610708') == md5('QNKCDZO')

This comparison is true because both md5() hashes start '0e' so PHP type juggling understands these strings to be scientific notation.  By definition, zero raised to any power is zero.
```
Our suspects quickly became valid when we checked and got that
```
md5("admin1674227342") = 0e463854177790028825434984462555
```
Then, simply using as password the string `0e463854177790028825434984462556` got us the flag `FLAG-K7PY48gt02T1yvoO9jzP694FztgR1jIS`.
