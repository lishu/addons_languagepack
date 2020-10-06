import bpy
from bpy.props import BoolProperty, StringProperty
from .lpmgr import register_language

class SystemLanguagePackEnableAddon(bpy.types.Operator):
    bl_idname = "system.language_pack_enable_addon"
    bl_label = "Enable"
    bl_description = "Enable/Disable Language Pack for this addon"

    addon_id: StringProperty()
    enabled: BoolProperty(default=True)

    def execute(self, context):
        if self.addon_id is None:
            return {"FINISHED"}        
        register_language(self.addon_id, self.enabled)
        pref = bpy.context.preferences.addons[__package__].preferences
        disable_addons = []
        if pref.disable_addons:
            disable_addons = pref.disable_addons.split(',')
        if self.enabled and self.addon_id in disable_addons:
            disable_addons.remove(self.addon_id)
        elif not self.enabled and self.addon_id not in disable_addons:
            disable_addons.append(self.addon_id)
        pref.disable_addons = ','.join(disable_addons)
        return {"FINISHED"}


class SystemLanguagePackAutoUpdate(bpy.types.Operator):
    bl_idname = "system.language_pack_auto_update"
    bl_label = "Auto Update"
    bl_description = "Auto Update All Your Installed & Enable Addon Language Pack"
    bl_options = {"REGISTER"}

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        
        return {"FINISHED"}

def register():
    bpy.utils.register_class(SystemLanguagePackAutoUpdate)
    bpy.utils.register_class(SystemLanguagePackEnableAddon)

def unregister():
    bpy.utils.unregister_class(SystemLanguagePackEnableAddon)
    bpy.utils.unregister_class(SystemLanguagePackAutoUpdate)