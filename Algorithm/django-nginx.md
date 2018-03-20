## django 处理并发

安装 uwsgi 

```
pip install uwsgi
```


测试 uwsgi 提供的 web 服务的功能

创建 test

```
# 创建 test.py 文件
def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return [b"Hello World"] # python3
    #return ["Hello World"] # python2
    
```    

启动服务

```
uwsgi --http :8000 --wsgi-file test.py 
```

```
netstat -lnpt | grep uwsgi
```

```
# test-uwsgi.ini

[uwsgi]
# 对外提供 http 服务的端口
http = :9000

#the local unix socket file than commnuincate to Nginx   用于和 nginx 进行数据交互的端口
socket = 127.0.0.1:8001

# the base directory (full path)  django 程序的主目录
chdir = /data/django_test

# Django's wsgi file
wsgi-file = django_test/wsgi.py

# maximum number of worker processes
processes = 4

#thread numbers startched in each worker process
threads = 2
 
#monitor uwsgi status  通过该端口可以监控 uwsgi 的负载情况
stats = 127.0.0.1:9191


# clear environment on exit
vacuum          = true

# 后台运行,并输出日志
daemonize = /var/log/uwsgi.log
```


```
/usr/local/bin/uwsgi test-uwsgi.ini # 在浏览器中 通过访问 http://ip:9000 可以看到发布的 django 程序
```

更好的性能是通过 NGINX

```
# django-nginx.cnf

# the upstream component nginx needs to connect to
upstream django {
    # server unix:///path/to/your/mysite/mysite.sock; # for a file socket
    server 127.0.0.1:8001; # for a web port socket (we'll use this first)
}
 
# configuration of the server
server {
    # the port your site will be served on
    listen      8000;
    # the domain name it will serve for
    server_name .example.com; # substitute your machine's IP address or FQDN
    charset     utf-8;
 
    # max upload size
    client_max_body_size 75M;   # adjust to taste
 
    # Django media
    location /media  {
        alias /path/to/your/mysite/media;  # your Django project's media files - amend as required
    }
 
    location /static {
　　　　　# 需要修改的地方在这里
        alias /data/django_test/static_all; # your Django project's static files - amend as required
    }
 
    # Finally, send all non-media requests to the Django server.
    location / {
        uwsgi_pass  django;
        include     /data/django_test/uwsgi_params; # the uwsgi_params file you installed
    }
}
```


修改好 配置文件之后 重启服务即可

```
nginx -t
nginx -s reload
```



