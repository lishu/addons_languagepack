
# 升级步骤
# 1. 下载线上 version 文件
# 2. 读取本地 version 文件
# 3. 比较当前语言下的插件可用更新
# 4.    下载新语言包到暂时位置
# 5.    下载成功后替换本地语言包文件
# 6.    替换成功后重新禁止、启用对应语言包
# 7.    报告更新成功
# 8. 所有更新完成后重写本地 version 文件

import bpy
from .utils import get_languagepack_online, get_version_json_online, get_installed_addons, get_version_json_local, set_version_json_local, write_languagepack

AUTO_UPDATE_STATE = [
    ('NONE', 'None', 'No Updated'),
    ('CHECK', 'Checking', 'Check version'),
    ('CHECKED', 'Checked', 'Checked without update'),
    ('UPDATING', 'Updating', 'Updating packages'),
    ('DONE', 'Done', 'Update done'),
    ('FAIL', 'Fail', 'Update fail')
]

def get_update_status():
    return bpy.context.preferences.addons[__package__].preferences.update_status

def set_update_status(context, status):
    context.window_manager.addons_languagepack_update_status = status

def get_version_hash(addons_json, name, language):
    for addon_name in addons_json:
        if addon_name == name:
            return addons_json[addon_name].get(language)
    return None

def set_version_hash(addons_json, name, language, hash):
    for addon_name in addons_json:
        if addon_name == name:
            addons_json[addon_name][language] = hash
            return

def run_update(context, user_language):
    import json, os
    set_update_status(context, 'CHECK')
    try:
        remote_version = get_version_json_online()['addons']
        local_version_obj = get_version_json_local()
        local_version = local_version_obj['addons']
        installed_addons = get_installed_addons()
        update_addons = dict()
        for addon_module in installed_addons:
            remote_hash = get_version_hash(remote_version, addon_module, user_language)
            local_hash = get_version_hash(local_version, addon_module, user_language)
            print(f'{remote_hash} {local_hash}')
            if remote_hash and remote_hash != local_hash:
                update_addons[addon_module] = remote_hash
        if len(update_addons) == 0:
            print('No update need')
            set_update_status(context, 'CHECKED')
            return

        set_update_status(context, 'UPDATING')
        # 更新单个语言包
        for addon in update_addons:
            print(f'Download language package for {addon}({user_language})')
            lp = get_languagepack_online(addon, user_language)
            if lp:
                write_languagepack(addon, user_language, lp)
                set_version_hash(local_version, addon, user_language, update_addons[addon])
        # 更新本地版本文件
        set_version_json_local(local_version_obj)

        # 重新注册语言包
        try:
            from .lpmgr import auto_register, unregister_languages
            unregister_languages()
            auto_register()
        except:
            print('Update done but can not Re-register.')
        
        print('Update done')
        set_update_status(context, 'DONE')
    except:
        set_update_status(context, 'FAIL')

def register():
    bpy.types.WindowManager.addons_languagepack_update_status = bpy.props.EnumProperty(items=AUTO_UPDATE_STATE, name="Update Status", default="NONE", options={'HIDDEN', 'SKIP_SAVE'})

def unregister():
    delattr(bpy.types.WindowManager, 'addons_languagepack_update_status')    

if __name__ == "__main__":
    register()