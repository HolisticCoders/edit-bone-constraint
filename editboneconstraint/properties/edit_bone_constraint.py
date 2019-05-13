import bpy
import re
from uuid import uuid4
from editboneconstraint.bone_mapping import BoneMapping


def get_target(self):
    armature = self.id_data
    target_id = self.target_id

    bone = BoneMapping().bone_from_uuid(armature, target_id)
    if bone:
        return bone.name
    return None


def set_target(self, value):
    armature = self.id_data
    target = armature.edit_bones[value]

    uuid = target.editboneconstraint.uuid
    if not uuid:
        uuid = BoneMapping().register_bone(armature, target)

    self["target_id"] = uuid
    self["target"] = value


class EditBoneConstraintProperty(bpy.types.PropertyGroup):
    type: bpy.props.StringProperty(name="Type")
    target: bpy.props.StringProperty(name="Target", get=get_target, set=set_target)
    target_id: bpy.props.StringProperty(name="Target ID")
    influence: bpy.props.FloatProperty(name="Influence", default=1.0, min=0.0, max=1.0)
    mute: bpy.props.BoolProperty(name="Mute", default=False)
    show_expanded: bpy.props.BoolProperty(name="Show Expanded", default=True)
    head_tail: bpy.props.FloatProperty(name="Head/Tail", default=0.0, min=0.0, max=1.0)
    offset: bpy.props.FloatVectorProperty(name="Offset", size=16, subtype="MATRIX")
    target_inverse_matrix: bpy.props.FloatVectorProperty(
        name="Previously Computed Matrix", size=16, subtype="MATRIX"
    )


class EditBoneConstraintProperties(bpy.types.PropertyGroup):
    constraints: bpy.props.CollectionProperty(
        type=EditBoneConstraintProperty, name="Constraints"
    )
    rest_matrix: bpy.props.FloatVectorProperty(
        name="Rest Matrix", size=16, subtype="MATRIX"
    )
    previously_computed_matrix: bpy.props.FloatVectorProperty(
        name="Previously Computed Matrix", size=16, subtype="MATRIX"
    )
    uuid: bpy.props.StringProperty(name="UUID")
