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

    base_directory = choose_directory()

    if base_directory:
        directories_to_create = [
            'dwg',
            'entregas',
            'dados de campo',
            'entregas'
        ]

    create_directories(base_directory, directories_to_create)

if __name__ == '__main__':
    main()