# authoritarian-legislator-responsiveness main code

This repository contains the main code for the paper Legislator Responsiveness in China’s National People’s Congress by Naiyu Jiang. These python scripts have been written to find cosine similarity between any two text documents (/short sentences) using word2vec.

## 1. Train Word Vectors：Word2vec

I use Word2vec to train word vectors. Word2vec is a method to efficiently create word embeddings, which are vector representations of a particular word. Word2Vec represents words into vector based on several features they have such as windows size and vector dimensions. Similar words tend to have the same vector values and are grouped in the same block. Word2Vec can capture the similarity value between words from the training of a large corpus. The
resulting similarity value is obtained from the word vector value than calculated using the Cosine Similarity equation.
The similarity value produced by Word2Vec ranges from -1 to 1 as the highest similarity value. For details on word2vec, see [this link](https://code.google.com/archive/p/word2vec/).

## 2. The Applications of Word Vectors in This Project

In this project, I want to find the similarity between sensitive news topics and bill titles. First, I create a model using Word2Vec for the exhaustive list of sensitive news topics. Then, using this model I can create feature vectors for text documents. The script finds and prints out the cosine similarity for each of the input bill titles. Finally, I set the correlation creteria to determine whether a bill title is similar to a sensitive news topic. For scores greater than 0.8, I will set the bills automatically as similar; and for scores greater than 0.5 and less than 0.8, I will check the threshold for the topic manually. 

![alt text](https://github.com/NaiyuJ/authoritarian-responsiveness/blob/main/criteria.png)

Here is an example of my similarity measuring process:

![alt text](https://github.com/NaiyuJ/authoritarian-responsiveness/blob/main/example.png)

## References & Further reading
1. [Train word2vec in Chinese](https://github.com/hankcs/HanLP/wiki/word2vec)
2. [Calculating Document Similarities using BERT, word2vec, and other models](https://towardsdatascience.com/calculating-document-similarities-using-bert-and-other-models-b2c1a29c9630)
3. [Word2vec embeddings](https://radimrehurek.com/gensim/models/word2vec.html)




