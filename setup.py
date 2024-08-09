import sys
import os
from cx_Freeze import setup, Executable

# Definir o que deve ser incluído na pasta final
arquivos = ['README.md']
# Saida de arquivos
configuracao = Executable(
    script='app.py',
    icon='trator.ico'
)
# Configurar o executável
setup(
    name='Padrão de diretórios para projetos agrícolas',
    version='1.0',
    description='Este programa automatiza a criação de diretórios para projetos agrícolas',
    author='Luiz Zamprogno',
    options={'build_exe':{
        'include_files': arquivos,
        'include_msvcr': True
    }},
    executables=[configuracao]
)
