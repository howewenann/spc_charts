# import the requests library
import requests
import os
import zipfile
import tarfile
from pathlib import Path

url1 = 'http://terra-ai.sg/datathon3-data.zip'
out1 = "data/raw/dengue.zip"

url2 = 'https://archive.ics.uci.edu/ml/machine-learning-databases/diabetes/diabetes-data.tar.Z'
out2 = "data/raw/diabetes.tar.Z"

# Google drive format
# https://docs.google.com/spreadsheets/d/KEY/export?format=csv&gid=SHEET_ID

url3 = 'https://docs.google.com/spreadsheets/d/1gFTNs_GtnTIyyVWXmsQxwdZpGbyicZM2HJcXvCf4b3k/export?format=csv&gid=0'
out3 = "data/raw/covid19.csv"


def unzip_tar(path):
    outpath = os.path.splitext(path)[0]
    with tarfile.open(path) as tar:
        tar.extractall(outpath)
    return None

def unzip_zip(path):
    outpath = os.path.splitext(path)[0]
    with zipfile.ZipFile(path, 'r') as zipObj:
        zipObj.extractall(outpath)
    return None


def download_data(url, out):

    # download the file contents in binary format
    r = requests.get(url)
    
    # open method to open a file on your system and write the contents
    with open(project_dir / out, "wb") as code:
        code.write(r.content)

    return None


if __name__ == "__main__":

    project_dir = Path(__file__).resolve().parents[2]

    # download dengue data and unzip
    download_data(url1, out1)
    # unzip_zip(out1)

    # download diabetes data and unzip
    download_data(url2, out2)
    # unzip_tar(out2)

    # download covid19
    download_data(url3, out3)

 