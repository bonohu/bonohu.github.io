Title: join command option for generating tab-delimited file
Date: 2018-06-15 19:00
Category: shell

When we want to join two files by a same key into one file, we can use `join` command. We can join lines by a first column value of tab-delimited files.

```
join -j 1 file1 file2
```

Indeed, `join` command itself is very useful, default output is not tab-delimited text, but space-delimited text. It is not good for us because most of data are tab-delimited. I just noticed an option for *tab-delimited* output.

```
join -j 1 -t "$(printf '\011')" file1 file2
```

It is required that files to join must be sorted. If not so, error will occur.

`join: file1:7: is not sorted`

Two files must be sorted like this.
```
sort -u file1 > file1s
sort -u file2 > file2s
```
By adding `-u` option, we can delete redundant lines.

Moreover, key for join must be unique. I could not overcome this restriction, and I wrote ad hoc Perl script for that.
