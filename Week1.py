import torch
a=torch.tensor([1,2,3,4])
print(a.dtype)
print(a.type())
print(a.size())
print(a.ndimension())

b=a.view(-1,1)
print(b)
print(b[0])
print(b[0].item())

c=torch.LongTensor([2,3,5,6])
d=torch.tensor([3,5,9,0],dtype=torch.int32)
print(torch.dot(a,c).item())
print(d.tolist())
import numpy as np
import matplotlib.pyplot as plt
#
# x=torch.linspace(0,2*np.pi,100)
# y=torch.sin(x)
# plt.plot(x.numpy(),y.numpy())
# plt.show()
#
# # Practice: Create your tensor, print max and min number, plot the sin result diagram
# x=torch.linspace(0,np.pi/2,25)
# yy=torch.sin(x)
# plt.plot(x.numpy(), yy.numpy())
# y=torch.max(x)
# z=torch.min(x)
a=torch.tensor([1,2,3])
print(a.dtype)


