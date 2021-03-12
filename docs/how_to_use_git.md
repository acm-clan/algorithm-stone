# 用颜值超高的github desktop参与开源项目

现在写程序基本上离不开github，每种语言如C/C++、Java、Python还是golang等都会将很多库开源在github上面，本篇文章就和大家聊聊如何使用git的基本操作，来参与github上的开源项目。很多童鞋喜欢直接使用git命令，但是对于新手，我更推荐github desktop客户端来操作git项目，下面一起来看看这个颜值超高的客户端App吧。

  
### 一切的开始clone命令和pull

我们首先需要下载git程序，打开git官网https://git-scm.com/：

![](https://oss.v8cloud.cn/markdown/a984c288a376abaf1c8ddc7959912fa4.png)

下载对应系统的安装包，下载完成后点击安装，这样就可以在cmd使用git命令了，检查版本

``` bash
git --version
```

如下：

![](https://oss.v8cloud.cn/markdown/f8bff1c6c6d51b86ae68226f90d9d995.png)

安装git之后，再到网站https://desktop.github.com/下载GitHub Desktop，如下图：

![](https://oss.v8cloud.cn/markdown/9067cbbee5346638e044421375f4052d.png)

下载后完成安装，首次打开需要输入github的账号和密码，登录之后可以clone项目了，选择File菜单如下：

![](https://oss.v8cloud.cn/markdown/a33d9bf30a155c9eeafb41bfadf8c516.png)

选择url，输入github项目的https地址，注意也可以使用git地址，但是一般使用https方便点，这样可以使用http代理工具，下载速度更快，如下图：

![](https://oss.v8cloud.cn/markdown/55ab2ca1fbddee6023a7dccd67a9953e.png)

这样我们就完成了clone操作。下面再看看pull，当有人提交代码到git后，会出现如下标记：

![](https://oss.v8cloud.cn/markdown/b4925a0f9e7140656a4e2940bdd4bfb0.png)

直接点解Pull origin即可更新到最新代码。

### 切换分支

如下图：

![](https://oss.v8cloud.cn/markdown/b17bdb3f3dd6750d42df3d7e9fabc6a3.png)

点击Current branch下拉界面，如果要切换到dev分支，直接点选就可以切换到dev分支。

  
### 修改后commit提交和push

如果我们修改了项目代码，并且这个项目是我们自己的，只需要输入message就可以直接提交，像下面这样：

![](https://oss.v8cloud.cn/markdown/af32cf0130fc462a096b73483c0b7dc6.png)

点击Commit to main，这时候会有一个Push origin的箭头，点击就会提交到服务器了，如果我们想起来需要修改刚刚的message，可以点击Undo按钮，就可以回退，注意一旦Push，这条记录就会永久产生，Push之前都可以撤销本地的Commit：

![](https://oss.v8cloud.cn/markdown/c9fe97e2c8a19c80691ea802accedc03.png)

Commit操作是把改动提交到本地，Push是把本地的Commit同步到服务器。可以在本地多次commit不push，多次commit后一起push。

### 如何撤销改动

首先选择文件，右键：

![](https://oss.v8cloud.cn/markdown/4dc5997d7588859b5a5b8abab769ea49.png)

选择Discard changes，就可以撤销文件的改动。

### 查看历史log和diff，合并分支

点击history栏：

![](https://oss.v8cloud.cn/markdown/0ad8f336a12e56a3d599ccf1424a9250.png)

可以看到上一次的提交记录。

这个界面还有个非常重要的功能那就是合并分支。

![](https://oss.v8cloud.cn/markdown/b1f00efe4afe8403047340476eb9fdf3.png)

点击红线中的输入框，会出现其他分支的信息，选择分支就可以合并别的分支提交到当前分支。

### 参与github开源

上面的操作基本上满足日常需求了，即使是新手也能几分钟上手。不过github上面的项目大部分不是自己的，如果要提交代码有2种办法，一个是成为contributor，这样可以直接提交代码。另外一个是fork项目然后提交PR。

首先fork项目，然后修改，执行上面的commit和push操作，然后打开github项目网站：

![](https://oss.v8cloud.cn/markdown/48d4d0728eb68ed883e21bdc0e7435d4.png)

点击Pull requests，点击New pull request，出现fork项目和原项目的对比：

![](https://oss.v8cloud.cn/markdown/727943d09e5ab6fe847700523f2d13ab.png)

点击Create pull request，输入修改的信息，这样就在原项目种创建了一条PR，等待原项目的开发merge到开发分支吧。

#### 如何保持项目最新

加上原项目是A，我fork的项目是B，A有了新的更新后，该如何保持我的B也是最新的呢？

依然是点击上面的Pull requests，和上面一样，然后点击Create pull request，如下图：

![](https://oss.v8cloud.cn/markdown/c1d654400ac10bf23954504a79532bde.png)

这时候没有任何changes，上面左边是原项目，右边是fork的，发现了箭头是从我的指向原项目了吗，因为需要将原项目的改变更新到我的项目，所以将左右的项目改变一下位置：

点击左边改成我的项目后出现如下图，两边变成一样的了，点击红色的链接，这个链接的意思是跨项目比较不同的forks差别，然后选择右边为原项目：

![](https://oss.v8cloud.cn/markdown/6e8a48e32c2bbb71013181a8abdafcdc.png)

于是出现这样的指向，原项目的更新也出现了：

![](https://oss.v8cloud.cn/markdown/1bfa005ab58b242b8872dd17fbdb2e68.png)

点击Create pull request，输入title和message，这时候自己的项目出现了一个PR，merge进来就可以和原项目一样新啦。

更新原项目稍微绕了点，不过还是比较简单的。

#### 现在就开始吧

上面大概讲解了操作github desktop的基本用法和参与开源的基本操作，更深入的还是要学习git，git博大精深，写代码必学技能之一，现在就开始吧。

  
  
