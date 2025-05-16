"""
GIT - control changes across multiple people in working on a robust project
one repository -> no conflicts
If you have Windows 7 then you have to look for the last supported version by searching for 'git versions for windows 7'
GIT is local repository, Git Hub is remote repository
VCS - Version Control System
90% of the times GIT will do the magic, but sometimes it will throw an error - there is a merge conflict, and will ask us
to fix the problem and then push the code
Git Hub - central repository - The place where you post a project/repository and a team mate can find and download it
Automation can be: web, mobile, api, unit testing

You have some code in a folder
git init - Initialise it as a Git repository
git config --global user.name 'Mihai'
git config --global user.email 'neagumihai54321@gmail.com'
First level of commit - stash/staging, final level of commit -commit
First add code to stash/staging, then to commit and finally to Github
git add * - add everything to the stash/staging
git status - command to see what files are added to the stash
git commit -m "first commit" - add from stage with a message
git remote add origin <server> - connect your local repository to a remote server, add the server to be able
to push to it
git remote set-url origin https://<token>@github.com/<user>/<repo>
git push origin master - push the code files into your remote repository

git clone origin main - extract code from remote repo into local repo for the first time
git remote set-url origin https://your-token@github.com/username/repository.git
git config --global credential.helper store
git pull origin main - check for updates

git checkout -b develop - create and access a new branch called 'develop'
git branch - see the current branch you are working in
git commit -a -m "your message" add changes
git push origin develop - push the new branch on the remote repo
git pull origin develop - pull from another user the new branch
git checkout develop - switch to 'develop' branch from 'main'
git branch -d develop - delete 'develop' branch



git config --global credential.helper store - Git will store your credentials and won't prompt for a username/password
git config --global init.defaultBranch main - this will replace 'Master' with 'main'
git help config - Git will help with config, it's going to lunch the browser
rm -rf .git - removes recursive, forced the git directory
.gitignore - input in this file the files you want GIT to exclude
"""