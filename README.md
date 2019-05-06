# Blog
基于Django+python的一个简单blog事例
  1. 安装django：pip install django或者pip install django ==<版本号，如1.9.5>
  2. 查看安装的django版本：python -m django --version；
  3. 创建一个文件夹来放置项目，进到此文件夹下；
  4. 执行项目：django-admin startproject myblog
  5. 项目的目录：
          i. manage.py:与项目进行交互的命令行工具集的入口；项目管理器；执行python manage.py来查看所有命令；
          ii. myblog:项目的一个容器；包含项目最近本的一些配置；目录名称不建议修改；
              1. _init_.py
              2. settings.py：项目的总配置文件；里面包含了数据库、Web应用、时间等各种配置；
              3. urls.py：URL配置文件；Django项目中所有地址（页面）都需要我们去配置其URL；
              4. wsgi.py：python服务器网关接口，python应用与web服务器之间的接口；
  6.  启动服务：进入到myblog项目文件夹下执行：python manage.py runserver
  7. 创建应用：进入到myblog项目文件夹下执行：python manage.py startapp blog，并在settings.py文件中的INSTALLED_APPS填写此应用名称；
  8. 应用的目录：
          i.   migratiosns:数据移植模块
          ii.     	_init_.py
          iii.   _init_.py
          iv.   admin.py：该应用的后台管理系统配置
          v.   apps.py：该应用的一些配置（基本不用）
          vi.   models.py：数据模型模块，使用ORM模块
          vii.   tests.py：自动化测试脚本
          viii.   views.py：执行响应的代码所在的模块，代码逻辑处理的重要位置
  9. 完成一个helloword输出：
            view.py文件：
        from django.http import HttpResponse
        # Create your views here.
        
        def index(request):
            return HttpResponse('Hello,World!')
             urls.py文件：
        from django.contrib import admin
        from django.urls import path
        
        import blog.views as bv
        urlpatterns = [
            path('admin/', admin.site.urls),
            path('index/', bv.index),
        ]
             启动服务：python manage.py runserver
             浏览器输入：http://127.0.0.1:8000/index/
  10. 更改url管理：
        urls.py文件：
        from django.contrib import admin
        from django.urls import path,include
        
        urlpatterns = [
            path('admin/', admin.site.urls),
            path('blog/', include('blog.urls')),
        ]
        在app-blog中新建一个urls.py文件，并写入：
        from django.urls import path
        from . import views
        
        urlpatterns = [
            path('', views.index),
        ]
  11. 开发第一个Template：
                  ■ 在APP的根目录下创建名叫Templates的目录:
                  ■ 在该目录下创建HTML文件:
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Title</title>
        </head>
        <body>
        <h1>Hello,Blog!</h1>
        </body>
        </html>
                  ■ 在views.py中返回render()
        from django.shortcuts import render
        from django.http import HttpResponse
        # Create your views here.
        
        def index(request):
            #return HttpResponse('Hello,World!')
            return render(request,'index.html')
  12. DTL初步使用：
        render()函数中支持一个dict类型参数
        　　该字典是后台传递到模板的参数，键为参数名
        　　在模板中使用来直接使用
        views.py：
        ...
        return render(request,'index.html',{'hello':'Hello blog!'})
        ...
        index.html：
        ...
        <h1>{{hello}}</h1>
        ...
  13. Models:
               Django中的models是什么？
          ●        通常，一个Model对应数据库的一张数据表
          ●        Django中Models以类的形式表现
          ●        它包含了一些基本字段以及数据的一些行为
        ORM：
          ● 　　对象关系映射（Object Relation Mapping）
          ● 　　实现了对象和数据库之间的映射
          ● 　　隐藏了数据访问的细节，不需要编写SQL语句
        编写models：
          ●          在应用根目录下创建models.py，并引入models模块
          ●          创建类，继承models.Model，该类即是一张数据表
          ●          在类中创建字段：
        字段即类里面的属性（变量）：attr = models.CharField(max_length = 64)
        models.py文件：
        from django.db import models
        # Create your models here.
        
        class Article(models.Model):
            title = models.CharField(max_length=30, default='Title')
            content = models.TextField(null=True)
        生成数据表：
        默认数据库配置是自带的，可以改成本地mysql数据库：
                      ● 在Python虚拟环境下安装pymysql：pip install pymysql；
                      ● 在项目文件夹下的_init_.py添加如下代码：
                              ■ import pymysql
                              ■ pymysql.install_as_MySQLdb()
                      ● 在settings.py中配置：
        DATABASES = {
                'default': {
                    'ENGINE': 'django.db.backends.mysql',
                    'NAME': 'Blog',  # 新建数据库名
                    'USER': 'root',  # 数据库登录名
                    'PASSWORD': 'root',  # 数据库登录密码
                    'HOST': '127.0.0.1',  # 数据库所在服务器ip地址
                    'PORT': '3306',  # 监听端口 默认3306即可
                }
            }
        命令行中进入manage.py同级目录
        　　        执行命令：
         python manage.py makemigrations app名（可选）
         python manage.py migrate
        查看：
        Django会自动在app/migrations/目录下生成移植文件
        执行命令查看SQL语句：python manage.py sqlmigrate 应用名 文件id
        eg:python manage.py sqlmigrate blog 0001
        默认sqlite3的数据库在项目根目录下db.sqlite3
        查看并编辑db.sqlite3，使用第三方软件，如SQLite Expert Personal
        页面呈现数据：
        后端代码：
        from django.shortcuts import render
        from django.http import HttpResponse
        # Create your views here.
        
        from . import models
        
        def index(request):
            #return HttpResponse('Hello,World!')
            article = models.Article.objects.get(pk=1)
            return render(request,'blog/index.html',{'article':article})
        前端代码：
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Title</title>
        </head>
        <body>
        <h1>{{ article.title }}</h1>
        <h1>{{ article.content }}</h1>
        </body>
        </html>

  14. Admin：
        Django自带的一个功能强大的自动化数据管理界面
        被授权的用户可直接在Admin中管理数据库
        Django提供了许多针对Admin的定制功能
        创建一个超级用户：
        python manage.py createsuperuser
        输入用户名：blog
        输入邮箱：
        输入密码：hzz3563137982
        在浏览器中输入：http://127.0.0.1:8000/admin/即可访问。
        界面是英文的，可以变成中文的：
        在settings 中配置文件中把：LANGUAGE_CODE = 'en-us'改成LANGUAGE_CODE = 'zh-Hans'即可。
        在应用下admin.py中引入自身的models模块
        from . models import Article
        admin.site.register(models.Article)
        每条都显示的Article object，很不方便，显示文章标题比较好
                  ■ 在Article类下添加一个方法
                  ■ 根据Python版本选择str(self) (python3以上)或unicode(self) （python2.7）
                  ■ return self.title,具体代码如下：
        def __str__(self):
        return self.title
  15. 
  16. ff
  17. 

