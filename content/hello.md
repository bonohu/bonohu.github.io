Title: Hello, world!
Date: 2018-01-16 12:00
Category: misc

## Test

Hello, world!

Blog in English has just been started.
The website I referred.

- https://qiita.com/akimach/items/dfcac164ac5669a6378e

Shell commands to update contents below.

```
# switched to pelican branch,
git checkout pelican

# and describe contents at this time

# HTML etc generated, and imported to output
pelican content -o output -s pelicanconf.py
ghp-import output -b master

# add, commit & push to pelican branch
git add .
git commit -m "Generate my site."
git push origin pelican

# switched to master branch
git checkout master

# add, commit & push to master branch
git add .
git commit -m "Published."
git push origin master
```
