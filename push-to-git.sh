make html
scp -r build/html/* docs/.
git add *
git commit -m "new update"
git push origin master