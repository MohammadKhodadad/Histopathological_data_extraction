import os
from datasets import load_dataset



def load_bach_data(data_address):
    os.makedirs(data_address, exist_ok=True)
    data = load_dataset("1aurent/BACH",cache_dir=data_address)
    images=data['train']['image']+data['test']['image']
    labels=data['train']['label']+data['test']['label']
    split=['train' for _ in range(len(data['train']['label']))] + ['test' for _ in range(len(data['test']['label']))]
    print(f"number of images: {len(labels)}")
    print(images[0].size)
    return images,labels,split
    
if __name__ == "__main__":
    load_bach_data('data')