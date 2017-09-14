JPush Docs
==========

## Get Started

1. 安装 Python（Python 2.7 和 Python 3 都可以，推荐 Python 3）

2. 安装 MKDocs

```bash
$ pip install mkdocs
```

3. `clone` 代码到本地

4. 同步 README（Windows 用户需在 Git 命令行环境下执行）

```bash
$ bash ./hooks/synreadme.sh
```

5. 运行 `MKDocs` 测试服务器

```bash
$ mkdocs serve
```

6. 使用浏览器访问：

```
http://127.0.0.1:8000/
```

## Github Webhook

1. 安装 Python 3

2. 创建并激活虚拟环境 `venv`

```bash
$ python -m venv venv
$ . ./venv/bin/activate
```

3. 安装依赖

```bash
$ pip install -r requirements.txt
```

4. 复制配置文件

```bash
$ cp hooks/hooksrc.sample hooks/hooksrc
$ cp hooks/uwsgi.ini.sample hooks/uwsgi.ini
```

5. 同步 README

```bash
$ bash ./hooks/synreadme.sh
```

6. 使用服务器

- 使用 `Flask` 自带服务器

```bash
$ python hooks/webhooks.py
```

- 使用 `uWSGI` 作为服务器 (`[]`表示可选命令行参数)

> 需要把 `uWSGI` 的配置文件 `hooks/uwsgi.ini` 中的一行配置项 `socket = 127.0.0.1:8080` 改成 `http-socket = 127.0.0.1:8080`

```bash
$ uwsgi -i hooks/uwsgi.ini [ &>> uwsgi.log [&]]
```

- 使用 `Nginx` 管理 `uWSGI`

> 需要保留 `uWSGI` 的配置文件 `hooks/uwsgi.ini` 中的 `socket = 127.0.0.1:8080` 配置项

7. 使用浏览器访问（Flask 服务器和 uWSGI 服务器）：

```
http://127.0.0.1:8080
```

返回 `Hello World` 则说明 github webhook 配置部署成功。

## Contributing

1. 同步 `JPush` 上游仓库的更新到自己的远端仓库
2. 更新文档
3. 提交文档到自己远端仓库
4. 提 `Pull Request` 到 JPush 上游仓库的 `master` 分支

## MKDocs
本文档基于 `Markdown` 编写，使用 [MKDocs](https://github.com/tomchristie/mkdocs) 工具生成 HTML 布局与页面。
