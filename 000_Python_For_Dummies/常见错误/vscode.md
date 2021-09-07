# VSCODE

## 设置python3
```bash
# 1. 检查本地python版本
# 查看是否成功安装python3.x

python3 -V 

# 2.查看python3路径
which python3
```

三、在VSCode中打开首选项，搜索：python.pythonPath

"python.pythonPath": "python"
改为：
"python.pythonPath": "/usr/local/bin/python3"，

四、这是我们F5调试，可能还是报错，我们需要把调试模式选择为python: terminal(external)
