由于softmax模型的相对简单，最终识别准确率92%不到，下面就针对这个数据集构建更加复杂精巧的模型以进一步提高识别准确率。


### 卷积神经网络 CNN

#### 权值的初始化

为了建立模型，我们需要先创建一些权值和偏置等参数，这些参数的初始化过程中需要加入一小部分的噪声以破坏参数整体的对称性，同时为了避免梯度为0.现在改为使用ReLU 激活函数，所以通常将这些参数初始化为很小的正值。

#### 卷积和池化

卷积操作使用滑动步长为1的窗口，使用0进行填充，所以输出规模和输入的一致；

池化操作是在2*2的窗口内采用最大池化技术（max-pooling)。


第一层：卷积层

第一层是卷积层，卷积层将要计算出32个特征映射(feature map)，对每个5 * 5的patch。它的权值tensor的大小为[5, 5, 1, 32]. 前两维是patch的大小，第三维时输入通道的数目，最后一维是输出通道的数目。对每个输出通道加上了偏置(bias)。

为了使得图片与计算层匹配，我们首先reshape输入图像x为4维的tensor，第2、3维对应图片的宽和高，最后一维对应颜色通道的数目。（此处-1表示任意维数。确定输入图像数量，如此处可以填写55000）

然后，使用weight tensor对x_image进行卷积计算，加上bias，再应用到一个ReLU激活函数，最终采用最大池化。

第二层：卷积层

为了使得网络有足够深度，我们重复堆积一些相同类型的层。第二层将会有64个特征，对应每个5 * 5的patch。



全连接层

到目前为止，图像的尺寸被缩减为7 * 7，我们最后加入一个神经元数目为1024的全连接层来处理所有的图像上。接着，将最后的pooling层的输出reshape为一个一维向量，与权值相乘，加上偏置，再通过一个ReLu函数。

Dropout

为了减少过拟合程度，在输出层之前应用dropout技术（即丢弃某些神经元的输出结果）。我们创建一个placeholder来表示一个神经元的输出在dropout时不被丢弃的概率。Dropout能够在训练过程中使用，而在测试过程中不使用。TensorFlow中的tf.nn.dropout操作能够利用mask技术处理各种规模的神经元输出。


输出层

最终，我们用一个softmax层，得到类别上的概率分布。（与之前的Softmax Regression模型相同）。

模型训练和测试

为了测试模型的性能，需要先对模型进行训练，然后应用在测试集上。和之前Softmax Regression模型中的训练、测试过程类似。区别在于：

+ 用更复杂的ADAM最优化方法代替了之前的梯度下降；

+ 增了额外的参数keep\_prob在feed_dict中，以控制dropout的几率；

+ 在训练过程中，增加了log输出功能（每100次迭代输出一次）。


全部代码如下：

```python
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

def weight_varible(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)

def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)

def conv2d(x, W):
    return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')

def max_pool_2x2(x):
    return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')


mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
print("Download Done!")

sess = tf.InteractiveSession()

# paras
W_conv1 = weight_varible([5, 5, 1, 32])
b_conv1 = bias_variable([32])

# conv layer-1
x = tf.placeholder(tf.float32, [None, 784])
x_image = tf.reshape(x, [-1, 28, 28, 1])

h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)
h_pool1 = max_pool_2x2(h_conv1)

# conv layer-2
W_conv2 = weight_varible([5, 5, 32, 64])
b_conv2 = bias_variable([64])

h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)
h_pool2 = max_pool_2x2(h_conv2)

# full connection
W_fc1 = weight_varible([7 * 7 * 64, 1024])
b_fc1 = bias_variable([1024])

h_pool2_flat = tf.reshape(h_pool2, [-1, 7 * 7 * 64])
h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)

# dropout
keep_prob = tf.placeholder(tf.float32)
h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

# output layer: softmax
W_fc2 = weight_varible([1024, 10])
b_fc2 = bias_variable([10])

y_conv = tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2)
y_ = tf.placeholder(tf.float32, [None, 10])

# model training
cross_entropy = -tf.reduce_sum(y_ * tf.log(y_conv))
train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)

correct_prediction = tf.equal(tf.arg_max(y_conv, 1), tf.arg_max(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

sess.run(tf.global_variables_initializer())

for i in range(20000):
    batch = mnist.train.next_batch(50)

    if i % 100 == 0:
        train_accuacy = accuracy.eval(feed_dict={x: batch[0], y_: batch[1], keep_prob: 1.0})
        print("step %d, training accuracy %g"%(i, train_accuacy))
    train_step.run(feed_dict = {x: batch[0], y_: batch[1], keep_prob: 0.5})

# accuacy on test
print("test accuracy %g"%(accuracy.eval(feed_dict={x: mnist.test.images, y_: mnist.test.labels, keep_prob: 1.0})))
```

最终达到99.2左右的准确率。






