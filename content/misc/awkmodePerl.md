Title: Perl in awk mode
Date: 2018-02-05 22:00
Category: shell

When I want to extract data by numeric value in other column, Perl in awk mode might be useful. It is often the case that I forget the option for that in Perl, so I took a note this time.

```
perl -anle  'print "$F[0]\t$F[3]" if ($F[3] > 0)'
```

This oneliner means that split column by tab and extract the 1st and 4th column when value of the 4th column is more than 0. I often forget the option `-anle`.   
