import bpy
from mathutils import Matrix


class AbstractConstraint:
    def __init__(self, prop):
        self.property = prop
        self.armature = self.property.id_data
        self.type = prop.type
        self.bone = self.armature.edit_bones[prop.bone]
        self.target = self.armature.edit_bones[prop.target]
        self.influence = prop.influence
        self.offset = prop.offset
        self.head_tail = prop.head_tail
