## Command line git

- status
    - Shows status of the local repository. This status includes:
        - number of local commits that have not been synced with remote (GitHub)
        - list of files in local folder than are NOT being tracked by git
        - list of files in local folder that have changes that need to be committed
    - `git status`
- clone
    - Inserts a copy of the specified repository into a new directory
        - Creates remote-tracking branches for each branch in the repo
    - `git clone <repo>`
- add
    - Stages a file to be added to the current repository
        - The file still need to be committed and synced 
        - Command can be ran multiple times before committing
    - `git add <file>`
- rm
    - Stages a file to be removed from the current repository
        - Same stipulations for add
    - `git rm <file>`
- commit
    - Creates a new commit with all files that were staged to be added or removed
        - Will prompt for a log message for the description of the commit
    - `git commit`
- push
    - Updates the remote repository with all current commits
    - `git push`
- fetch
    - Grabs all data from a remote repository
        - This only bring the data in, it does not change or add data on the current branch
        - `git fetch <repo>`
- merge
    - Takes all the changes from specified branch into the current branch
        - Conflict can occur if both branches have different versions of the same file committed but not pushed
    - `git merge <branch>`
- pull
    - Adds all commits and files from specified repository to current repository
        - Equivalent to `git fetch <fetch_repo>` followed by `git merge <fetch_repo_head>`
    - `git pull <repo>`
- branch
    - List, creates or delete branches in current repository
        - To list branches, just use `git branch` without arguments
        - To create a new branch, use `git branch <branchname>`
        - To delete a branch, use `git branch --d <branchname>`
- checkout
    - Switches to the specified branch 
    - `git branch <branchname>`
- ~~init~~
- ~~remote~~

## git files & folders

- .git folder
- .gitignore file
- ~~.git/hooks~~

## GitHub

- Pull requests
- SSH authentication to repositories
- ~~Actions~~