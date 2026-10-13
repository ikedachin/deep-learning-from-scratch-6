import os, sys
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
sys.path.append('.')


import regex as re

def pretokenize(text):
    pattern = r"""'(?:[sdmt]|ll|ve|re)| ?\p{L}+| ?\p{N}+| ?[^\s\p{L}\p{N}]+|\s+(?!\S)|\s+"""
    return re.findall(pattern, text)

end_token = "<|endoftext|>"

input_text = open("./codebot/tiny_codes.txt").read()
texts = input_text.split(end_token)
print(texts[:5])
text_list = [pretokenize(text) for text in texts]


for t in text_list:
    print(t)