Title: parallelized blat
Date: 2018-05-01 17:00
Category: misc

## BLAT with multi-threads support

As I had to map assembled reads to the genomic sequence, I used BLAT (the BLAST-like Alignment Tool) for that purpose. BLAT was so fast for landing reads to genomic sequence, but it can be slow if reads are so many. I thought it would be so nice to have multi-threaded BLAT.

And, [there is](https://github.com/icebert/pblat)! Just `git clone https://github.com/icebert/pblat` and then `make`. `pblat` binary file will be generated. It works very well!
