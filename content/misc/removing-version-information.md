Title: Removing version information in IDs
Date: 2018-08-31 14:00
Category: shell

Identifiers (IDs) in public databases often contain version information.
For example, `.16` in `ENSG00000100644.16` from Ensembl and `.1` in `NM_001243084.1` from RefSeq.
Such version information can be an obstacle to join entries from different databases.
So, version information should be trimmed before joining.
The file that contains such IDs with version information `id.txt` can be converted by tiny Perl script like

```
% perl -i~ -pe 's/([^\.]+)\./$1/g' id.txt
```

Original file will be renamed to `id.txt~`, and converted file is now named as `id.txt`.