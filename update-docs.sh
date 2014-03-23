#!/bin/bash

set -e

echo Switching to doc tree
cd docs
make html
rm -r /tmp/autodocs
cp -a _build/html /tmp/autodocs
cd ..
git checkout gh-pages
cp -a /tmp/autodocs/* .
find . | xargs git add
git commit -m "Update docs"
git push
git checkout -f master
