import numpy as np
import matplotlib.pyplot as plt

# 随即生成样本数据，二分类问题，每个类别5000个样本
np.random.seed(12)
num_observations = 5000

x1 = np.random.multivariate_normal([0, 0], [[1, .75], [.75, 1]], num_observations)
# print(x1.shape)
# print(x1)

x2 = np.random.multivariate_normal([1, 4], [[1, .75], [.75, 1]], num_observations)
# print(x2.shape)
# print(x2)

X = np.vstack((x1, x2)).astype(np.float32)
# print(X.shape)
# print(X)

y = np.hstack((np.zeros(num_observations), np.ones(num_observations)))
# print(y.shape)
# print(y)

# 数据的可视化
plt.figure(figsize=(12, 8))
plt.scatter(X[:, 0], X[:, 1], c=y, alpha=.4)
# plt.show()


# 实现 sigmoid 函数
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


# 计算 log likelihood
def log_likelihood(X, y, w, b):
    """
    针对所有样本，计算（负的） log likelihood, 也叫做 cross-entropy loss
    这个值越小越好
    X: 训练数据（特征向量）， N * D
    y: 训练数据（标签），一维向量，长度 D
    w: 模型的参数，一维向量，长度 D
    b: 模型的偏移量，标量
    """

    # 按照标签来提取正样本和负样本的下标
    pos, neg = np.where(y == 1), np.where(y == 0)

    # 正样本计算loss
    pos_sum = np.sum(np.log(sigmoid(np.dot(X[pos], w) + b)))
    # 负样本计算loss
    neg_sum = np.sum(np.log(1 - sigmoid(np.dot(X[neg], w) + b)))

    return -(pos_sum + neg_sum)


def logistic_regression(X, y, num_steps, learning_rate):
    """
    基于梯度下降法实现逻辑回归模型
    X: 训练数据（特征向量）, N * D
    y: 训练数据（标签）, 一味的向量，长度为 D
    num_steps: 梯度下降法的迭代次数
    learning_rate: 步长
    """
    w, b = np.zeros(X.shape[1]), 0
    for step in range(num_steps):
        error = sigmoid(np.dot(X, w) + b) - y

        # 对w, b 的梯度计算
        grad_w = np.matmul(X.T, error)
        grad_b = np.sum(error)

        # 对w, b 的梯度更新
        w = w - learning_rate * grad_w
        b = b - learning_rate * grad_b

        # 每隔一段时间，计算 log likelihood, 看看有没有变化
        # 正常情况下，它会慢慢变小， 最后收敛
        if step % 10000 == 0:
            print(log_likelihood(X, y, w, b))

    return w, b


w, b = logistic_regression(X, y, num_steps=100000, learning_rate=5e-5)
print("(自己写的)逻辑回归的参数w, b分别为: ", w, b)

# 调用 sklearn 模块，对比结果
from sklearn.linear_model import LogisticRegression

# C 设置一个很大的值，意味着不想加入正则项
clf = LogisticRegression(fit_intercept=True, C=1e15)
clf.fit(X, y)
print("(sklearn)逻辑回归的参数w, b分别为: ", clf.coef_, clf.intercept_, )
