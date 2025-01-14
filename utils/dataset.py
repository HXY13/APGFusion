import torch.utils.data as Data
import h5py
import numpy as np
import torch

class H5Dataset(Data.Dataset):
    def __init__(self, h5file_path):
        self.h5file_path = h5file_path
        h5f = h5py.File(h5file_path, 'r')
        self.keys = list(h5f['img_patchs'].keys())
        h5f.close()

    def __len__(self):
        return len(self.keys)

    def __getitem__(self, index):
        h5f = h5py.File(self.h5file_path, 'r')
        key = self.keys[index]
        Img = np.array(h5f['img_patchs'][key])
        MRI = np.array(h5f['mria_patchs'][key])
        h5f.close()
        return torch.Tensor(MRI), torch.Tensor(Img)