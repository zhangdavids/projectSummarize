当你通过在浏览器里敲http://127.0.0.1:8000/hello/来访问Hello world消息的时候，Django在后台有些什么动作呢？

所有均开始于setting文件。当你运行python manage.py runserver，脚本将在于manage.py同一个目录下查找名为setting.py的文件。这个文件包含了所有有关这个Django项目的配置信息，均大写： TEMPLATE_DIRS , DATABASE_NAME , 等. 最重要的设置是ROOT_URLCONF，它将作为URLconf告诉Django在这个站点中那些Python的模块将被用到

还记得什么时候django-admin.py startproject创建文件settings.py和urls.py吗？自动创建的settings.py包含一个ROOT_URLCONF配置用来指向自动产生的urls.py. 打开文件settings.py你将看到如下：

ROOT_URLCONF = 'mysite.urls'
相对应的文件是mysite/urls.py

当访问 URL /hello/ 时，Django 根据 ROOT_URLCONF 的设置装载 URLconf 。 然后按顺序逐个匹配URLconf里的URLpatterns，直到找到一个匹配的。 当找到这个匹配 的URLpatterns就调用相关联的view函数，并把 HttpRequest 对象作为第一个参数。

正如我们在第一个视图例子里面看到的，一个视图功能必须返回一个HttpResponse。 一旦做完，Django将完成剩余的转换Python的对象到一个合适的带有HTTP头和body的Web Response，（例如，网页内容）。

总结一下：

进来的请求转入/hello/.

Django通过在ROOT_URLCONF配置来决定根URLconf.

Django在URLconf中的所有URL模式中，查找第一个匹配/hello/的条目。

如果找到匹配，将调用相应的视图函数

视图函数返回一个HttpResponse

Django转换HttpResponse为一个适合的HTTP response， 以Web page显示出来

你现在知道了怎么做一个 Django-powered 页面了，真的很简单，只需要写视图函数并用 URLconfs把它们和URLs对应起来。 你可能会认为用一系列正则表达式将URLs映射到函数也许会比较慢，但事实却会让你惊讶。