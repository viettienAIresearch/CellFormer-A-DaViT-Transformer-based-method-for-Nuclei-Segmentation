# -*- coding: utf-8 -*-
"""Data_science_bowl_dataset.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11cV0MjWf5Jc2f9SC5xb64WhUZIeBvxOJ
"""

class DataScienceBowl(Dataset):
  def __init__(self, image_dir, mask_dir, transform=None):
    self.image_dir = image_dir
    self.mask_dir = mask_dir
    self.image = np.load(image_dir)
    self.mask = np.load(mask_dir)
    self.transform = transform

  def __len__(self):
    return self.image.shape[0]

  def __getitem__(self, index):
    image = self.image[index]
    mask = self.mask[index].squeeze()

    if self.transform is not None:
      augmentations = self.transform(image=image, mask=mask)
      image = augmentations["image"]
      mask = augmentations["mask"]
    return image.type(torch.FloatTensor), mask.unsqueeze(0).type(torch.FloatTensor)