

ruby 是两格的缩进 ！！！

### 基础使用

+ 类和对象

```ruby
class Person
  def initialize(name)
     @name = name
  end

  def show_name
    puts @name
  end
end

zhao = Person.new 'zhao'
qian = Person.new 'qian'

zhao.show_name
qian.show_name

```

简单解释一下，class是定义类Person，def定义两个方法。new是生成对象，会调用initialize这个方法。@name是实例变量的写法。最后两句是调用方法show_name。

+ 块

```ruby
3.times do
  puts 'hello world'
end

people = ['zhao', 'qian']
people.each do |x|
 puts x
end
```

块是ruby的特色。

以上就是两种块的写法，第一个是无参数，后一个带参数x，［］是数组。块可以看成独立的函数，与块前面的方法协同工作，就像二人转。

+ 模块

```ruby
module Show
  def show_msg
    puts 'hello world'
  end
  Pi = 3.14
end

class Person
  include Show
end

class Desk
  include Show
end

puts Show::Pi
Person.new.show_msg
Desk.new.show_msg
```

模块也是Ruby的特色。

主要有两个作用，一个是作为命名空间，避免名字冲突，比如例子中的Pi。另一个是共享代码，例子中Person和Desk共享Show的代码。



