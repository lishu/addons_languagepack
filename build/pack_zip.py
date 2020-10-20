'''生成版本发布需要的 zip 包'''

import os
import zipfile

def copy_dir_to_zip(target: 'zipfile.ZipFile', srcdir: str, arcname: str):
    for p in os.listdir(srcdir):
        src = os.path.join(srcdir, p)
        tgr = os.path.join(arcname, p)
        if os.path.isdir(src):
            copy_dir_to_zip(target, src, tgr)
        elif os.path.isfile(src):
            print('%s > %s'%(src, tgr))
            target.write(src, tgr)

def make_zip():
    with zipfile.ZipFile('addons_languagepack.zip', 'w') as target:
        target.write('__init__.py', 'addons_languagepack/__init__.py')
        target.write('autoupdate.py', 'addons_languagepack/autoupdate.py')
        target.write('lpmgr.py', 'addons_languagepack/lpmgr.py')
        target.write('ops.py', 'addons_languagepack/ops.py')
        target.write('pref.py', 'addons_languagepack/pref.py')
        target.write('utils.py', 'addons_languagepack/utils.py')
        target.write('version.json', 'addons_languagepack/version.json')
        copy_dir_to_zip(target, '__pycache__', 'addons_languagepack/__pycache__')
        copy_dir_to_zip(target, 'libs', 'addons_languagepack/libs')

if __name__ == "__main__":
    make_zip()