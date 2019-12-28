#!/bin/bash
#
# References
#   https://v1.vuepress.vuejs.org/guide/deploy.html#github-pages
#
pushd ./docs/.vuepress/dist

git init
git add -A
git commit -m "$(date)"
git push -f git@github.com:luncliff/ssf.git master:gh-pages

popd
