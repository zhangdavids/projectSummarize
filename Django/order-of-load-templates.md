Django默认会在配置文件setting.py的TEMPLATE_LOADERS中开启django.template.loaders.filesystem.Loader，开启该选项后可以按照TEMPLATE_DIRS中列出的路径的先后顺序从中查找并载入模板。

比如有如下配置：

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
)
TEMPLATE_DIRS = (
    '/var/www/site/mycitsm/mycitsm/templates',
    '/var/www/site/mycitsm/sqlreview/templates',
)
现在TEMPLATE_DIRS中指定的两个目录中均存在base.html，渲染模板的语句为 return render(request, 'base.html',context)，那么Django会优先使用第一个目录中的base.html模板。当第一个目录中不存在base.html时，Django才会使用第二个目录中的base.html模板。当然，当两个目录都不存在base.html时，会提示找不到模板。因此为了避免混淆，在使用'django.template.loaders.filesystem.Loader'时尽量不要在TEMPLATE_DIRS指定的不同的位置放置同名模板。

如果确实想在不同的位置放置同名模板呢？比如，为了达到程序复用的目的，我们往往会创建一些某个Django APP特定的static文件和template文件，保存在该APP特定的目录中。而我们不能保证这些文件与其他位置的文件不发生重名。因此这里引入了另外一种模板载入模式'django.template.loaders.app_directories.Loader'，开启该选项后可以从INSTALLED_APPS中已安装app对应的templates/目录中查找要渲染的模板文件（对于静态文件对应的是app的static/目录）。

比如有如下配置：

TEMPLATE_LOADERS = (
   'django.template.loaders.app_directories.Loader'，
)
TEMPLATE_DIRS = ()
这里我们没有在TEMPLATE_DIRS 中指定包含模板文件的路径信息，但由于我们使用的是 'django.template.loaders.app_directories.Loader'载入方式，他会自动从APP对应的templates目录中查找相应的模板文件。比如渲染语句为return render(request, 'base.html',context)，APP对应的模板目录为/var/www/site/mycitsm/sqlreview/templates/，只要该目录中存在base.html，Django就会渲染该模板，不存在则提示找不到，除此之外不会从其他地方找该模板文件了。

细心的你可能已经想到了：要是同时使用了两种载入模板的方式呢？比如同时使用了’django.template.loaders.filesystem.Loader’和’django.template.loaders.app_directories.Loader’会如何查找并载入模板？

比如有如下配置：

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader'，
)
TEMPLATE_DIRS = (
    '/var/www/site/mycitsm/mycitsm/templates',
    '/var/www/site/mycitsm/sqlreview/templates',
)
TEMPLATE_DIRS中指定的两个目录内均存在base.html模板，渲染模板的语句为 return render(request, 'base.html',context)，则Django会先依据TEMPLATE_LOADERS中最先列出的模板载入方式来查找并载入模板，方式同上，若找不到模板文件则使用列出的第二种方式查找，依次类推，直至找到或找不到。这样的话，Django要么找不到模板，要么会载入最先找到的模板，若在多个不同路径下存在同名的模板文件，最终载入的模板与列出的载入方式的顺序和列出的包含模板的目录的顺序嘻嘻相关。这往往是不明确的，极易造成混淆。

因此，通常在APP各自的templates目录中保存APP特定的模板，并不直接在APP对应templates目录中直接存放模板文件本身，而是在该目录中在创建一层以APP名称命名的目录，比如APP名称为sqlreview则存放该APP模板的目录为…/sqlreview/templates/sqlreview/，在指定要渲染的模板时可以通过模板文件的上一层目录来限定模板文件，以避免混淆，这实际上是提供了一个命名空间。比如return render(request, ‘sqlreview/base.html’,context),可以在/var/www/site/mycitsm/sqlreview/templates目录中找到该模板。这样便不用担心Django载入的模板究竟是不是对的、需要的那个模板。

# django 1.8中的改变
在django 1.8中，setting里取消了TEMPLATE_LOADERS和TEMPLATE_DIRS设置，用一个TEMPLATES设置来代替

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'blog/templates'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
其中’DIRS’字段的值是一个列表，用来代替TEMPLATE_DIRS，设置模板的路径

TEMPLATES自带的loader是'django.template.loaders.filesystem.Loader'，如果我们想设置loader为'django.template.loaders.app_directories.Loader'，就将APP_DIRS的值设置为TRUE

## 补充

'django.template.loaders.filesystem.Loader'依赖于’DIRS’的设置，如果’DIRS’是一个空列表的话，他将找不到任何模板

'django.template.loaders.app_directories.Loader'会自动去app下面的template目录下寻找模板，所以采用这种方法就无需给’DIRS’赋值