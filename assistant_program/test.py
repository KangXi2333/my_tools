import torch

torch.manual_seed(2022)

tensor = torch.randn(4, 4)
mask = torch.zeros(4,4)
print(tensor)
print(mask)
# build mask
for index, data in enumerate(range(3, -1, -1)):
    mask[index, data: ] = 1
# convert bool
mask = mask.bool()
print(mask)
tensor.masked_fill_(mask, -float('inf'))
print(tensor)
