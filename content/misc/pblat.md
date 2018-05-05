Title: parallelized BLAT
Date: 2018-05-01 17:00
Category: misc

As I had to map assembled reads to the genomic sequence, I used BLAT (the BLAST-like Alignment Tool) for that purpose. BLAT was so fast for landing reads to genomic sequence, but it can be slow if reads are so many. I thought it would be so nice to have multi-threaded BLAT.

And, [there is](https://github.com/icebert/pblat)! Just `git clone https://github.com/icebert/pblat` and then `make`. `pblat` binary file will be generated. It works very well with a command like below.

```
time pblat -threads=4 refgenome.fa query.fa output.psl
```

`-threads=N` is only the difference from original BLAT command where N is the number of threads.

An example execution time for execution with N=12 was below.

> 26353.36s user 88.99s system 798% cpu 55:10.32 total
 
The license to use this code is same as that of BLAT. Commercial users should take care of this.
