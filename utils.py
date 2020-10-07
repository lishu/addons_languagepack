BLOCK_SIZE = 65536

def get_file_hash(path: str):
    '''获取文件的 hash 代码'''
    import hashlib
    file_hash = hashlib.sha256()
    with open(path, 'rb') as f:
        fb = f.read(BLOCK_SIZE)
        while len(fb) > 0:
            file_hash.update(fb)
            fb = f.read(BLOCK_SIZE)
    return file_hash.hexdigest()

def get_installed_addons():
    """获取用户安装的插件信息。

    key: 插件模块名称
    value: dict() bl_info 内容字典
    """
    import addon_utils
    addons = dict()
    for mod in addon_utils.modules():
        addons[mod.__name__] = mod.bl_info
    return addons