Title: running kallisto
Date: 2018-01-22 18:00

If the transcriptome sequence set is available for an organism, `kallisto` can be used for transcript quantification. The version I used was `0.43.1`.

```
kallisto index -i index transcriptome.fa
kallisto quant -i index -o results/ -t 4 test_1.fq test_2.fq -b 100
```

This command above is for **paired end** sequence. I first tried bzipped(bzip2) FASTQ files for quant, but it failed. FASTQ files must be uncompressed.

For **single end**,  _fragment length_ must be specified for runnging kallisto quant.

IDs for genes (based on IDs in `transcriptome.fa`) might be different from those by alignment-based RNA-seq (from GFF file). ID conversion should be done locally before the comparison of those.
