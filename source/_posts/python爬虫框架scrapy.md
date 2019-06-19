---
title: python爬虫框架scrapy
catalog: true
date: 2019-06-19 14:07:34
subtitle:
header-img:
tags: python
---
### 基本用法

1.创建项目

```shell
scrapy startproject 项目名称
```

2.创建一个爬虫

```shell
scrapy genspider XX XX.com
```

3.启动脚本

``` shell
scrapy crawl XX
```

4.爬虫脚本

 必须要有`name`和`parse`以及`start_urls`方法，`allowed_domains`可选

```python
# -*- coding: utf-8 -*-
import scrapy

class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baidu.com']
    start_urls = ['https://www.baidu.com/']

    def parse(self, response):
        print(response.text)
```

其中 start_urls可以接受多个url参数，也可以拆分成多个步骤

```python
# -*- coding: utf-8 -*-
import scrapy

class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baidu.com']
    # start_urls = ['https://www.baidu.com/']

    def start_requests(self):
        yield scrapy.Request('https://www.baidu.com')

    def parse(self, response):
        print(response.text)
```

---

1.`Items`相当于定义的需要输出的数据结构；

`item`传参是爬虫脚本的`parse`方法`yield`过来的对象

---

## Pipline

### 1. 介绍

  当item在Spider中被收集之后，会传递到item pipline中处理；

  作用：

- 清理html数据
- 验证爬取数据
- 去重并丢弃
- 数据持久化

### 2. 编写item pipline
  
2.1 必须实现的函数

- process_item

  每个`pipline`都是一个python类，负责接收到`item`并执行一些行为，内部必须实现`process_item(self, item, spider)`方法，必须返回一个`dict`或者`item`对象。

  `piplines`只能接受字典和`items`，在主程序的`parse`方法通过`yield`推送到`piplines`

2.2可以选择实现

- `open_spider(self, spider)`表示当spider开启的时候调用的方法；
- `close_spider(self, spider)`标识当spider关闭的时候调用的方法；
  
注意：

- `pipline`写完需要在配置项`settings`的`ITEM_PIPELINES`里写入来启动

```python
ITEM_PIPELINE {
  demo.pipelines.testDemoPipeline : 300    // 300是优先级 越大优先级越高
}
```

- 文件流写入是缓冲一定字节的数据再一次性写入

  强制立刻写入

```python
self.file.flush()
```

---
