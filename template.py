# template.py is for setting up the folder structure
import os
from pathlib import Path
import logging

#Logging basic config and Logging format 
# first initialize the logging.info and then time and message 
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "StockMgmtSystem"

list_of_files = [
    ".github/workflows/.gitkeep", # we need it for CI/CD deployment in YAML file
    f"src/{project_name}/__init__.py", # source folder and init contructor file
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py", 
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb",
    "templates/index.html"


]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    
    else:
        logging.info(f"{filename} is already exists")