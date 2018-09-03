Title: Tiny Perl script for formatting TSA entries
Date: 2018-09-03 12:00
Category: shell

When we submit relatively large entries to DDBJ, we use [Mass Submission System (MSS)](https://www.ddbj.nig.ac.jp/ddbj/mss-e.html).
We will use MSS for submitting [transcriptome sequence assembly (TSA)](https://www.ddbj.nig.ac.jp/ddbj/tsa-e.html) to DDBJ.

After extracting the list of IDs from header lines of FASTA by command like 

```% perl -nle 'print $1 if(/^\>(\S+)/) hoge.fasta > id.txt'```

tiny Perl script called `TSA-SRA-writer.pl` to write formatted text for DDBJ submission might be useful. 
User should note that only the latter (but huge) body of the formatted text is described by this script, and user needed to add the header part of that.

```
#!/usr/bin/env perl
# TSA-SRA-writer.pl
# STDIN: list of IDs

# organism name
my $organism     = "Hoge hoge";
# tissue name
my $tissue_type  = "fuga";

while(<STDIN>) {
        chomp;
        my $seqid = $_;
        print "$seqid\tsource\t1..E\torganism\t$organism\n";
        print "\t\t\tmol_type\tmRNA\n";
        print "\t\t\ttissue_type\t$tissue_type\n";
        print "\t\t\tsubmitter_seqid\t$seqid\n";
        print "\t\t\tff_definition\t".'@@[organism]@@ RNA, @@[submitter_seqid]@@'."\n";
}
```