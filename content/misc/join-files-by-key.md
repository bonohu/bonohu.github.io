Title: Join files by key
Date: 2018-03-25 16:00
Category: shell

Joining two files by key in the first column of files can be easily done by using UNIX command below.

```
join -j 1 file1.txt file2.txt
```

This is very useful command, but the output is space-delimited by default.
In order to get the output by tab-delimited, following option for `join` is effective.

```
join -j 1 -t "$(printf '\011')" file1.txt file2.txt
```

Two files must be sorted and non-redundant before running `join` command.
`sort` command with `-u` (unique) option should be applied.

```
sort -u file1.txt > file1s.txt
mv file1s.txt file1.txt
```


