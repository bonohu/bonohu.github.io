Title: Running kallisto
Date: 2018-01-22 18:00

If the transcriptome sequence set is available for an organism, [kallisto](https://pachterlab.github.io/kallisto/) can be used for transcript quantification. The `kallisto` version I used was `0.43.1`, which was previously installed using Homebrew by the command like `brew install kallisto`.

```
kallisto index -i index transcriptome.fa
kallisto quant -i index -o results/ -t 4 test_1.fq test_2.fq
```

This command above is for **paired end** sequence. I first tried bzipped(bzip2) FASTQ files for quant, but it failed. FASTQ files must be uncompressed.

For **single end**,  _fragment length_ must be specified by `-l` option for runnging kallisto quant.

```
kallisto quant -i index -o results/ -t 4 --single  -l 100 -s 20 test.fq 
```

IDs for genes (based on IDs in `transcriptome.fa`) might be different from those by alignment-based RNA-seq (from GFF file). ID conversion should be done locally before the comparison of those.

An example for batch script to run kalllisto

```
#!/bin/sh
p=4
ref=kallisto_index
outdir=kallisto_outdir
# should be used in the fq containing directory!
for fq in *.fq.gz;
 do g="${fq%.fq.gz}"
 # for single-end reads. '-l' and '-s' should be modified to fit your data
 time kallisto quant -i $ref -o $outdir/$g -t $p --single  -l 100 -s 20 $fq -b 100
done
```
