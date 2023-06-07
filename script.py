import argparse
import os
import requests
from git import Repo
import subprocess

def clone_repository(repo_url, destination_path):
    Repo.clone_from(repo_url, destination_path)

def get_user_repositories(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    if response.status_code == 200:
        repositories = response.json()
        return repositories
    else:
        return None

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Clonar repositorios desde GitHub')
    parser.add_argument('-u', '--username', help='Nombre de usuario de GitHub')
    parser.add_argument('-n', '--number', type=int, help='Número de repositorios a clonar')

    args = parser.parse_args()

    if args.username:
        username = args.username
        repositories = get_user_repositories(username)
        if repositories is None:
            print('\033[93mEl usuario no existe o no se pudo obtener la lista de repositorios.\033[0m')
            exit()
    else:
        print('\033[93mDebe especificar el nombre del usuario de GitHub.\033[0m')
        exit()

    num_repositories = len(repositories)
    if args.number:
        requested_repositories = args.number
        if requested_repositories <= 0:
            print('\033[93mEl número de repositorios a clonar debe ser mayor que 0.\033[0m')
            exit()
        elif requested_repositories > num_repositories:
            print('\033[93mEl usuario de GitHub tiene menos repositorios de los solicitados.\033[0m')
            print(f'\033[93mEl usuario tiene {num_repositories} repositorio(s).\033[0m')
            exit()
        else:
            num_repositories = requested_repositories

    for repo in repositories[:num_repositories]:
        repo_dir_name = repo['name']
        destination_path = os.path.join('./descargas', repo_dir_name)
        clone_repository(repo['clone_url'], destination_path)
    
    print(f'\033[92m✅ Se han clonado exitosamente {num_repositories} repositorio(s).\033[0m')
    
    subprocess.run(['python', '-m', 'venv', 'gitclonatore'])
    subprocess.run(['source', 'gitclonatore/bin/activate'])
    subprocess.run(['pip', 'install', '-r', 'requirements.txt'])
