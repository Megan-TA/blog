---
title: 常用npm包整理
catalog: false
date: 2019-07-03 09:56:32
subtitle:
header-img:
tags: npm
---

## git 钩子

- husky
- lint-staged

## 代码风格相关

- commitizen
- eslint
- standard-version
- stylelint

```shell
npm install commitizen -g

commitizen init cz-conventional-changelog --yarn --dev --exact


yarn add standard-version -D

```

配置`package.json`

```json

"scripts": {
"release": "standard-version"
},
"husky": {
    "hooks": {
        "pre-commit": "lint-staged"
    }
},
"lint-staged": {
    "src/**/*.{js}": [
        "eslint --fix",
        "git add"
    ]
}
```

参考链接：

1. [commitizen](https://github.com/commitizen/cz-cli)

## tildify

将绝对路径转换为波形路径 比如/Users/sindresorhus/dev → ~/dev

## ora

这个模块用于在终端里有显示载入动画

## download-git-repo

一个用于下载 git 仓库的项目的模块

## inquirer

是一个命令行的回答的模块，你可以自己设定终端的问题，然后对这些回答给出相应的处理

## commander

可以将文字输出到终端当中 多用于提示 根据定义的 bin 的 name 触发对应脚本

## verdaccio

搭建私有 npm 库
