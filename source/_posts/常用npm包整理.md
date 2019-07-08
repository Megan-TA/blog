---
title: 常用npm包整理
catalog: false
date: 2019-07-03 09:56:32
subtitle:
header-img:
tags: npm
---

### git钩子

- husky
- lint-staged

### 代码风格相关

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
