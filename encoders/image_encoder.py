from abc import abstractmethod, abstractproperty
from dataclasses import dataclass, field
from typing import Type

import torch
from torch import nn

class BaseImageEncoder(nn.Module):
    @abstractproperty
    def name(self) -> str:
        """
        returns the name of the encoder
        """

    @abstractproperty
    def embedding_dim(self) -> int:
        """
        returns the dimension of the embeddings
        """

    @abstractmethod
    def encode_image(self, input: torch.Tensor) -> torch.Tensor:
        """
        Given a batch of input images, return their encodings
        """

    @abstractmethod
    def get_relevancy(self, embed: torch.Tensor, positive_id: int) -> torch.Tensor:
        """
        Given a batch of embeddings, return the relevancy to the given positive id
        """
