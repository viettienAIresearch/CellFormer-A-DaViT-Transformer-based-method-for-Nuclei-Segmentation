# -*- coding: utf-8 -*-
"""conv2d_upsample_mlp.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11cV0MjWf5Jc2f9SC5xb64WhUZIeBvxOJ
"""

class BasicConv2d(nn.Module):
    def __init__(self, in_planes, out_planes, kernel_size, stride=1, padding=0, dilation=1):
        super(BasicConv2d, self).__init__()

        self.conv = nn.Conv2d(in_planes, out_planes,
                              kernel_size=kernel_size, stride=stride,
                              padding=padding, dilation=dilation, bias=False)
        self.bn = nn.BatchNorm2d(out_planes)
        self.relu = nn.ReLU(inplace=True)

    def forward(self, x):
        x = self.conv(x)
        x = self.bn(x)
        x = self.relu(x)
        return x

def Upsample(x, size, align_corners = False):
    """
    Wrapper Around the Upsample Call
    """
    return nn.functional.interpolate(x, size=size, mode='bilinear', align_corners=align_corners)

class MLP(nn.Module):
    """
    Linear Embedding
    """
    def __init__(self, input_dim=2048, embed_dim=768):
        super().__init__()
        self.proj = nn.Linear(input_dim, embed_dim)
        self.act=nn.GELU()
        self.proj_re=nn.Linear(embed_dim,input_dim)
    def forward(self, x):
        B,C,H,W=x.shape
        x = x.flatten(2).transpose(1, 2)
        x = self.proj(x)
        x=self.act(x)
        x=self.proj_re(x)
        x=x.reshape(B,C,H,W)
        return x