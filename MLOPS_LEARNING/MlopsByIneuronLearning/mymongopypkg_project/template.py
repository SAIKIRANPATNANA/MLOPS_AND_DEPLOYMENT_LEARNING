import os
from pathlib import Path  
import logging

list_of_files = [
    '.github/workflow/.gitkeep',
    '__init__.py',
    'src/__init__.py',
    'src/components/__init__.py',
    'src/components/data_ingestion.py',
    'src/components/data_transformation.py',
    'src/components/model_training.py',
    'src/components/model_evaluation.py',
    'src/utils/__init__.py',
    'src/utils/utils.py',
    'src/exception/__init__.py',
    'src/exception/exception.py',
    'src/logger/__init__.py',
    'src/logger/logging.py',
    'src/pipelines/__init__.py',
    'src/pipelines/training.py',
    'src/pipelines/prediction.py',
    'test/unit/__init__.py',
    'test/integration/__init__.py',
    'experiments/emperiment.py',
    'requirements.txt',
    'requirements_dev.txt',
    'tox.ini',
    'setup.py',
    'setup.cfg',
    'pyproject.toml',
    'init_setup.sh',
    '.gitignore'
]

for filepath in list_of_files:
    dir_name, file_name = os.path.split(filepath)
    if dir_name != '':
        os.makedirs(dir_name,exist_ok = True)
    if not os.path.exists(filepath) or not os.path.getsize(filepath):
        with open(filepath, 'w') as f:
            pass

