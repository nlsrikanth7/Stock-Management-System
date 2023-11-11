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
    "requirements.txt",
    "setup.py",
    "main.py",
    "templates/index.html",
    "create_mysql_database.py"

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