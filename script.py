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
    parser.add_argument('username', help='Nombre de usuario de GitHub')
    parser.add_argument('-n', '--number', type=int, help='Número de repositorios a clonar')
    parser.add_argument('-c', '--cantidad', type=int, help='Cantidad de repositorios')

    args = parser.parse_args()

    if args.cantidad and args.cantidad >= 1 and args.cantidad <= 4:
        args.number = args.cantidad

    if args.number:
        if args.number >= 1 and args.number <= 4:
            repositories = get_user_repositories(args.username)
            if repositories is None:
                print('\033[93mEl usuario no existe o no se pudo obtener la lista de repositorios.\033[0m')
            else:
                num_repositories = min(args.number, len(repositories))
                for repo in repositories[:num_repositories]:
                    repo_dir_name = repo['name']
                    destination_path = os.path.join('./descargas', repo_dir_name)
                    clone_repository(repo['clone_url'], destination_path)
                print('\033[92m✅ Repositorios clonados exitosamente.\033[0m')
        else:
            print('\033[93mEl número de repositorios a clonar debe estar entre 1 y 4.\033[0m')
    else:
        print('\033[93mDebe especificar el número de repositorios a clonar usando el parámetro -n.\033[0m')

    # Crear entorno virtual
    subprocess.run(["python", "-m", "venv", "gitclonatore"], check=True)

    # Activar entorno virtual
    activate_script = os.path.join("gitclonatore", "bin", "activate")
    subprocess.run(["source", activate_script], shell=True, check=True)

    # Instalar dependencias desde requirements.txt
    subprocess.run(["pip", "install", "-r", "requirements.txt"], check=True)
