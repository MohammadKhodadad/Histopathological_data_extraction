import os
import urllib.request
import tarfile

# Define the link and the target directory
LINK = 'http://www.inf.ufpr.br/vri/databases/BreaKHis_v1.tar.gz'
DATA_DIR = './data'
ARCHIVE_NAME = 'BreaKHis_v1.tar.gz'
ARCHIVE_PATH = os.path.join(DATA_DIR, ARCHIVE_NAME)

# Create the data directory if it does not exist
os.makedirs(DATA_DIR, exist_ok=True)

# Download the file

if not os.path.exists(ARCHIVE_NAME):
    print(f"Downloading {LINK}...")
    urllib.request.urlretrieve(LINK, ARCHIVE_PATH)
    print(f"Downloaded archive to {ARCHIVE_PATH}")
else:
    print('{ARCHIVE_PATH} already downloaded.')
# Extract the file
if ARCHIVE_PATH.endswith("tar.gz"):
    print(f"Extracting {ARCHIVE_PATH}...")
    with tarfile.open(ARCHIVE_PATH, "r:gz") as tar:
        tar.extractall(path=DATA_DIR)
    print(f"Extraction complete.")
else:
    print(f"The file {ARCHIVE_PATH} is not a .tar.gz file.")
