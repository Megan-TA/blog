---
title: node性能优化
catalog: true
date: 2019-12-23 23:14:51
subtitle:
header-img:
tags: node
---

## 性能测试

### 压力测试工具

1. ab
2. webBench

简单介绍下 ab 测试工具使用

```shell
// -c200 模拟200个客户端并发请求 -n1600 一共请求1600次 -t15 压测15s
ab -c200 -n1600 http://127.0.0.1:3000/download
```

测试完有个测试报告，主要关心几个数值：

1.  qps（request per second）: 并发数
2.  Transfer rate （吞吐量）
3.  Time per request（平均响应时间）

### 找到性能瓶颈所在地

1. top （检查 cpu、内存使用情况）
2. iostat （检查 io 设备情况）
3. 后端服务

---

## 性能分析

1. 工具

- Node.js 自带 profile

```js
// 启用profile模式，生成性能的log文件
node --prof 入口文件

// 打开ab进行压测
ab -c200 -t15 http://127.0.0.1:3000/download

// ab测试完之后 分析生成的profile
node --prof-process 刚才生成的log文件
```

- chrome devtool

```js
// inspect-brk 启动时暂停代码执行 debugger模式
node --inspect-brk 入口文件

// 进行压测

// 在chrome devtool的profiler下查看cpu使用情况 地址：chrome://inspect

```

- Clinic.js
