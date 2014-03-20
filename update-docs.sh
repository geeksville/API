
exit
FIXME make sure we wont run if git dir not clean or if we have faults
cd docs
make html
cp -a _build/html /tmp/autodocs
cd ..
git checkout gh_pages
cp -a /tmp/autodocs/* .
find . | xargs git add
git commit -c "Update docs"
git push
git checkout master

