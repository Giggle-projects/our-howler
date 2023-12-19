from git import Repo

PATH_OF_GIT_REPO = '.git'

def push(target_username):
    repo = Repo(PATH_OF_GIT_REPO)
    repo.git.add('--all')
    repo.git.commit('-m', target_username + ' update score',
        author="First Last <first.last@company.com>"
    )
    origin = repo.remote(name='origin')
    origin.push()
