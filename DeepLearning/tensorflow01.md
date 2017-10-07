## tf 学习笔记总结 01

概念之类的就不重复记录了。

主要是一些总结性的东西，可能可读性不是很好...

### 设计理念

1. 图的定义和图的运行完全分开  
    符号式编程

	涉及很多的嵌入和优化，不容易理解和调试，但是运行速度有所提升
	
	Torch是典型的命令式  
	TensorFlow完全是符号式编程  
	Caffe MXNet则是采用了混合式编程（两种都有）  

2. 涉及的运算都要放在图中，图的运行只发生在会话（session）中  

### 编程模型

使用数据流图做计算的，因此需要先创建一个数据流图。  

包括有：  
输入input  
塑形reshape  
Relu 层  
Logit 层  
Softmax  
交叉熵 cross entropy  
梯度  gradient  
SGD 训练层  
等  

tensor 张量代表了数据流图中的边

flow 流动这个动作则是代表了数据流图中节点做的操作

#### 边

两种连接关系： 数据依赖和控制依赖。  

任意维度的数据统称为张量。张量在数据流图中从前往后流动一遍就完成了一次前向传播，也就是fp，

残差从后往前流动完成bp

虚线边被称为控制依赖，常用代码为：  

```
tf.Graph.control_dependencies(control_inputs)
```

支持的张量具体为 tf.float64 tf.float32 等等，具体详查


#### 节点

节点又被称为算子，代表了一个操作，一般用来表示施加的数学运算，也可以表示数据输入input或者是输出的终点

或读取／写入持久变量的终点

常用的操作有：

|类别 |例子  |
| --------   | :----- |
|数学运算  |  Add, Subtract, Multiply, Div, Exp, Log, Greater, Less, Equal...  |
|数组| Concat, Slice, Split, Constant, Rank, Shape, Shuffle... |
|矩阵 |  MatMul, MatrixInverse, MatrixDeterminant... |
|有状态的操作| Variable, Assign, AssignAdd...|
|神经网络的构建|  SoftMax, Sigmoid, ReLU, Convolution2D, MaxPool...|
|检查点操作|  Save, Restore...|
|队列和同步操作| Enqueue, Dequeue, MutexAcquire, MutexRelease... |
|控制张量流动的操作| Merge, Switch, Enter, Leave, NextIteration...|


以tensorflow 1.1.0为例子，相关的代码在tensorflow/python/ops/目录下

### 其他概念

#### 图

把操作任务描述成有向无环图，先创建各个节点。

#### 会话

启动图的第一步是创建一个会话

建立会话之后，会生成一张空图，在会话中添加节点和边，形成一张图，然后执行。


#### 设备

目前较多使用 GPU ，从0开始

#### 变量

变量是特殊的数据，它在图中有固定的位置，不像普通张量那样可以流动


### 常用API

图的api

|操作|描述|
|------|:------|
|tf.Graph.\__init__()|创建一个空图|
|.as_default()|将某个图设置为默认图|
|.device(device\_name\_or\_function)|定义运行图所使用的设备，并返回一个上下文|
|.name_scope(name)|为节点创建层次化的名称，并上下文|


节点的api

|操作|描述|
|------|:------|
|tf.Operation.name|操作的名称|
|type|类型，比如MatMul|
|inputs, outputs|操作的输入与输出|
|control_inputs|操作的依赖|
|run(feed_dict=None, session=None)|在会话中运行该操作|
|get_attr(name)|获取操作的属性值|


张量的api

|操作|描述|
|------|:------|
|tf.Tensor.dtype|张量的数据类型|
|name|名称|
|value_index|在操作输出中的索引|
|graph|所在的图|
|op|产生该张量的操作|
|consumers()|返回该张量的操作列表|
|eval()|在会话中求张量的值|
|get_shape()|返回用于表示张量的形状的类|
|set_shape()|更新形状|
|device|设置计算该张量的设备|



交互式的情况下，可以使用InteractiveSession类，以及Tensor.eval()、Operation.run()等方法

