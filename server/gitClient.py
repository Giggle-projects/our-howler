import os
os.environ["GIT_PYTHON_REFRESH"] = "quiet"
from git import Repo

PATH_OF_GIT_REPO = '/app/.git'

def push(target_username):
    repo = Repo(PATH_OF_GIT_REPO)
    repo.index.add("*")
    repo.index.commit('-m', target_username + ' update score')
    origin = repo.remote(name='origin')
    origin.push()
