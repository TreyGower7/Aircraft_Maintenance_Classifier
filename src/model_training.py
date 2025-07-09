# pip3 install transformers torch torchvision
import torch
import matplotlib.pyplot as plt
import numpy as np
import torch.nn as nn
from transformers import BertModel, BertTokenizer


class BERTClassifier(nn.Module):
    def __init__(self):
        super(BERTClassifier, self).__init__()
    
    def forward():
        """
        Define how the data flows in one forward pass
        """