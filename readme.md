README > [English](readme_en.md),  [简体中文](readme.md)

# 插件语言包管理器(Addon's Language Package Manager)

这是一个 Blender 插件，用于给其它插件添加语言包而不直接更改其源代码。这样用户可以一直保持更新，所有翻译过的文本仍然能正确显示。

此插件从框架上来说已支持所有语言，但目前作者只能提供简体中文翻译包。

## 翻译计划

|插件|简体中文(zh_CN)|*等你加入*|
|-|-|-
|BoltFactory|✔
|BlenderKit Online Asset Library|✔
|Addon's Language Package Manager|✔
|Animation Nodes|✔
|Import Images as Planes|✔
|3D Navigation|✔
|Math Vis (Console)|✔
|Modifier Tools|✔
|Stored Views|✔
|BoxCutter|✔
<small>✔ 已翻译 ⏱计划</small>

## 加入翻译
很显然不可能一个人翻译所有的语言，或知道所有好的插件。所以欢迎大家一起来加入翻译。你知道很好用的国产插件，也可以试着翻译成英文(en_US)或其它语言

您只需要 fork 本项目，在 libs 目录中添加或找到你要翻译的内容。

翻译文件结构为：`(插件模块名称)/(语言).py`。
* **插件模块名称** 可以在 Blender 插件管理界面中的 `文件：` 部分看到，如果此内容最后一部分是 `/blenderkit/__init__.py`，那它的模块名称为 `blenderkit`，如果是 `curve_assign_shapekey.py` 那它的模块名称为 `curve_assign_shapekey`
* **语言** 为 blender 定义的语言代码，在 Blender 的设置中界面部分，点击语言，显示出来语言选择面板后，鼠标停在对应语言上，会显示此语言的代码。你也可以直接在 Blender 的 Python 控制台中执行 `bpy.app.translations.locale` 查看当前界面的语言代码，或执行 `bpy.app.translations.locales` 查看所有已知的语言代码