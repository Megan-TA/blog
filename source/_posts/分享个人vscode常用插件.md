---
title: 分享个人vscode常用插件
catalog: true
date: 2019-06-19 13:39:11
subtitle:
header-img:
tags: IDE
---

1. Visual Studio IntelliCode 智能补全
2. prettier 快速格式化 CMD+Shift+P
3. Regex Previewer 正则表达式测试
4. stylelint
5. vetur # 开发 vue，语法补全、提示助手 （必备插件）
6. vscode-icons # vscode 图标显示
7. 小程序助手
8. vscode-element-helper
9. SVG Viewer # 预览 SVG
10. Path Intellisense 路径自动补全
11. minapp # 小程序开发语法补全、提示助手
12. markdownlint markdown 语法支持和预览
13. Live Server
14. koroFileHeader # 函数注释、文件信息
15. GitLens # git 辅助工具
16. javascript code snippets # js 代码提示、补全
17. Eslint # 代码风格提示
18. Element UI Snippets
19. EditorConfig for vs code
20. Document This
21. Debugger for Chrome
22. Color HighLight
23. CodeIf
24. Code Runner
25. Chinese Lanfguage Pack for vs code
26. Bracket Pair Colorizer 括号以多彩颜色区分
27. Beautify # 美化代码
28. Auto Rename Tag # 自动重命名标签
29. Auto Close Tag # 自动闭合标签
30. Better Comments
31. DotENV
32. Git Graph git可视化工具
33. Git History Diff
34. git-commit-lint-vscode commit加上emoji
35. Import Cost 显示导入模块大小
36. Open file From Path 直接跳转到指定代码
37. VS Color Picker 取色工具
38. vscode-fileheader
39. image preview 侧边栏图片预览

---

给vscode文件目录设置别名，并在引入时有对应提示，需要在根目录下新增`jsconfig.json`的文件

```json
{
    "compilerOptions": {
        "target": "ES6",
        "module": "commonjs",
        "allowSyntheticDefaultImports": true,
        "baseUrl": "./",
        "paths": {
            "@/*": ["src/*"],
            "@public/*": ["src/_public/*"],
        }
    },
    "exclude": [
        "node_modules"
    ]
}
```
