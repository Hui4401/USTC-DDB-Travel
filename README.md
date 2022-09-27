# USTC-DDB-Travel
中科大软件学院高级数据库课程期末作业，实现一个简单的旅游预订系统，基于 Python + Flask + MySQL

完成功能：

- 普通用户登录注册，管理员登录
- 查询航班，出租车，宾馆信息
- 登录用户可预定航班，出租车，宾馆，并查看自己的预订记录
- 管理员可新增或更新航班，出租车，宾馆信息，还可以更新用户资料和查看用户旅行路线

![image-20210605213446682](https://cdn.jsdelivr.net/gh/Hui4401/file/imgbed/img/2021/06/05/20210605222957.png)

## Install

```bash
git clone https://github.com/Hui4401/USTC-DDB-Travel.git
```

## Usage

首先确保系统已有如下环境：

- Python3.8+
- MySQL8.0

使用步骤：

1. 在 MySQL 中新建一个数据库 travel
2. 打开项目文件夹下的 configs.py，修改其中的数据库连接信息：

```bash
# 修改 root:12345 为自己的数据库用户名密码
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:12345@localhost:3306/travel'
```

3. 命令行执行 `pip install -i https://mirrors.aliyun.com/pypi/simple/ -r requirements.txt` 来安装 Web 环境

4. 执行 `flask fake` 来生成初始数据，这里生成了一个管理员账户 admin 和20条用户名为 user1~user20
   的普通用户，密码均为 111，以及苏州，西安，北京，深圳等地的20余条航班，出租车，酒店数据

5. 接下来执行 `flask run` 或者 `python run.py` 都可以启动系统，之后打开浏览器，访问 http://localhost:5000 来打开系统的 Web 界面

## License

[GPLv3](LICENSE) © Hui4401
