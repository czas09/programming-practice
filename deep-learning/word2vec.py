from time import time

import numpy as np

from layers import Embedding
from losses import NCELoss
from ..preprocessing.nlp import Vocabulary, tokenize_words
from ..utils.data_structures import DiscreteSampler


class Word2Vec(object):
    def __init__(
        self, 
        context_len=5, 
        min_count=None, 
        skip_gram=False, 
        max_tokens=None, 
        embedding_dim=300, 
        filter_stopwords=True, 
        noise_dist_power=0.75, 
        init="glorot_uniform", 
        num_negative_samples=64, 
        optimizer="SGD(lr=0.1)", 
    ): 
        pass
    
    def _init_params(self):
        pass
    
    @property
    def parameters(self):
        pass
    
    @property
    def hyperparameters(self):
        pass
    
    @property
    def derived_variables(self):
        pass

    @property
    def gradients(self):
        pass
    
    def forward(self, X, targets, retain_derived=True):
        pass
    
    def backward(self):
        pass
    
    def update(self, cur_loss=None):
        pass
    
    def flush_gradients(self):
        pass
    
    def get_embedding(self, word_ids):
        pass
    
    def _build_noise_distributions(self):
        pass
    
    def _train_epoch(self, X, target):
        pass
    
    def minibatch(self, corpus_fps, encoding):
        pass
    
    def fit(
        self, 
        corpus_fps, 
        encoding="utf-8-sig", 
        n_epochs=20, 
        batchsize=120, 
        verbose=True
    ): 
        pass