---
title: git常用命令
catalog: true
date: 2019-04-25 15:55:22
subtitle:
header-img:
tags: git
---

1. 记录账户密码，不用每次 pull/push 都输入账号密码

   在指定项目下，或者全局的根目录下输入如下命令，再执行 pull 之后输入账号密码，以后就不用再输入了

   ```shell
     git config --global credential.helper store
   ```

2. git 回退版本

   - 本地回退到指定版本

   ```shell
     git reset --hard commit_id
   ```

- 远程强制回退到指定版本

  ```shell
    git push origin HEAD --force
  ```

3. git rebase
   指定要合并 commit 的 id（不包含这个 commit）

   ```shell
     git rebase -i commit_id
   ```

   交互操作： s 合并 commit 记录 p 选中当前 commit 记录

4. git tag
   打标签

```shell
  git tag v1.0.0
```

删除标签

```shell
给标签加注释-m 指定标签版本 -a
```

git tag -a v0.1.0 -m “0.1.2 版本”

```shell
git tag -d v1.0.0
```

推送某次标签 和 本地全部标签

```
git push origin v1.0.0
git push origin –tags
```

5. 项目迁移到新仓库

```
git remote rename origin old-origin
git remote add origin 远程地址
git remote rm old-origin
git push -u origin --all
git push -u origin --tags
```

6. 导出私钥

没有设置 ssh 的话，拉取代码会报`Permission denied, please try again`

导出公私钥的方式`ssh-keygen -t rsa -C "xxxx@xxxx.com"`会生成 id_rsa 和 id_rsa.pub 两个文件，将 id_rsa.pub 拷贝到 gitlab 对应的远程仓库的 ssh keys 列表里面
