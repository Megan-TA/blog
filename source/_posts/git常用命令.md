---
title: git常用命令
catalog: true
date: 2019-04-25 15:55:22
subtitle:
header-img:
tags: git
---

## git merge（合并）

git 中有两个合并策略： fast-forward（-ff）和no-fast-forward（--no-ff）

### fast-forward（--ff）

从master分支切出的dev分支，dev在merge到master时，master分支并没有额外提交，那么合并不会产生新的提交记录

![git merge --ff](https://mmbiz.qpic.cn/mmbiz_gif/meG6Vo0MeviaPS2ZgOV7sV3qpnhsB4LFOtuyKTBrtvK9POh0ZicUNyIXv0ibWLFrc3LicMicWlicFhqlUV5qLcC0t1tw/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1)

### no-fast-forward（--no-ff）

dev在merge到master时，master分支有额外提交，那么合并会产生新的提交记录

![git merge --no-ff](https://mmbiz.qpic.cn/mmbiz_gif/meG6Vo0MeviaPS2ZgOV7sV3qpnhsB4LFOovc8FicicdbGMeIPQt2bFCq8xmucibxsQ7zWib2g8NDW5GWRq2arZ6sktA/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1)

## git rebase（变基）

除了 git merge，还能使用 git rebase 来合并分支。

git rebase 指令会 复制 当前分支的所有最新提交，然后将这些提交添加到指定分支提交记录之上。

比较适合开发阶段，master分支做了修改同步到开发分支。

![git rebase](https://mmbiz.qpic.cn/mmbiz_gif/meG6Vo0MeviaPS2ZgOV7sV3qpnhsB4LFOs1pbHgKho3v46GZhMre3BDX1JHVicL4lTlzKOmVfpwiaqRdwVGZ9WsFA/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1)

## 交互式变基

git rebase 时，我们还能通过交互式变基（Interactive Rebase）方式对当前分支上的提交记录做修改！

变基时提供了 6 种操作模式：

- reword：修改提交信息
- edit：修改此提交
- squash：将当前提交合并到之前的提交中
- fixup：将当前提交合并到之前的提交中，不保留提交日志消息
- exec：在每一个需要变基的提交上执行一条命令
- drop：删除提交

drop案例：
![git rebase -i HEAD~3](https://mmbiz.qpic.cn/mmbiz_gif/meG6Vo0MeviaPS2ZgOV7sV3qpnhsB4LFOBnJ7NwOgrzMIhcKXsME3PiaIaoVQyuNpUyduZk1CZ5s6SLfec8zfONA/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1)

spuash案例：
![git rebase -i HEAD~3](https://mmbiz.qpic.cn/mmbiz_gif/meG6Vo0MeviaPS2ZgOV7sV3qpnhsB4LFOfOgVv8QmLumCzyvHzLutYBgWY5u1buC2ibGibfn8b7LLFg7bM92uB97g/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1)

## git reset（重置）

### 软重置

执行软重置时，撤回到特定提交之后，已有的修改会保留。

![git reset --soft HEAD~3](https://mmbiz.qpic.cn/mmbiz_gif/meG6Vo0MeviaPS2ZgOV7sV3qpnhsB4LFO8dmv56PCuicTzZTVL6lVp541picccqwMAU36EhACmJCMttPvBJl8tXjQ/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1)

### 硬重置

不保留提交的修改也不会保留本地文件修改，直接将当前分支的状态恢复到某个分支提交下。

![git reset --hard HEAD~3](https://mmbiz.qpic.cn/mmbiz_gif/meG6Vo0MeviaPS2ZgOV7sV3qpnhsB4LFOsiboiaLTHUnlyorlyicvxZtRT9tQD4fcX2VponJIcFUpZHbKKdP5p31vQ/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1)

### 远端重置

git push origin HEAD~XXX --force
git push origin COMMIT_ID --force

## git revert（还原）

另一种撤销更改的方式，会创建一条还原的提交记录。

![git revert XXX](https://mmbiz.qpic.cn/mmbiz_gif/meG6Vo0MeviaPS2ZgOV7sV3qpnhsB4LFO9KAj8ZGBkjDallvJibGfibgWnfa5ECCY2pOpf6tZwwicv6RGViazjibRiaAg/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1)

## git cherry-pick（检出提交）

如果分支上的某次提交是合并分支需要的，可以使用cherry-pick单独将某次提交合并分支。

![git cherry-pick XXXX](https://mmbiz.qpic.cn/mmbiz_gif/meG6Vo0MeviaPS2ZgOV7sV3qpnhsB4LFO9KAj8ZGBkjDallvJibGfibgWnfa5ECCY2pOpf6tZwwicv6RGViazjibRiaAg/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1)

## git fetch（获取）

同一分支上开发时，本地获取其他人远端提交的更新方式。

![git fetch](https://mmbiz.qpic.cn/mmbiz_gif/meG6Vo0MeviaPS2ZgOV7sV3qpnhsB4LFOuJEMNkPeXatRs6qqqKUh51nicwicuAyrm8b278TCYShxvv7wHY1n3gkw/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1)

## git pull（拉取）

git pull实际做了两件事： git fetch和git merge

![git pull](https://mmbiz.qpic.cn/mmbiz_gif/meG6Vo0MeviaPS2ZgOV7sV3qpnhsB4LFO9Zib2iag8NqZMe4IrLnEQyqKlicfm6PjbdicfmicbCHNY0yGJu2nweOx2uA/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1)

## git reflog （操作日志）

每个人都会犯错，举一个例子：假设你不小心使用 git reset 命令硬重置仓库到某个提交。后面突然想到，重置导致了一些已有的正常代码的误删！

git reflog用于显示所有已执行性操作的日志！包含合并、重置、还原等

![git reflog](https://mmbiz.qpic.cn/mmbiz_gif/meG6Vo0MeviaPS2ZgOV7sV3qpnhsB4LFOWIushRbiaiagnJor6ac0LTIDZpJiaicPBK0eMibv0uXS9vlD7VlFtva2hFQ/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1)

## git tag（标签）

### 本地打tag

```shell
  git tag v1.0.0
```

### 删除本地标签

- -m 给标签加注释
- -a 指定标签版本

比如：git tag -a v0.1.0 -m “0.1.2 版本”

```shell
git tag -d v1.0.0
```

### 推送某次标签 和 本地全部标签

```shell
git push origin v1.0.0
git push origin –tags
```

## 其他

### 导出私钥

没有设置 ssh 的话，拉取代码会报`Permission denied, please try again`

导出公私钥的方式`ssh-keygen -t rsa -C "xxxx@xxxx.com"`会生成 id_rsa 和 id_rsa.pub 两个文件，将 id_rsa.pub 拷贝到 gitlab 对应的远程仓库的 ssh keys 列表里面

### 项目迁移到新仓库同步所有提交记录

```shell
git remote rename origin old-origin
git remote add origin 远程地址
git remote rm old-origin
git push -u origin --all
git push -u origin --tags
```

### 记录账户密码，不用每次 pull/push 都输入账号密码

在指定项目下，或者全局的根目录下输入如下命令，再执行 pull 之后输入账号密码，以后就不用再输入了

```shell
git config --global credential.helper store
```

### mac 上 git 使用每次都需要输入管理员密码解决

```shell
ssh-add
```

ssh-add 这个命令不是用来永久性的记住你所使用的私钥的。实际上，它的作用只是把你指定的私钥添加到 ssh-agent 所管理的一个
session 当中。而 ssh-agent 是一个用于存储私钥的临时性的 session 服务，也就是说当你重启之后，ssh-agent
服务也就重置了。

下面的命令是永久记住私钥

在~/.ssh/config 文件中添加如下命令：

```shell
Host *
   AddKeysToAgent yes
   UseKeychain yes
   IdentityFile ~/.ssh/id_rsa
```

保存后,输入命令: ssh-add -K ~/.ssh/id_rsa 问题就解决了

## 参考资料

1. [Generating a new SSH key and adding it to the ssh-agent](https://help.github.com/en/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)

2. [图解常用的 Git 指令含义](https://mp.weixin.qq.com/s/oKMdlo6jsIcMcZW8nzoAUg)
