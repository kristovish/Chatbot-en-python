import json

import strig

import random

import nltk

import numpy as np

from nltk.stem import WordNetLemmatizer

import tensorflow as tf

from tensorflow.keras import Sequential

from tensorflow.keras.layers import Dense, Dropout

nltk.download("punkt")

nltk.download("wordnet")


#loading the Dataset: intens.json
data_file = open(data_root = '/intents.json').read()
data = json.loads(data_file)


