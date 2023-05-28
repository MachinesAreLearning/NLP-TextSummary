import os 
print(os.getcwd())
from pathlib import Path 
import logging 

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name ="textsummarizer"

list_of_files = [
    ".github/workflow/.gitkeep"
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constant/__init__.py",
    "config/config.yaml",
    "paramas.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "README.md",
    "requirements.txt",
    "requirements-dev.txt",
    ".gitignore",
    "setup.py",       
    "reserch/trails.ipynb"
    "test.py"
    ]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.splitext(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory {filedir}")
        
    if (not os.path.exists(filepath) or (os.path.getsize(filepath)==0)):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Created empty file {filepath}")
            
    else:
        logging.info(f"File {filepath} already exists") 
        