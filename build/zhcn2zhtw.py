''' 提供使用 zh_CN 转换到 zh_TW '''

from os import path, listdir

from opencc.opencc import OpenCC

# 不自动生成列表，有人工翻译后添加到此列表
NO_TRANS = []

__libs = path.join(path.dirname(path.dirname(__file__)), 'libs')

def c2t_file(cc : OpenCC, source: str, target: str):
    import importlib
    
    source_module_name = source.replace('\\', '.')
    module_spec = importlib.util.spec_from_file_location(f"{source_module_name}", source)
    lang_module = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(lang_module)
    lang_dict = lang_module.lang_dict

    output = []
    output.append('# -*- coding: utf-8 -*-')
    output.append('')
    output.append('lang_dict = {')
    for key in lang_dict:
        tw = cc.convert(lang_dict[key])
        output.append('   (%s, %s) : %s,' % (key[0].__repr__(), key[1].__repr__(), tw.__repr__()))
    output.append('}')
    
    with open(target, 'tw', encoding="utf-8") as f:
        f.write('\n'.join(output))

def c2t():
    cc = OpenCC('s2tw')
    for addon in listdir(__libs):
        addon_dir = path.join(__libs, addon)
        cn_file = path.join(addon_dir, 'zh_CN.py')
        tw_file = path.join(addon_dir, 'zh_TW.py')
        if path.isfile(cn_file):
            c2t_file(cc, cn_file, tw_file)

if __name__ == "__main__":
    c2t()