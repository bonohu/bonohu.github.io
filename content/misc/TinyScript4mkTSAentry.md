Title: Tiny Perl script for formatting TSA entries
Date: 2018-09-03 12:00
Category: shell

When we submit relatively large entries to DDBJ, we use Mass Submission System (MSS).
We will use MSS for submitting transcriptome sequence assembly (TSA) to DDBJ.

After extracting the list of IDs from header lines of FASTA by command like ```% perl -nle 'print $1 if(/^\>(\S+)/) hoge.fasta > id.txt'```, tiny Perl script called `TSA-SRA-writer.pl` to write formatted text for DDBJ submission might be useful. 



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
        $seqid = $_;
        print "$seqid\tsource\t1..E\torganism\t$organism\n";
        print "\t\t\tmol_type\tmRNA\n";
        print "\t\t\ttissue_type\t$tissue_type\n";
        print "\t\t\tsubmitter_seqid\t$seqid\n";
        print "\t\t\tff_definition\t".'@@[organism]@@ RNA, @@[submitter_seqid]@@'."\n";
}
```