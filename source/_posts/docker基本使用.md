---
title: docker基本使用
catalog: true
date: 2019-06-19 14:15:03
subtitle:
header-img:
tags: docker
---

本文都是基于`centos7`环境使用

1. 启动 docker

启动配置文件默认`/etc/docker/daemon.json`
可以修改配置文件指定 docker 服务启动的一些默认参数

- --regisrty-mirror=PROXY_URL 指定拉取镜像的地址加速 Docker 镜像拉取

  2.docker pull NAME[:TAG]
  默认都是从 `docker`官方仓库去拉取镜像（registry.hub.docker.com）
  一般直接 pull  
  比如：
  `docker`下载`node`的`alpine`版本

```shell
docker pull node:10.15-alpine
```

相当于

```shell
docker pull registry.hub.docker.com/ubuntu:node:10.15-alpine
```

`alpine`是`node`在`docker`运行的最小环境的版本，相比于完整的`node`包体积更小

如果不指定版本默认拉取 `latest`版本，生产环境的时候最好指定版本号，因为`lastest`版本会跟踪最新版本的变更而变化

3.如何进入`未启动`的`node`镜像内部去修改默认一些配置

```shell
docker run -it node:10.15-alpine sh
```

以`shell`脚本的方式去执行`node`命令

4.docker exec ／ docker attach

两者都是进入容器内部

`attach`的不足：

- 多个窗口同时 `attach`同一个容器时候，所有窗口会同步显示；
- 当某个窗口因命令阻塞，所有窗口都无法执行操作；

进入`已成功运行`的容器内部

```shell
docker exec -it 容器名称/容器ID /bin/sh
```

- -i 支持标准输入
- -t 开启一个伪终端

  5.docker ps

- docker ps
  查看已经成功运行的容器（如果运行容器之后 ps 未看到说明容器启动失败）
- docker ps -a
  查看所有容器（包含未成功运行的容器）
- docker ps -f 容器 id  
   根据容器 id 筛选指定容器

  6.docker run

参数部分

- -d 守护进程方式运行
- -p 端口映射 （外部访问的端口：docker 内部端口）
- -u 指定容器的用户
- -v 挂载存储卷映射 （外部存储卷位置：docker 内部存储卷位置）
- -h 指定容器的主机名
- -root
- --name 容器重命名
- --rm 容器停止后自动删除
- --link 关联其它容器

7. 删除

docker rmi XXX

批量删除失效的容器

```
docker rm `docker ps -a -q`
```