```python
# Enter an interactive TensorFlow Session.
import tensorflow as tf
sess = tf.InteractiveSession()

x = tf.Variable([1.0, 2.0])
a = tf.constant([3.0, 3.0])

# Initialize 'x' using the run() method of its initializer op.
x.initializer.run()

# Add an op to subtract 'a' from 'x'.  Run it and print the result
sub = tf.sub(x, a)
print(sub.eval())
# ==> [-2. -1.]

# Close the Session when we're done.
sess.close()
```

抓取ops的输出，需要先执行session的run函数，然后通过print函数打印出状态信息。


```python
input1 = tf.constant(3.0)
input2 = tf.constant(2.0)
input3 = tf.constant(5.0)
intermed = tf.add(input2, input3)
mul = tf.mul(input1, intermed)

with tf.Session() as sess:
  result = sess.run([mul, intermed])
  print(result)

# output:
# [array([ 21.], dtype=float32), array([ 7.], dtype=float32)]
```

填充

先创建特定数据类型的占位符placeholder，再进行数据的填充。

```python
input1 = tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)
output = tf.mul(input1, input2)

with tf.Session() as sess:
  print(sess.run([output], feed_dict={input1:[7.], input2:[2.]}))

# output:
# [array([ 14.], dtype=float32)]
```


官网上有一段示例程序，关于曲线拟合的计算

```python
# 简化调用库名
import tensorflow as tf
import numpy as np

# 模拟生成100对数据对, 对应的函数为y = x * 0.1 + 0.3
x_data = np.random.rand(100).astype("float32")
y_data = x_data * 0.1 + 0.3

# 指定w和b变量的取值范围（注意我们要利用TensorFlow来得到w和b的值）
W = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
b = tf.Variable(tf.zeros([1]))
y = W * x_data + b

# 最小化均方误差
loss = tf.reduce_mean(tf.square(y - y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

# 初始化TensorFlow参数
init = tf.initialize_all_variables()

# 运行数据流图（注意在这一步才开始执行计算过程）
sess = tf.Session()
sess.run(init)

# 观察多次迭代计算时，w和b的拟合值
for step in xrange(201):
    sess.run(train)
    if step % 20 == 0:
        print(step, sess.run(W), sess.run(b))

# 最好的情况是w和b分别接近甚至等于0.1和0.3
```

### 经典例子

MNIST 手写体识别任务

有一个简单的图片数据集，包含了大量的数字手写体图片，包含标注信息，也就是俗称的标签，数据集的数据分为三份：训练，测试，验证的比例为55000:10000:5000，也就是11:2:1。当然按照吴恩达老师的建议比例是6:2:2为最好。

训练集用来训练模型，

测试集是不可见的，相当于一个黑盒子，

验证数据集可以检验所训练出来的模型的正确性和是否过拟合。

图片是 28*28 的像素点矩阵，在此我们以784的一维数组来表示图片，

训练的数据集可以是一个形状为55000*784位的tensor，

labels的值在0-9之间，使用one hot向量来表示label，

mnist.train.labels是一个55000 * 10的二维数组。

#### Softmax Regression模型

数字手写体图片的识别，实际上可以转化成一个概率问题，如果我们知道一张图片表示9的概率为80%，而剩下的20%概率分布在8，6和其他数字上，那么从概率的角度上，我们可以大致推断该图片表示的是9.

Softmax Regression是一个简单的模型，很适合用来处理得到一个待分类对象在多个类别上的概率分布。所以，这个模型通常是很多高级模型的最后一步。

Softmax Regression大致分为两步：

Step 1: add up the evidence of our input being in certain classes;
Step 2: convert that evidence into probabilities.

```python
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
print("Download Done!")

x = tf.placeholder(tf.float32, [None, 784])

# paras
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))

y = tf.nn.softmax(tf.matmul(x, W) + b)
y_ = tf.placeholder(tf.float32, [None, 10])

# loss func
cross_entropy = -tf.reduce_sum(y_ * tf.log(y))

train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

# init
init = tf.global_variables_initializer()

sess = tf.Session()
sess.run(init)

# train
for i in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

correct_prediction = tf.equal(tf.arg_max(y, 1), tf.arg_max(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))

print("Accuarcy on Test-dataset: ", sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))
```

目前得到的结果只有91.8的准确率，[这里](http://rodrigob.github.io/are_we_there_yet/build/classification_datasets_results.html)有众多数据集上不同模型的准确率。













