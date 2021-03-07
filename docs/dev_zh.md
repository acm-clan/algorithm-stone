### 开发文档

#### 安装开发环境

###### Windows开发
1 安装python3.9  
2 打开vscode，打开terminal，使用windowns的cmd  
3 安装python库，执行如下命令  
```shell
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

4 安装graphviz-4.6.1，记得添加到PATH中  
5 在根目录执行  
```shell
python src/main.py
```

###### Linux开发（Ubuntu)
1 安装python3.9和pip3，请自行google如何安装  
2 安装python库，执行如下命令  
```shell
pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

4 安装graphviz-4.6.1，建议直接采用源码安装，安装完成后检查版本：
```
dot -v
```
5 在根目录执行  
```shell
python3 src/main.py
```

###### Mac开发
1 安装python3.9和pip3，建议直接在python官网下载安装包
```shell
pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

4 安装graphviz-4.6.1，建议直接采用源码安装，安装完成后检查版本：
```
dot -v
```
5 在根目录执行  
```shell
python3 src/main.py
```

#### 如何调试
在vscode中安装python插件，直接按F5键即可开始调试

#### 目录说明

1 src目录，源代码目录，可以从main.py开始熟悉代码  
2 map目录，输入的目录，给维护人员使用的目录，每个模块使用一个文件，便于查找和编辑，文件名是平台名+模块名称  
3 images是输出目录，程序通过解析map目录中的数据，生成一个svg文件，svg文件在根目录的README.md文件中引用  
4 db目录是数据库文件，用于缓存题目数据，其他一些需要程序缓存的数据  
5 user目录是用户做题目录，对于leetcode平台，可以直接在vscode中编辑和题解，程序会自动监测是否存在题目，如果存在就在svg中标记为已完成  

#### svg文件与做题顺序说明

首先在浏览器中打开svg文件，对于每个算法模块（比如动态规划）来说，需要分子模块，每个子模块下面对应不同的题目，刷题时需要根据从上到下，从左到右的顺序执行。  
这些顺序是我自己刷题后精心编排的，题目之间的梯度比较小。  

#### map文件说明

map文件中对于主模块是[xxx]，对于子模块是[-xxx]，然后子模块下是题目号码，可以参考leetcode-dp.txt文件。

#### 如何参与该项目

#### query工具使用说明
在根目录输入：
``` shell
python3 src/query.py
```

可以看到查询命令

查询tree的所有题目可以输入：
```
leetcode tag tree
```

查询tree的所有简单题目可以输入：
```
leetcode tag tree easy
```

query命令非常方便查询不同tag的题目id

