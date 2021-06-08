from pyhanlp import *
from tests.book.ch03.msr import msr_train
from tests.test_utility import test_data_path
import csv
IOUtil = JClass('com.hankcs.hanlp.corpus.io.IOUtil')
DocVectorModel = JClass('com.hankcs.hanlp.mining.word2vec.DocVectorModel')
Word2VecTrainer = JClass('com.hankcs.hanlp.mining.word2vec.Word2VecTrainer')
WordVectorModel = JClass('com.hankcs.hanlp.mining.word2vec.WordVectorModel')
TRAIN_FILE_NAME = msr_train
MODEL_FILE_NAME = os.path.join(test_data_path(), "word2vec33.txt")
def cut_para(content):
    end_flag = ['\n']
    content_len = len(content)
    sentences = []
    tmp_char = ''
    for idx, char in enumerate(content):
        tmp_char += char
        if (idx + 1) == content_len:
            sentences.append(tmp_char)
            break
        if char in end_flag:
            next_idx = idx + 1
            if not content[next_idx] in end_flag:
                sentences.append(tmp_char)
                tmp_char = ''
    return sentences
def print_nearest(word, model):
    print(
        "\n                                                Word     "
        "Cosine\n------------------------------------------------------------------------")
    for entry in model.nearest(word):
        print("%50s\t\t%f" % (entry.getKey(), entry.getValue()))
def print_nearest_document(document, documents, model):
    print_header(document)
    for entry in model.nearest(document):
        print("%50s\t\t%f" % (documents[entry.getKey()], entry.getValue()))
def print_header(query):
    print(
        "\n%50s          Cosine\n------------------------------------------------------------------------" % (query))
def train_or_load_model():
    if not IOUtil.isFileExisted(MODEL_FILE_NAME):
        if not IOUtil.isFileExisted(TRAIN_FILE_NAME):
            raise RuntimeError("语料不存在，请阅读文档了解语料获取与格式：https://github.com/hankcs/HanLP/wiki/word2vec")
        trainerBuilder = Word2VecTrainer();
         #trainerBuilder = Word2VecTrainer.setLayerSize(300);
        return trainerBuilder.train(TRAIN_FILE_NAME, MODEL_FILE_NAME)
    return load_model()
def load_model():
    return WordVectorModel(MODEL_FILE_NAME)
with open('01-ceshi.txt','r',encoding='utf-8',errors='ignore')as ff:
    content=ff.read()
content_cut=cut_para(content)
#print(content_cut)
input_sentences='滴滴顺风车乘客遇害系列事件'
#if __name__ == '__main__':
wordVectorModel = train_or_load_model()
docVectorModel = DocVectorModel(wordVectorModel)
with open('datadata.txt','w',encoding='utf8')as f:
 for i in range(len(content_cut)):
        ss=docVectorModel.similarity(input_sentences,str(content_cut[i]))
        f.write(str(ss))
        f.write('\n')
     