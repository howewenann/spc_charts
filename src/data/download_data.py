# import the requests library
import requests
from pathlib import Path

url = 'https://bioconnector.github.io/workshops/data/ilinet.csv'
out = "data/raw/raw_data.csv"

if __name__ == "__main__":

    project_dir = Path(__file__).resolve().parents[2]

    # download the file contents in binary format
    r = requests.get(url)
    
    # open method to open a file on your system and write the contents
    with open(project_dir / out, "wb") as code:
        code.write(r.content)


 