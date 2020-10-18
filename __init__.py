bl_info = {
    "name": "Addon's Language Package Manager",
    "author": "lishu",
    "version": (0, 4),
    "blender": (2, 80, 0),
    "description": "Provide your language for many addons",
    "wiki_url": "https://github.com/lishu/addons_languagepack",
    "category": "System",
    }

from .lpmgr import auto_register, unregister_languages
from . import pref
from . import ops
from .autoupdate import register as autoupdate_register, unregister as autoupdate_unregister

def register():
    pref.register()
    autoupdate_register()
    auto_register()
    ops.register()

def unregister():
    ops.unregister()
    autoupdate_unregister()
    unregister_languages()
    pref.unregister()