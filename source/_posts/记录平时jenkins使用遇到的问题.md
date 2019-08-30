---
title: 记录平时jenkins使用遇到的问题
catalog: true
date: 2019-05-21 13:51:07
subtitle:
header-img:
tags: jenkins
---

1. `gitlab`通过`webhooks`在项目指定的分支 push 之后触发 jekins 自动打包

   - 在 jekins 安装 `gitlab-hook-plugin`和 `gitlab-plugin`插件，安装成功的话会在创建项目的`Build Triggers`构建地方看到一个选项 `Build when a change is pushed to GitLab. GitLab webhook URL`

   ![WechatIMG1.png](https://upload-images.jianshu.io/upload_images/6655013-f765101312bb25b4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

按照如下配置方式在`jekins`里指定`dev-hc`分支触发打包

![WechatIMG2.jpeg](https://upload-images.jianshu.io/upload_images/6655013-16a3ba489550681e.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

在`gitlab`指定的项目设置`webhooks`，在项目的 url 写上`jekins`的项目 url 以及对应的`token`,完成之后保存下，按下对应的 Test 按钮可以测试下是否返回 200 状态码

![WechatIMG3.png](https://upload-images.jianshu.io/upload_images/6655013-82715e7e25e1f667.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![WechatIMG4.png](https://upload-images.jianshu.io/upload_images/6655013-4d8f7dcfa20e6b47.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

2. jekins 的时间不正确

打开 【系统管理】->【脚本命令行】运行下面的命令

```shell
System.setProperty('org.apache.commons.jelly.tags.fmt.timeZone', 'Asia/Shanghai')
```

如果是在 docker 下运行的 jenkins 的话，可能上述还不生效，需要切换到`/etc`目录下
如果`timezone`

3. jenkins 配置执行的 shell 对接构建参数

比如构建参数有`job`，在 shell 里面对应的参数就为`$job`
