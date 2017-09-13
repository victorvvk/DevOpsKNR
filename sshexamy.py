#/usr/bin

git push --force-with-lease origin-push

will fail unless you manually run git fetch origin-push. This method is of course entirely defeated by something that runs git fetch --all  in that case you'd need to either ' disable it or do something more tedious like

git fetch 
git tag base master
git rebase -i master
git push --force-with-lease=master:base master:master
