Title: So this is Xmas And what have you done?
Date: 2018-12-21 23:00
Category: DBCLS

I joined [BioHackathon2018](http://2018.biohackathon.org/hackathon) held at Matsue.
I also joined [Common Workflow Language (CWL) Workshop Tokyo 2018](https://github.com/pitagora-galaxy/cwl/wiki/CWL-Workshop-Tokyo-2018) held at Shibuya prior to the hackathon, and learned a little bit about CWL.

I have other tasks (update searchability of All of gene expression (AOE)) to be discussed in the hackathon, but it was a very good chance to implement my data analysis pipeline with CWL for making an index for AOE.
I asked [Ishii-san](https://github.com/manabuishii) about the possibility of CWLization for non-docker workflow, and he said 'It definitely works!'.
So I tried to code it concurrently.

I wrote my code with a great [reference material (in Japanese)](https://github.com/pitagora-galaxy/cwl/wiki/CWL-Start-Guide-JP) which was shown in CWL Workshop Tokyo 2018.

For the reference, my original script to run was like [this](https://github.com/dbcls/AOE/blob/master/00getlistofxRX.sh).

```
perl 00getlistofxRX.pl \
| pigz -c > xRX.json.gz
```

First I tried to make `CommandLineTool` by modifying the sample code for my case.
Because my code requires an additional file which tells the IP address of API server, I failed to do it initially.
With a great help from Ishii-san, I could do it finally ([`perl-gethoge.cwl`](https://github.com/dbcls/AOE/blob/master/perl-gethoge.cwl)).
The files to be used should be described in `inputs:`.

Then, other part (`CommandLineTool`) for the workflow was coded with the name [`pigz.cwl`](https://github.com/dbcls/AOE/blob/master/pigz.cwl) which compresses the output from the other command.

Finally the `Workflow` named [`gethoge-and-pigz.cwl`](https://github.com/dbcls/AOE/blob/master/gethoge-and-pigz.cwl) was coded by looking at the great reference described above.
There was some trials in setting the output files, but it was not so hard compared with the former issue (additional file inclusion).

These `cwl` files were successfully pushed to [GitHub pages](https://github.com/dbcls/AOE) and thus [visualized with the power of public web service](https://view.commonwl.org/workflows/github.com/dbcls/AOE/blob/3ab6db7ca9eb982111e0aa038e03a74183fd06bb/gethoge-and-pigz.cwl), where you can see our workflow in a diagram representation. 
And, my workflow can be run with the command below now!


```
cwltool perl-gethoge.cwl --file 00getlistofxRX.pl  --ipfile IP.txt
```

Of course, `IP.txt` must be specified (not in GitHub repository now, though).

Thanks a lot, Ishii-san and other hackers in CWL community especially for [Michael](https://github.com/mr-c) who gave me a lot of chocolates both at Tokyo and Matsue!


