Title: uniq -c option
Date: 2018-03-23 17:00
Category: shell

When I want to count the number of redundant words in a file (`hoge.txt`), I have used simple Perl code like this(`count.pl`).

```
#!/usr/bin/perl
while(<>) {
        my($word) = split;
        $num{$word}++;
}
foreach (sort keys %num) {
        print "$_\t$num{$_}\n";
}
```

In order to count the number of redundancy in the list, I often run this script with shell command like below.

```
cat hoge.txt \
| perl count.pl \
| sort -rn
```

This operation can be relaced with a simple shell command like below.

```
uniq -c hoge.txt \
| sort -rn
```

`uniq` has been very familiar command, but I have not realized the option `-c`. 
The UNIX world is very deep indeed!
