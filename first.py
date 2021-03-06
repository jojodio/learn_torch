from __future__ import print_function
import torch

x = torch.empty(5,3)
print(x)
y = torch.rand(5,3)
print(y)
z = torch.zeros(5, 3, dtype=torch.long)
print(z)
a = torch.tensor([5.5, 3])
print(a)
print(x.size())
x = torch.rand_like(x, dtype=torch.float)
print(x)
y.add_(x)
print(y)
x = x.view(-1,5)
print(x)
c = torch.randn(1)
print(c)
print(c.item())
xx = x.numpy()
print(xx)
x.add_(1)
print(x)
print(xx)
import numpy as np
d = np.ones(5)
f = torch.from_numpy(d)
np.add(d, 1, out=d)
print(d)
print(f)
if torch.cuda.is_available():
    device = torch.device("cuda")
    y = torch.ones_like(x, device=device)
    x = x.to(device)
    z = x + y
    print(z)
    print(z.to("cpu",torch.double))
