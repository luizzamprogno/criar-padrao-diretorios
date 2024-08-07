import os
import tkinter as tk
from tkinter import filedialog

def choose_directory():
    root = tk.Tk()
    root.withdraw()

    selected_dir = filedialog.askdirectory(title='Escolha o diretório onde o projeto será salvo')

    return selected_dir

def create_directories(base_dir, directories):

    for directory in directories:
        path = os.path.join(base_dir, directory)
        os.makedirs(path, exist_ok=True)
        print(f'Diretório criado: {path}')

def main():

    while True:

        base_directory = choose_directory()

        if not base_directory:
            print('Nenhum diretório selecionado, encerrando...')
            return

        project_name = input('Digite o nome do projeto: ')
        project_directory = os.path.join(base_directory, project_name)


        if not os.path.exists(project_directory):
            directories_to_create = [
                'dwg',
                'entregas',
                'dados de campo',
                'dados de projeto'
            ]
            create_directories(project_directory, directories_to_create)
            print(f'Projeto criado no diretório: {project_directory}')
            break

        else:
            print(f'O diretório do projeto {base_directory} já existe. Por favor selecione outro diretório')


if __name__ == '__main__':
    main()