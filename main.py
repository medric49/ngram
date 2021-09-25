# Author : Medric Sonwa

import os
import numpy as np
import kenlm


def perplexity_values(bin_text, test_text):
    model = kenlm.Model(bin_text)

    perplexities = []
    for text in test_text:
        perplexities.append(model.perplexity(text))

    mean_perplexity = np.mean(perplexities)
    min_perplexity = np.min(perplexities)
    max_perplexity = np.max(perplexities)

    print(f'Min perplexity : {min_perplexity}')
    print(f'Max perplexity : {max_perplexity}')
    print(f'Mean perplexity : {mean_perplexity}')

    del model

    return min_perplexity, max_perplexity, mean_perplexity


if __name__ == '__main__':
    test_text = '1g-word-1m-benchmark-r13output/news.en-00000-of-00100'
    with open(test_text, 'r') as test_text:
        test_text = test_text.read()
    n = 1000
    test_text = test_text.split('\n')[:n]

    root = 'texts'
    files = os.listdir(root)
    files = sorted(files)
    files = [os.path.join(root, file) for file in files]

    result_file = open('result_file.txt', 'w')

    for i, file in enumerate(files):
        os.system(f'lmplz -o 4 -S 80% < {file} > arpas/text_{i+1}.arpa')
        os.system(f'build_binary arpas/text_{i+1}.arpa bins/text_{i+1}.bin')

        arpa_text = f'arpas/text_{i+1}.arpa'
        bin_text = f'bins/text_{i+1}.bin'

        min_v, max_v, mean_v = perplexity_values(bin_text, test_text)

        result_file.write(f'{i+1} {min_v} {max_v} {mean_v}\n')
        os.system(f'rm {arpa_text} {bin_text}')

    result_file.close()




