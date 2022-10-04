# Save the beach

## Solution

We are given a file, `secret`. From the hexdump we see some `IHDR` chunks, and that the first five bytes are replaced by `_`. We try then to insert the first five bytes of a PNG file, and we get a valid `secret.png` file. From that, `zsteg` gives us `INKEMVKBPNAW2ND2GFXDMX3IGBXXOXZUNRGF6YRRORJV63JUOQ3TG4T5$CTFUA$` which is the base32 for the flag, `CTFUA{Am4z1n6_h0ow_4lL_b1tS_m4t73r}`.