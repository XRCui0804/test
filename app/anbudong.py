import numpy as np


# 欧氏距离计算
def absolutedist(xi, xj):
    return np.sqrt(np.sum((xi - xj) ** 2))  # 计算欧氏距离

def incrementaldist(xi, xj):
    yi = []
    yj = []
    for i in range(len(xi)):
        yi.append(xi[i]-xi[i-1])
        yj.append(xj[i]-xj[i-1])
        yi = np.array(yi)
        yj = np.array(yj)
        return np.sqrt(np.sum((yi - yj) ** 2))

def growthratedist(xi, xj):
    yi = []
    yj = []
    zi = []
    zj = []
    for i in range(len(xi)):
        yi.append(xi[i]-xi[i-1])
        yj.append(xj[i]-xj[i-1])
        yi = np.array(yi)
        yj = np.array(yj)
        zi.append(yi[i]/xi[i-1])
        zj.append(yj[i]/xj[i-1])
        zi = np.array(zi)
        zj = np.array(zj)
        return np.sqrt(np.sum((zi - zj) ** 2))


def distance(absolutedist, incrementaldist, growthratedist):
    # 为给定数据集构建一个包含K个随机质心的集合
    dist = 0.1566 * absolutedist + 0.1287 * incrementaldist + 0.7147 * growthratedist
    return dist


#对一个样本找到与该样本距离最近的聚类中心
def nearest(point, centroids):
    min_dist = 0
    m = np.shape(centroids)[0]  # 当前已经初始化的聚类中心的个数
    for i in range(m):
        # 计算point与每个聚类中心之间的距离
        d = distance(absolutedist(point, centroids[i, ]),incrementaldist(point, centroids[i, ]),growthratedist(point, centroids[i, ]))
        # 选择最短距离
        if min_dist > d:
            min_dist = d
    return min_dist

#选择尽可能相距较远的类中心
def get_centroids(dataset, k):
    m, n = np.shape(dataset)
    centroids = np.zeros((k , n))
    index = np.random.randint(0, m)
    centroids[0,] = dataset[index, ]
    # 2、初始化一个距离的序列
    d = [0.0 for _ in range(m)]
    for i in range(1, k):
        sum_all = 0
        for j in range(m):
            # 3、对每一个样本找到最近的聚类中心点
            d[j] = nearest(dataset[j, ], centroids[0:i, ])
            # 4、将所有的最短距离相加
            sum_all += d[j]
        # 5、取得sum_all之间的随机值
        sum_all *= np.random.rand()
        # 6、获得距离最远的样本点作为聚类中心点
        for j, di in enumerate(d):
            sum_all=sum_all - di
            if sum_all > 0:
                continue
            centroids[i,] = dataset[j, ]
            break
    return centroids


def randCent(dataSet, k):
    m, n = dataSet.shape
    centroids = np.zeros((k, n))
    for i in range(k):
        index = int(np.random.uniform(0, m))  #
        centroids[i, :] = dataSet[index, :]
    return centroids


def KMeans1(dataSet, k):
    """
    k均值聚类
    """
    m = np.shape(dataSet)[0]  # 行的数目
    # 第一列存样本属于哪一簇,第二列存样本的到簇的中心点的误差
    clusterAssment = np.mat(np.zeros((m, 2))) #生成矩阵
    clusterChange = True
    # 第1步 初始化centroids
    centroids = randCent(dataSet, k)
    while clusterChange:  # while True
        clusterChange = False
        # 遍历所有的样本（行数）
        for i in range(m):
            minDist = 100000.0
            minIndex = -1  # 遍历所有的质心
            # 第2步 找出最近的质心
            for j in range(k):
                # 计算该样本到质心的欧式距离
                distances = distance(absolutedist(centroids[j, :], dataSet[i, :]),incrementaldist(centroids[j, :], dataSet[i, :]),growthratedist(centroids[j, :], dataSet[i, :])) # minDist = 100000.0  minIndex = -1
                if distances < minDist:
                    minDist = distances
                    minIndex = j #质心为j
# clusterAssment,第一列存样本属于哪一簇,第二列存样本的到簇的中心点的误差,
            # 第 3 步：更新每一行样本所属的簇
            if clusterAssment[i, 0] != minIndex: #clusterAssment = np.mat(np.zeros((m, 2))) #生成矩阵
                clusterChange = True
                clusterAssment[i, :] = minIndex, minDist ** 2
        # 第 4 步：更新k个质心
        for j in range(k):
            pointsInCluster = dataSet[np.nonzero(clusterAssment[:, 0].A == j)[0]]  # 获取簇类所有的点,非零元素
            centroids[j, :] = np.mean(pointsInCluster, axis=0)  # 对矩阵的行求均值
    print("Congratulations,cluster complete!")
    return centroids, clusterAssment

def deal_data(data: list):
    """
    将二维数组中所有第一个元素相同的数组元素第二个元素相加
    :param data <class: list> 传入的二维数组
    :return <class: dict>
    :raise None
    """
    ret = {}

    data_list = np.array(data)
    for item in data_list:
        if item[0] not in ret:
            ret[item[0]] = item[-1]
        else:
            ret[item[0]] += item[-1]

    return ret

