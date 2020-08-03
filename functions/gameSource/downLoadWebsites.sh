#!/bin/bash

## Command modified from: https://unix.stackexchange.com/questions/281991/pass-a-list-of-urls-contained-in-a-file-to-curl
## Documention of curl : https://curl.haxx.se/docs/manpage.html
xargs <listOfGames.txt -I{} curl  -# -O {}


