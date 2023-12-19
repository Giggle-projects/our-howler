from git import Repo

PATH_OF_GIT_REPO = '/app/.git'

def push(target_username):
    repo = git.Repo(PATH_OF_GIT_REPO)
    repo.git.add('--all')
    repo.git.commit('-m', target_username + ' update score',
                    author='github-actions[bot]@users.noreply.github.com')
    origin = repo.remote(name='origin')
    origin.push()
