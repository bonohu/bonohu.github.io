Title: Moving to cleanly installed High Sierra
Date: 2018-07-12 12:00
Category: shell

As there was a mechanical trouble in my main machine, MacBookPro, I am moving to new MacBookPro with cleanly installed High Sierra (10.13.6). Below is a log for my future replication...

First of all, default shell was changed with `chsh` command to `/bin/zsh`.

After installing Homebrew, `coreutils` was firstly introduced.

```
% brew install -v coreutils
```

`PATH` was changed  to use commands instroduced.

```
export PATH="/usr/local/opt/coreutils/libexec/gnubin:$PATH"
export MANPATH="/usr/local/opt/coreutils/libexec/gnuman:$MANPATH"
```

Several tools were introduced with brew commands below.

```
% brew install -v gnu-tar â€”with-default-names
% brew install -v grep â€”with-default-names
% brew install -v findutils â€”with-default-names
% brew install -v rsync
% brew install -v pigz
% brew install -v less
% brew install -v pbzip2
% brew install -v byobu
% brew install -v lftp
```

Before using `pip` with `python`, Anaconda(miniconda) was introduced to separately install them.

In order to use `csvlook`, `csvkit` was installed via `pip`.

```
% pip install csvkit
% pip install pelican Markdown
% pip install ghp-import
```

