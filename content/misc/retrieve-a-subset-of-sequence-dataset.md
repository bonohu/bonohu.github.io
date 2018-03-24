Title: Retrieve a subset of sequence dataset
Date: 2018-03-24 15:00
Category: shell

In order to extract a set of sequence from FASTA-formatted file (both in nucleotides and peptides), several commands can be used to do so.
In recent years, I regularly use `blastdbcmd` in NCBI BLAST suite. To run this command, the file must be indexed by `makeblastdb` with the option below. This command is also needed to run the BLAST search, but additional options(`-parse_seqids` and others) are needed for the sequence retrieval.

```
makeblastdb -in hoge.fa -dbtype prot -hash_index -parse_seqids
blastdbcmd -db hoge.fa -entry_batch idlist.txt
```

In this example, `hoge.fa` is a large file containing sequences in FASTA format. `idlist.txt` contains the list of IDs, where only ID of sequence is described in a line (in other words, `\\N` is a delimiter of data).

This is for FASTA file in peptides. If the file in nucleotides, user must change `-dbtype prot` option to `-dbtype nucl`.
