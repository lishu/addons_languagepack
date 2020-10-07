'''构造 version.json 文件，用于保存最新版本的插件文件信息'''

VERSION_FILE = "version.json"
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


def update_version_file():
    import os, json
    project_dir = os.path.dirname(os.path.dirname(__file__))
    version_file = os.path.join(project_dir, VERSION_FILE)
    libs_dir = os.path.join(project_dir, 'libs')

    version_info = {"title": "Language Pack Version - File Hash"}
    version_addons = dict()

    addon_dirs = os.listdir(libs_dir)
    for addon_name in addon_dirs:
        addon_dir = os.path.join(libs_dir, addon_name)
        addon_langs = dict()
        if os.path.isdir(addon_dir):
            for lang_file in os.listdir(addon_dir):
                if lang_file.endswith('.py'):
                    addon_langs[lang_file[:-3]] = get_file_hash(os.path.join(addon_dir, lang_file))
            if len(addon_langs):
                version_addons[addon_name] = addon_langs
    version_info['addons'] = version_addons
    jo = json.dumps(version_info, indent=3)
    with open(version_file, 'wb') as f:
        f.write(jo.encode('utf8'))
        f.flush()

if __name__ == "__main__":
    update_version_file()