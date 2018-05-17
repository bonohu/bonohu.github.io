Title: HISAT2
Date: 2018-05-17 18:00

HISAT2 is successor of TopHat2. Execution of HISAT2 itself does not require genome annotation file (GTF).

First of all, index for HISAT2 should be constructed unless pre-calculated indexes are available (indexes for popular genomes are pre-calculated and can be downloaded from [HISAT2 website](https://ccb.jhu.edu/software/hisat2/index.shtml) ). When the FASTA-formatted genome is `hogenome.fa` and the name of that index is `hoge`, command to build the index is below.

```
hisat2-build -p 4 hogenome.fa hoge
```

`-p` option specifies the number of max processors to use (in this case, `4` is specified).

One example for shell script to run `hisat2`, named `hisat2.sh`, is like this.

```
#!/bin/sh
x=hoge
base=$1
p=4
hisat2 -p $p -x $x --dta -1 ${base}_1.fq -2 ${base}_2.fq \
| samtools view -@ $p -bS - \
| samtools sort -@ $p -T /tmp/hoge$$ -o ${base}.bam -
```

Because `hisat2` outputs SAM-formatted alignment file by default, output is designed to be converted to BAM file using `samtools view`. Additionally the BAM file is designed to be converted to be sorted using `samtools sort` as the BAM file generated is not sorted, but the file is often needed to be sorted in other program.

Command to run the script is below.

```
time sh hisat2.sh sample
```