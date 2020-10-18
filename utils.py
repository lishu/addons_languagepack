BLOCK_SIZE = 65536

GIT_MASTER_RAW = 'https://raw.githubusercontent.com/lishu/addons_languagepack/master/'

def download_string(uri: str):
    '''从给定的网址使用 GET 方式获取文本内容'''
    import requests
    return requests.get(uri).text

def write_languagepack(addon, local, content):
    import os
    with open(os.path.join(os.path.dirname(__file__), f'libs/{addon}/{local}.py'), 'w') as f:
        f.write(content)

def get_languagepack_online(addon, local):
    return download_string(f'{GIT_MASTER_RAW}libs/{addon}/{local}.py')

def get_version_json_online(uri: str = None):
    '''获取线上版本的 version.json 内容'''
    import json
    if uri is None:
        uri = 'https://raw.githubusercontent.com/lishu/addons_languagepack/master/version.json'
    js = download_string(uri)
    return json.loads(js)

def get_version_json_local():
    '''获取本机版本的 version.json 内容'''
    import os, json
    with open(os.path.join(os.path.dirname(__file__), 'version.json')) as f:
        js = f.read()
        return json.loads(js)

def set_version_json_local(d):
    '''设置本机版本的 version.json 内容'''
    import os, json
    with open(os.path.join(os.path.dirname(__file__), 'version.json'), 'w') as f:
        f.write(json.dumps(d, indent=3))

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