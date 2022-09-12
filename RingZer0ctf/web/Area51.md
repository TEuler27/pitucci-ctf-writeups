# Area 51

### Author

[Mr.Un1k0d3r](https://twitter.com/mrun1k0d3r)

### Description

Access to this area is restricted using some secure .htaccess
 
## Solution
 
We know that the access is somehow restricted by the .htaccess file. After a few google researches we have found that a possible workaround is to try to use some different requests (e.g. `PUT`). Indeed, copying the headers and sending a PUT requests rewarded us with the flag:

```
AREA 51 The origin of the Area 51 name is unclear? Alien?
FLAG-w4KRr557y626izv567758O52
```