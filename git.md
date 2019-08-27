# git

```
################################################################################
# Git reset
git reset --hard HEAD~1

# OR
git reset --soft HEAD~1
git reset --hard

################################################################################
# git clean
git clean -fxd

################################################################################
# See which tag are you in
git describe --tags

################################################################################
# git log
git log -1 HEAD
git log --graph --pretty=format:'%C(yellow)%h %Creset%ad %C(cyan)%an%Cgreen%d %Creset%s' -5
git log -n 5

################################################################################
# Preparing release with bumpversion
git reset --hard
git add ReleaseNotes.md
bumpversion --allow-dirty --commit --tag release
bumpversion --commit patch

git push && git push --tags

################################################################################
# git clone
git clone --depth 1 <url>

################################################################################
# Rebase from a previous (merged) branch to master

git rebase --onto master base_update branch_name

################################################################################
# SourceTree performance - Fix slow speed

git config --global core.preloadindex true
git config --global core.fscache true

################################################################################
# Git: http://stackoverflow.com/questions/9683279/make-the-current-commit-the-only-initial-commit-in-a-git-repository

# Step 1: remove all history
rm -rf .git

# Step 2: reconstruct the Git repo with only the current content
git init
git add .
git commit -m "Initial commit"

# Step 3: push to GitHub.
git remote add origin <github-uri>
git push -u --force origin master

################################################################################
# git submodule

git clone --recursive

# pull but only the google_fibre git repo
git pull

# Need to pull also the submodules the first time
git submodule update --init --recursive

# Update
git submodule foreach git pull
git submodule foreach git pull origin master

# Git: Add submodule
cd repo1_folder
git submodule add https://bitbucket.org/account/repo2.git
git status
git add .
git commit -m "Added submodule"
git push

# Git: Remove submodule
git submodule deinit repo2
git rm repo2
rm -rf .git/modules/repo2
git status
git commit -m "Removed submodule"
git push