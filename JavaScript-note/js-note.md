### javascript是什么？

  它是一门基于客户端的脚本语言，是相对于服务器而言，浏览器就是一个客户端软件，浏览器从服务器上将资源（html,css,js,图片等）请求下来 并且在本地利用浏览器去解析这些资源服务器本质上也是一台电脑。用来接收客户端发过来的请求，并处理请求。同时存储数据 读取数据等操作
  
  
+ ECMAscript JavaScript的核心，描述了语言的基本语法和数据类型，ECMAScript是一套标准，定义了一种语言的标准与具体实现无关
+ DOM（document object model 文档对象模型）一套操作页面元素的API
+ BOM（browser object model 浏览器对象模型）一套操作浏览器功能的API

#### 七大数据类型

基本数据类型（简单数据类型）

* number 数值型
* string 字符串
* boolean 布尔型
* undefined 未定义
* null 空引用

引用数据类型（复杂数据类型）

* object
* Array

### es6 常用特性

1 变量声明 let const

let 是变量
const 是常量

{}大括号内的代码即为作用域

来看一道题

	var funcs = []
	    for (var i = 0; i < 10; i++) {
	        funcs.push(function() { console.log(i) })
	    }
	    funcs.forEach(function(func) {
	        func()
	    })


如何依次输出0-9


	// ES5告诉我们可以利用闭包解决这个问题
    var funcs = []
    for (var i = 0; i < 10; i++) {
        func.push((function(value) {
            return function() {
                console.log(value)
            }
        }(i)))
    }

    // es6
    for (let i = 0; i < 10; i++) {
        func.push(function() {
            console.log(i)
        })
    }


2 模板字符串

基本的字符串格式化，将表达式嵌入字符串进行拼接，用${}来界定

es5 通过反斜杠来做多行字符串或者字符串一行行拼接，es6直接使用反引号搞定

对字符串还提供了很多方法 比如 include repeat等


函数 

函数的默认参数

	function action(num = 200) {
	        console.log(num)
	    }
	    action() //200
	    action(300) //300

箭头函数

ES6很有意思的一部分就是函数的快捷写法。也就是箭头函数。

箭头函数最直观的三个特点。

不需要function关键字来创建函数
省略return关键字
继承当前上下文的 this 关键字

	//例如：
    [1,2,3].map( x => x + 1 )

	//等同于：
    [1,2,3].map((function(x){
        return x + 1
    }).bind(this))


拓展的对象功能


键值对重名：

	function people(name, age) {
	        return {
	            name,
	            age
	        };
	    }


更方便的数据访问--解构


展开运算符

