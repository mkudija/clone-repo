import os
import sys
import subprocess
from pathlib import Path

for parent in Path.cwd().parents:
    if str(parent)[-6:]=='GitHub':
        GitHubPath = parent


def clone(repo):
    clone_path = str(GitHubPath)+'/'+repo.split('.git')[0].split('/')[-1]
    clone_name = ''

    if os.path.isdir(clone_path):
        clone_name = repo.split('.git')[0].split('/')[-1]+'_clone'

    if str(sys.platform)=='darwin':
        subprocess.call('pwd', cwd=GitHubPath, shell=True)
    elif str(sys.platform)[:3]=='win':
        subprocess.call('cd', cwd=GitHubPath, shell=True)
    
    print('\n')
    if len(clone_name)>0:
        subprocess.call('git clone {} {}'.format(repo, clone_name), cwd=GitHubPath, shell=True)
        clone_path = str(GitHubPath)+'/'+clone_name
        print('\nDone. Cloned: \n\t{}\n\tto...\n\t{}\n'.format(repo,clone_path))
    else:
        subprocess.call('git clone {}'.format(repo), cwd=GitHubPath, shell=True)
        print('\nDone. Cloned: \n\t{}\n\tto...\n\t{}\n'.format(repo,clone_path))


if __name__=='__main__':

    repo = sys.argv[1]
    clone(repo)