'''
Extract model information into a txt file
Usage: python model_to_txt.py input.model output.txt
'''

from gensim.models import word2vec
import sys

input_f  = sys.argv[1]
output_f = sys.argv[2]

model = word2vec.Word2Vec.load(input_f)
model.wv.save_word2vec_format(output_f, binary=False)
