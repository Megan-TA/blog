---
title: vscode常用设置
catalog: true
date: 2020-05-11 13:57:25
subtitle:
header-img:
tags: IDE
---


```json
{
    "workbench.iconTheme": "vscode-icons",
    "editor.fontSize": 14,
    "editor.accessibilityPageSize": 14,
    "editor.formatOnSave": true,
    "editor.tabSize": 4,
    "editor.codeActionsOnSave": {
        "source.fixAll": true
    },
    "window.zoomLevel": 1,
    "fileheader.Author": "knight",
    "fileheader.LastModifiedBy": "knight",
    "fileheader.tpl": "/*\r\n * @Author: {author} \r\n * @Title:  \r\n * @Date: {createTime} \r\n * @Last Modified by:   {lastModifiedBy} \r\n * @Last Modified time: {updateTime} \r\n */\r\n",
    "git.autofetch": true,
    "merge-conflict.diffViewPosition": "Beside",
    "[vue]": {
        "editor.defaultFormatter": "octref.vetur"
    },
    "eslint.alwaysShowStatus": true,
    "eslint.validate": [
        "javascript",
        "javascriptreact",
        {
            "language": "html",
            "autoFix": true
        },
        {
            "language": "vue",
            "autoFix": true
        }
    ],
    "eslint.format.enable": true,
    "vetur.format.defaultFormatter.html": "js-beautify-html",
    "vetur.format.defaultFormatterOptions": {
        "js-beautify-html": {
            "wrap_attributes": "force-aligned"
        }
    },
    "vetur.format.enable": true,
    "vetur.format.defaultFormatter.ts": "prettier",
    "vetur.format.options.tabSize": 4,
    "javascript.preferences.quoteStyle": "single",
    "typescript.preferences.quoteStyle": "single",
    "pretty-formatter.quoteConvert": "single",
    "vetur.format.defaultFormatter.js": "vscode-typescript",
    "path-intellisense.absolutePathToWorkspace": true,
    "path-intellisense.mappings": {
    "@": "${workspaceRoot}/src",
    "@public": "${workspaceRoot}/src/_public"
    },
}
```
