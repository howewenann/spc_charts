from pathlib import Path
import os

# Data Folders to be recreated
dir_raw = 'data/raw'
dir_processed = 'data/processed'
dir_interim = 'data/interim'
dir_external = 'data/external'

if __name__ == "__main__":

    project_dir = Path(__file__).resolve().parents[2]

    os.makedirs(project_dir / dir_raw)
    os.makedirs(project_dir / dir_processed)
    os.makedirs(project_dir / dir_interim)
    os.makedirs(project_dir / dir_external)