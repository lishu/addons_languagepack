README > [English](readme_en.md),  [简体中文](readme.md)

# Addon's Language Package Manager

This is a Blender plug-in that adds language packs to other plug-ins without directly changing their source code. This allows the user to keep up to date and all translated text still displays correctly.

This plug-in is framework-supported for all languages, but currently the author can only provide Chinese Simplified translation package.

## Translation plan

|Addon|Chinese Simplified(zh_CN)|*Wait for you to join.*|
|-|-|-
|Assign Shape Keys|✔
|BoltFactory|✔
|BlenderKit Online Asset Library|✔
|Auto Mirror|✔
|Edit Mesh Tools|✔
|Extra Objects|✔
|Addon's Language Package Manager|✔
|Animation Nodes|✔
|Import Images as Planes|✔
|3D Navigation|✔
|Math Vis (Console)|✔
|Modifier Tools|✔
|Stored Views|✔
|BoxCutter|✔
|IvyGen|✔
|Curve Tools|✔
|LoopTools|✔
|Align Tools|✔
<small>✔ Translated ⏱Plan</small>

## Join the translation
Obviously it is not possible to translate all the languages alone, or know all the good plug-ins. So welcome to join the translation. You know very good use of domestic plug-ins, you can also try to translate into en_US or other languages.

All you need to do is fork this project add or find what you want to translate in the libs directory.

The translation file structure is: `(addon module name)/(language.py`.
* **addon module name** You can see in the `File:` section of the Blender plug-in management interface that if the last part of this content is `/blenderkit/__init__.py`, its module name is `blenderkit`, and if it is `curve_assign_shapekey.py` its module name is `curve_assign_shapekey`.
* **language** The language code defined for blender, in the interface section of Blender's settings, clicks on the language, displays the language selection panel, and hovers over the corresponding language, displaying the code for that language. You can also view the language code of the current interface directly from `bpy.app.translations.locale` directly in Blender's Python console, or `bpy.app.translations.locales` to view all known language codes.