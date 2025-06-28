
## ？创建虚拟环境
这一步根据个人情况要不要创建
```
python -m venv venv
```
记得激活虚拟环境


## 安装依赖

install flask
```
pip install flask
```

## 运行
```
flask run
```

如果想在手机上也能访问，运行下面这个指令
在同一wifi下，手机电脑连的同一个wifi或者路由器
如果手机访问不到电脑启动的服务器，需要在电脑的防火墙设置一下进栈出栈规则，开放5000端口
```
flask run --host 0.0.0.0
```