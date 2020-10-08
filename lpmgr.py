from .utils import get_installed_addons
from bpy.app import translations
from os import path, listdir
import importlib, importlib.util
import bpy

__libs = path.join(path.dirname(__file__), 'libs')
__translations_registed = dict()
__supported_addons = None

def is_translations_registed(module: str) -> bool:
    return __translations_registed.get(module, False)

def get_supported_addons(use_cache = True):
    """获取本地支持翻译的插件信息。

    key: 插件模块名称
    value: list() 支持的区域名称列表
    """
    global __supported_addons
    if use_cache and __supported_addons:
        return __supported_addons
    print('RECREATE SUPPORTED ADDONS')
    addons = dict()
    for addon_dir in listdir(__libs):
        addon_path = path.join(__libs, addon_dir)
        if path.isdir(addon_path):
            addons[addon_dir] = [name[:-3] for name in listdir(addon_path) if name.endswith('.py')]
    __supported_addons = addons
    return addons

def get_module_language_dict(module: str):
    module_dir = path.join(__libs, module)
    # print(module_dir)
    if path.isdir(module_dir):
        lang_dict = dict()
        for file in listdir(module_dir):
            # print(file)
            if file.endswith('.py'):
                try:
                    filepath = path.join(module_dir, file)
                    local = file.split('.')[0]
                    module_spec = importlib.util.spec_from_file_location("%s.libs.%s.%s" % (__package__, module, local), filepath)
                    lang_module = importlib.util.module_from_spec(module_spec)
                    module_spec.loader.exec_module(lang_module)
                    if hasattr(lang_module, 'lang_dict'):
                        lang_dict[local] = getattr(lang_module, 'lang_dict')
                    else:
                        print("ERROR load language module %s, lang_dict not found" % file)
                except:
                    print("ERROR load language module %s" % file)
        return lang_dict
    return None

def get_module_locale_file(module: str, locale: str):
    return path.join(__libs, module, f"{locale}.py")

def register_language(module: str, register: bool = True):
    if register:
        auto_register_language(module)
    else:
        translations.unregister(module)
        del __translations_registed[module]

def auto_register():
    supported_addons = get_supported_addons()
    installed_addons = get_installed_addons()    
    pref = bpy.context.preferences.addons[__package__].preferences
    disable_addons = []
    if pref.disable_addons:
        disable_addons = pref.disable_addons.split(',')
    
    for id in supported_addons:
        if id not in installed_addons or id not in disable_addons:
            auto_register_language(id)


def auto_register_language(module: str):
    language_dict = get_module_language_dict(module)
    # print(language_dict)
    if language_dict:
        try:
            # print("translations.register(%s, %s)" % (module, str(language_dict)))
            translations.register(module, language_dict)
            __translations_registed[module] = True
        except:
            __translations_registed[module] = False
            print("translations register fail.")
    else:
        __translations_registed[module] = False

def unregister_languages():
    for module in __translations_registed.keys():
        translations.unregister(module)