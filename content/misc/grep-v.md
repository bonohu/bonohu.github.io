Title: grep -v
Date: 2019-04-19 21:00
Category: shell

`grep` has various options.
I frequently use `-v` option to filter lines without the keyword.

```
grep -v human data.txt
```

where `data.txt` is a bunch of data to be greped.
We can filter *out* lines with keyword *human*. 

Other example is to filter the lines which have a value in the first column.
When the first column is missing, head of the line is '\t' (tab character) in the tab-deliminated text.
We can make use of `grep -v` command below to filter out the lines without the first column.

```
grep -v ^$'\t' data.txt
```

`^` means the head of line, and `$'\t'` means tab character.
It greatly enhances the efficiecy of our study to have a list of lines with required data.




