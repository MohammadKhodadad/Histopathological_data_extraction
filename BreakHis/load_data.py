import torch
from torchvision import transforms
from PIL import Image
import os
import glob

import os
import urllib.request
import tarfile


def download_breakhis_data(data_address='./data',unzip=True):   
    # Define the link and the target directory
    LINK = 'http://www.inf.ufpr.br/vri/databases/BreaKHis_v1.tar.gz'
    ARCHIVE_NAME = 'BreaKHis_v1.tar.gz'
    ARCHIVE_PATH = os.path.join(data_address, ARCHIVE_NAME)

    # Create the data directory if it does not exist
    os.makedirs(data_address, exist_ok=True)

    # Download the file

    if not os.path.exists(ARCHIVE_PATH):
        print(f"Downloading {LINK}...")
        urllib.request.urlretrieve(LINK, ARCHIVE_PATH)
        print(f"Downloaded archive to {ARCHIVE_PATH}")
    else:
        print(f'{ARCHIVE_PATH} already downloaded.')
    # Extract the file
    if unzip:
        if ARCHIVE_PATH.endswith("tar.gz"):
            print(f"Extracting {ARCHIVE_PATH}...")
            with tarfile.open(ARCHIVE_PATH, "r:gz") as tar:
                tar.extractall(path=data_address)
            print(f"Extraction complete.")
        else:
            print(f"The file {ARCHIVE_PATH} is not a .tar.gz file.")



def load_breakhis_data(data_address):
    download_breakhis_data(data_address)
    addresses=glob.glob(os.path.join(data_address,'*/*/*/*/*/*/*/40X/*.png'))
    print(f"number of images: {len(addresses)}")
    images=[Image.open(address).convert('RGB') for address in addresses[:10]]
    labels=[address.replace('\\','/').split('/')[4] for address in addresses[:10]]
    split=['train' for _ in range(len(labels))]
    print(images[0].size)
    return images,labels,split

if __name__ == "__main__":
    load_breakhis_data('data')