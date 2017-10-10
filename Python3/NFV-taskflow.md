## 任务执行的taskflow介绍

atom 是 taskflow的最小单位，其他所有的类，包括task类都是atom类的子类

task 是拥有执行和回滚功能的最小工作单元。可以自定义execute和revert方法

使用flow来关联各个task，不仅能够包含task还能够嵌套flow，

常见的有线性，无序，图流。

Retry: Retry 是一个控制当错误发生时, 如何进行重试的特殊工作单元, 而且当你需要的时候还能够以其他参数来重试执行别的 Atom 子类. 常见类型:

+ AlwaysRevert: 错误发生时, 回滚子流
+ AlwaysRevertAll: 错误发生时, 回滚所有流
+ Times: 错误发生时, 重试子流
+ ForEach: 错误发生时, 为子流中的 Atom 提供一个新的值, 然后重试, 直到成功或 retry 中定义的值用完为止.
+ ParameterizedForEach: 错误发生时, 从后台存储(由 store 参数提供)中获取重试的值, 然后重试, 直到成功或后台存储中的值用完为止.

Engine: Engines 才是真正运行 Atoms 的对象, 用于 load(载入) 一个 flow, 然后驱动这个 flow 中的 task/flow 开始运行. 我们可以通过 engine_conf 参数来指定不同的 engine 类型. 常见的 engine 类型如下:

+ serial: 所有的 task 都在调用了 engine.run 的线程中运行.
+ parallel: task 可以被调度到不同的线程中运行.
+ worker-based: task 可以被调度到不同的 woker 中运行.