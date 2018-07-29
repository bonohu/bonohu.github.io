Title: Local reverse complement  
Date: 2018-07-29 18:00
Category: shell

To get reverse complement for specific DNA string is frequently needed in molecular biology.
There were some web interface to do that, but it is not secure.
Calculating reverse complement locally is ideal solution for that issue.

In the search of an example code with practical usefulness in GitHub,
I came across [seqtk](https://github.com/lh3/seqtk), which can do reverse complement locally.

```
% git clone https://github.com/lh3/seqtk
% cd seqtk
% make
% ./seqtk seq -r DNA.fa > revcomp.fa
```

Input file: `DNA.fa`

```
>DNA.fa
gattgtcacggtttaatgggattgtgaaggtgttagcggtttttcttgtaaaactgattt
```

Output file: `revcomp.fa`

```
>DNA.fa
aaatcagttttacaagaaaaaccgctaacaccttcacaatcccattaaaccgtgacaatc
```
