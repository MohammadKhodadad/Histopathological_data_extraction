import torch
from torchvision import transforms
from PIL import Image
import os
import glob

def load_breakhis_data(data_address):
    addresses=glob.glob(os.path.join(data_address,'*/*/*/*/*/*/*/40X/*.png'))
    data=[Image.open(address).convert('RGB') for address in addresses[:10]]
    labels=[address.replace('\\','/').split('/')[4] for address in addresses[:10]]
    split=['train' for _ in range(len(labels))]
    return data,labels,split

if __name__ == "__main__":
    load_breakhis_data('data')