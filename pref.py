from .lpmgr import get_supported_addons, is_translations_registed
from .utils import get_installed_addons
from bpy.types import AddonPreferences
from bpy.utils import register_class, unregister_class
from bpy.props import BoolProperty, EnumProperty, StringProperty
from bpy.app import translations

GITHUB_HOME = "https://github.com/lishu/addons_languagepack"

class AddonsLanguagePackPreferences(AddonPreferences):
    '''选项面板'''
    bl_idname=__package__

    disable_addons: StringProperty()
    show_locale_nosupported : BoolProperty(name="Show No Supporetd", description="Show addon in language pack but no current language", default=False)
    show_dev_options : BoolProperty(name="Development Options", description="Show Development Options")
    style_translation : EnumProperty(items=[
        ('NONE', 'None', 'Do not use style translation'),
        ('C4D', 'Cinema 4d', 'Use Cinema 4d style translation'),
        ('MAX', '3D Max', 'Use 3D Max style translation'),
    ], name="Style", description="Style translation use other software common words.", default='NONE')

    def draw(self, context):
        layout = self.layout

        # row = layout.row(align=True)
        # row.label(text="Translation Style")
        # row.prop_tabs_enum(self, 'style_translation')

        # layout.operator('system.language_pack_auto_update')

        user_locale = translations.locale
        addons = get_installed_addons()
        support_addons = get_supported_addons()
        for id in addons:
            bl_info = addons[id]
            support_locales = support_addons.get(id)
            if support_locales is None:
                continue
            col = layout.column(align=True)
            if not self.show_locale_nosupported and not (user_locale in support_locales):
                continue
            row = col.row()
            row.label(text='%s: %s' % (bl_info.get('category', 'Other'), bl_info['name']), translate=False)
            row2 = row.row()
            row2.alignment="RIGHT"
            row2.emboss="NONE"
            if support_locales:
                if user_locale in support_locales:
                    is_registed = is_translations_registed(id)
                    op = row2.operator("system.language_pack_enable_addon", 
                        icon="CHECKBOX_HLT" if is_registed else "CHECKBOX_DEHLT",
                        text="Enable")
                    op.addon_id = id
                    op.enabled = not is_registed
                    if self.show_dev_options:
                        op = row2.operator("system.language_pack_open_addon", icon="FILEBROWSER")
                        op.addon_id = id
                        op.locale = user_locale
                        op = row2.operator("wm.url_open", icon="URL", text="GITHUB")
                        op.url=f"{GITHUB_HOME}/blob/master/libs/{id}/{user_locale}.py"
                else:
                    row2.label(text="No supported your langauge now", icon="ERROR")
            else:
                row2.label(text="No supported this addon")
        
        layout.prop(self, 'show_dev_options')

        if self.show_dev_options:
            row = layout.row(align=True)
            row.prop(self, 'show_locale_nosupported')


def register():
    register_class(AddonsLanguagePackPreferences)

def unregister():
    unregister_class(AddonsLanguagePackPreferences)

if __name__ == "__main__":
    register()