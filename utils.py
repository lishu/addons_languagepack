import bpy
import addon_utils

def get_installed_addons():
    """获取用户安装的插件信息。

    key: 插件模块名称
    value: dict() bl_info 内容字典
    """
    addons = dict()
    for mod in addon_utils.modules():
        addons[mod.__name__] = mod.bl_info
    return addons