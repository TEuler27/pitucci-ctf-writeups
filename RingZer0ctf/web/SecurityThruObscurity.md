# Security thru obscurity!

### Author

[Mr.Un1k0d3r](https://twitter.com/mrun1k0d3r)

### Description

No description
 
## Solution
 
Entering the challenge page we got greeted by a message saying `You don't have admin access`. Looking deeper we found a promising cookie
```
AUTH=Z3Vlc3QsYTM3NWEzZjEzM2RkODAwMiwxNjY0NTUzMDg4LGZhbHNlOjUzOTdlNWIwNGY2NGJkYWY1NjlhYzc1NzgzYjgyZGI5
```
The string is base64 encoded, using cyberchef to decode we got
```
AUTH=guest,a375a3f133dd8002,1664553088,false:5397e5b04f64bdaf569ac75783b82db9
```
The first term is the permission type, the third is a timestamp (probably an expiration date) while the last term after the semicolon is the md5 hash of the rest of the cookie. We constructed a new cookie of the form
```
AUTH=admin,a375a3f133dd8002,1764553088,true:e77618dc62eb6710d09dfd1882e82686
```
and we base64 decoded it to obtain
```
AUTH=YWRtaW4sYTM3NWEzZjEzM2RkODAwMiwxNzY0NTUzMDg4LHRydWU6ZTc3NjE4ZGM2MmViNjcxMGQwOWRmZDE4ODJlODI2ODY=
```
Sending the request again with this new cookie got us the flag: `FLAG-Feg03OSzWhxO03K94108100f`.
