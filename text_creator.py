# Author : Medric Sonwa

import os

root = '1g-word-1m-benchmark-r13output/1bshort'
files = os.listdir(root)
files = sorted(files)
files = [os.path.join(root, file) for file in files]

for i in range(len(files)):
    os.system(f'cat {" ".join(files[:i+1] )} > texts/text_{i+1}.txt')

