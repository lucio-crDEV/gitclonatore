import argparse
import os
import requests
from git import Repo

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
    # Definición de los argumentos de línea de comandos
    parser = argparse.ArgumentParser(description='Clonar repositorios desde GitHub')
    parser.add_argument('username', help='Nombre de usuario de GitHub')
    parser.add_argument('-n', '--number', nargs='?', const=-1, type=int, help='Número de repositorios a clonar o nombre de un repositorio específico')

    args = parser.parse_args()

    repositories = get_user_repositories(args.username)

    if repositories is None:
        print('\033[93mEl usuario no existe o no se pudo obtener la lista de repositorios.\033[0m')
    elif args.number:
        if args.number > 0:
            num_repositories = min(args.number, len(repositories))
            # Clonar los repositorios especificados
            for repo in repositories[:num_repositories]:
                repo_dir_name = repo['name']
                destination_path = os.path.join('./descargas', repo_dir_name)
                clone_repository(repo['clone_url'], destination_path)
            print('\033[92mRepositorios clonados exitosamente.\033[0m')
        elif args.number == -1:
            # Clonar un repositorio específico
            repo_name = args.number
            repo = next((r for r in repositories if r['name'] == repo_name), None)
            if repo is not None:
                repo_dir_name = repo['name']
                destination_path = os.path.join('./descargas', repo_dir_name)
                clone_repository(repo['clone_url'], destination_path)
                print('\033[92mRepositorio clonado exitosamente.\033[0m')
            else:
                print('\033[93mEl repositorio especificado no existe.\033[0m')
        else:
            # Obtener la cantidad de repositorios del usuario
            num_repositories = len(repositories)
            print(f"La cantidad de repositorios del usuario {args.username} es de: {num_repositories}.")
            print('\033[93mEl número de repositorios a clonar debe ser mayor que 0.\033[0m')
    else:
        print('\033[93mDebe especificar un número válido de repositorios a clonar o el nombre de un repositorio específico.\033[0m')
