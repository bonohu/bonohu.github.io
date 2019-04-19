Title: fgrep
Date: 2019-04-18 21:00
Category: shell

It turned out that the command I regularly use to search a bunch of data is not known to others.

I frequently use `fgrep` to grep against a list of keywords (i.e. IDs).

```
fgrep -f keywords.txt data.txt
```

where `keywords.txt` contains a list of keywords ('one keyword in one line' manner), and `data.txt` is a bunch of data to be greped.

In fact, we can make use of `grep -f` command instead of `fgrep -f`. 
I am not sure about the difference currently.





