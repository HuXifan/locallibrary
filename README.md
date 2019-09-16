# locallibrary
基于Django的本地图书馆网站
## 配置数据库
使用SQLite数据库 不需要额外配置
## 测试网站框架
项目在运行前，我们应该向运行数据库迁移。这会更新我们的数据库并且包含所有安装的应用（同时去除一些警告）。
### 运行数据库迁移节  
Django 使用对象关系映射器（ORM）将Django代码中的模型定义映射到底层数据库使用的数据结构。当我们更改模型定义时，Django会跟踪更改并创建数据库迁移脚本 (in /locallibrary/catalog/migrations/) 来自动迁移数据库中的底层数据结构来
当我们创建网站时，Django会自动添加一些模型供网站的管理部分使用（稍后我们会解释）。运行以下命令来定义数据库中这些模型的表（确保你位于包含 manage.py 的目录中):
python manage.py makemigrations
python manage.py migrate
