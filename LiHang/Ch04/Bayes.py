# -*- coding:utf-8 -*-
# Filename: Bayes.py
# Author：hankcs
# Date: 2015/2/6 22:25
from math import log, exp

class LaplaceEstimate(object):
    """
    拉普拉斯平滑处理的贝叶斯估计
    """
 
    def __init__(self):
        self.d = {}  # [词-词频]的map
        self.total = 0.0  # 全部词的词频
        self.none = 1  # 当一个词不存在的时候，它的词频（等于0+1），拉普拉斯平滑，计算条件概率，分子+1
 
    def exists(self, key):
        return key in self.d
 
    def getsum(self):
        return self.total
 
    def get(self, key):
        if not self.exists(key):
            return False, self.none
        return True, self.d[key]
 
    def getprob(self, key):
        """
        估计先验概率
        :param key: 词
        :return: 概率
        """
        return float(self.get(key)[1]) / self.total
 
    def samples(self):
        """
        获取全部样本
        :return:
        """
        return self.d.keys()
 
    def add(self, key, value):
        self.total += value
        if not self.exists(key):
            self.d[key] = 1 #拉普拉斯平滑，计算条件概率，分子+1
            self.total += 1 #拉普拉斯平滑，计算条件概率，分母+1
        self.d[key] += value
        print self.total
        print self.d
 
class Bayes(object):
    def __init__(self):
        self.d = {}  # [标签, 概率] map
        self.total = 0  # 全部词频
 
    def train(self, data):
        for d in data:  # d是[[词链表], 标签]
            c = d[1]  # c是分类
            if c not in self.d:
                self.d[c] = LaplaceEstimate()  # d[c]是概率统计工具
            for word in d[0]:
                self.d[c].add(word, 1)  # 统计词频
        self.total = sum(map(lambda x: self.d[x].getsum(), self.d.keys()))
        print "total:" + str(self.total)
 
    def classify(self, x):
        tmp = {}
        for c in self.d:  # 分类
            tmp[c] = log(self.d[c].getsum()) - log(self.total)  # P(Y=ck)
            for word in x:
                tmp[c] += log(self.d[c].getprob(word))          # P(Xj=xj | Y=ck)
            #print tmp[c]
        ret, prob = 0, 0
        for c in self.d:
            now = 0
            try:
                for otherc in self.d:
                    now += exp(tmp[otherc] - tmp[c])            # 将对数还原为1/p， 在进行条件概率的时候，不是连乘，而是取对数相加，最后逐差取指数，这个过程会发生归一化，得出一个概率出来
                    print tmp[otherc]
                    print tmp[c]
                    print now
                now = 1 / now
                print "now:" + str(now)
            except OverflowError:
                now = 0
            if now > prob:
                ret, prob = c, now 
        return (ret, prob)
 
class Sentiment(object):
    def __init__(self):
        self.classifier = Bayes()
 
    def segment(self, sent):
        words = sent.split(' ')
        return words
 
    def train(self, neg_docs, pos_docs):
        data = []
        for sent in neg_docs:
            data.append([self.segment(sent), u'neg'])
        for sent in pos_docs:
            data.append([self.segment(sent), u'pos'])
        self.classifier.train(data)
 
    def classify(self, sent):
 
        return self.classifier.classify(self.segment(sent))
 
s = Sentiment()
s.train([u'糟糕', u'好 差劲', '悲剧', u'糟糕'], [u'优秀', u'很 好', '牛逼']) # 空格分词
 
print s.classify(u"好 优秀")
