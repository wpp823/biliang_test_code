from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

# 获取数据

iris = load_iris()

# 2.数据的基本处理

x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=22)

# 3.特征工程，特征预处理

transfer = StandardScaler()
x_train = transfer.fit_transform(x_train)
x_test = transfer.transform(x_test)

# 4.机器学习--KNN
# 4.1 实例化一个预估器

estimator = KNeighborsClassifier()

# 4.2 模型调优--交叉验证,网格搜索
param_grid = {"n_neighbors": [1, 3, 5, 7]}

estimator = GridSearchCV(estimator, param_grid=param_grid,cv=5)

# 4.3 模型训练
estimator.fit(x_train, y_train)

# 5.模型评估
# 5.1 预测值结果输出
y_pre = estimator.predict(x_test)
print(f"预测值:{y_pre}")

# 5.2 准确率计算
score = estimator.score(x_test, y_test)

print(f"准确率:{score}")

# 5.3 查看交叉验证,网格搜索的一些属性

print(f"在交叉验证中的得到的最好结果:{estimator.best_score_}")
print(f"在交叉验证中的得到的最好模型:{estimator.best_estimator_}")
print(f"在交叉验证中的得到的模型结果:{estimator.cv_results_}")
