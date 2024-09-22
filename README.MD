What is Git?

- Git is a free and opensource version control system, that allows the developers to track changes in files.
  It allows developers to save snapshots of the code, roll back to previous versions, and work on multiple versions simultaneously using branches.

What is Version Control?

- The management of changes to document, computer programs, large websites, and other collection of information.

What is a Repository?

- Project, or the folder where the project is kept.

What is Github?

- GitHub is a cloud-based hosting service for Git repositories. It enables collaboration between multiple developers on the same project, writing the code for the same project without getting conflicts.

Git Commands:

- git init -> Initializes a empty repository
- git clone <url> -> Bring a repository that is hosted somewhere like Github into a folder on your local machine
- git remote add origin <url> -> Add remote repository
- git add <filename> or . -> Track your files and changes in Git.
- git commit -m "Message" -> Save your files in Git
- git push -u origin -> Upload Git commits to a remote repo, like Github
- git pull -> Download changes from remote repo to your local machine, the opposite of push
- git branch -> Display on which branch we are currently
- git branch <branchname> -> Creates a branch
- git checkout <branchname> -> Switches the branch
- git branch -d <branch-name> -> Deletes a branch
- git push origin --delete <branch-name> -> Deletes a branch from the remote repository

What does git add do, and what is the difference between git commit and git push?

- git add stages your changes, making them ready to be committed. git commit saves the changes in your local repository, while git push uploads your local commits to the remote repository on GitHub.

What is the purpose of creating branches in Git?

- Branches allow you to work on new features or fixes in isolation, preventing changes from affecting the main codebase until they are ready to be merged.

What is the difference between git pull and git clone?

- git clone is used to copy a remote repository to your local machine for the first time. git pull is used to fetch and merge changes from the remote repository into your local repository.

What is a PR?

- A pull request (PR) is a way to propose changes you've made in a branch to the main project. It's also where other team members can review, discuss, and approve or reject the changes.

What is the difference between a Pull Request and a merge?

- A Pull Request is a way to propose and review changes before merging them into the main branch. A merge is the actual combination of two branches into one.

- After successfully merging two branches through a PR, you need to pull the changes to the local repo from the remote repo using git pull.

What is Github Actions?

- GitHub Actions is a tool to automate tasks in your software development lifecycle, such as Continuous Integration (CI) and Continuous Deployment (CD). It allows you to automatically build, test, and deploy your code after every commit.

What is GitHub Actions, and how does it help with CI?

- GitHub Actions automates workflows like testing, building, and deploying code. It helps with Continuous Integration by automatically running tests and other checks every time code is pushed to the repository.

How can someone contribute to your open-source project?

- They can fork the project, make changes in their fork, and submit a pull request to propose their changes.

This is main branch.
This is a change from github.
