import sys
print('python:', sys.executable)
import tensorflow
print('tensorflow', tensorflow.__version__)
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
print('numpy', np.__version__)
print('import OK')
