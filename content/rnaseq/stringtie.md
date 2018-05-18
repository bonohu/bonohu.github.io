Title: StringTie
Date: 2018-05-18 6:00

After the execution of HISAT2, aligned reads can be assembled using [StringTie](http://www.ccb.jhu.edu/software/stringtie/).

> StringTie is a fast and highly efficient assembler of RNA-Seq alignments into potential transcripts.

The pipeline to process data by HISAT2 and StringTie is similar to that by TopHat and Cufflinks. Genome annotation file (GTF) can be used in this stage.

Sorted BAM file (`sample.bam`) is an intial input of the execution of `stringtie`.

```
stringtie sample.bam -p 4 -G hogenome.gtf -o gtf/sample.gtf -A abd/sample.txt
```

Outputs are the genome annotation of transcripts in GTF format (`-o gtf/sample.gtf`) and the abundance of transcripts in tab-deliminated text (`-A abd/sample.txt`).

`-G` option specifies *reference* genome annotation file for working genome assembly (optional). Refer [StringTie manual](http://www.ccb.jhu.edu/software/stringtie/index.shtml?t=manual) for details.
