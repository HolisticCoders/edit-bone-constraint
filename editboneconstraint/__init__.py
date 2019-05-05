# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
import os
import site

vendor_dir = os.path.join(os.path.dirname(__file__), "vendor")
site.addsitedir(vendor_dir)

import bpy

from editboneconstraint.operators import (
    AddConstraintOperator,
    AddConstraintWithTargetsOperator,
    ClearConstraintOperator,
    EvaluateEditBoneConstraintsOperator,
)
from editboneconstraint.constraints import instanciate_constraint_from_property
from editboneconstraint.graph import sort_bones_by_constraints
from editboneconstraint.properties import EditBoneConstraintProperty
from editboneconstraint.ui import ConstraintStackPanel

bl_info = {
    "name": "Edit Bone Constraints",
    "author": "Loïc Pinsard, Alexy Long",
    "description": "This addon lets you add constraints in the edit mode of an armature. Allowing you to have guide bones that control the placement of all the other bones of your rig.",
    "blender": (2, 80, 0),
    "version": (0, 0, 1),
    "location": "",
    "warning": "",
    "category": "Rigging",
}


classes_to_register = [
    # properties
    EditBoneConstraintProperty,

    # operators
    AddConstraintOperator,
    AddConstraintWithTargetsOperator,
    ClearConstraintOperator,
    EvaluateEditBoneConstraintsOperator,

    # ui
    ConstraintStackPanel,
]


addon_keymaps = []


@bpy.app.handlers.persistent
def evaluate_constraints(*args):
    if (
        # bpy.context.area.type == "VIEW_3D"
        bpy.context.active_object.type == "ARMATURE"
        and bpy.context.object.mode == "EDIT"
    ):
        armature = bpy.context.object.data
        sorted_bones = sort_bones_by_constraints(armature)
        for bone in sorted_bones:
            for constraint_prop in bone.constraints:
                constraint = instanciate_constraint_from_property(constraint_prop)
                constraint.evaluate()


def register():

    # register the classes
    for cls in classes_to_register:
        bpy.utils.register_class(cls)

    # add the property to the edit bones
    bpy.types.EditBone.constraints = bpy.props.CollectionProperty(
        type=EditBoneConstraintProperty, name="Constraints"
    )
    bpy.types.EditBone.initial_matrix = bpy.props.FloatVectorProperty(
        name='Initial Matrix',
        size=16,
        subtype='MATRIX',
    )
    bpy.types.EditBone.initial_length = bpy.props.FloatProperty(name="Initial Length")

    # handle the keymap
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name="3D View", space_type="VIEW_3D")
    kmi = km.keymap_items.new("editbone.constraint_add_with_targets", "C", "PRESS", ctrl=True, shift=True)
    addon_keymaps.append((km, kmi))

    # callbacks
    bpy.app.handlers.frame_change_pre.append(evaluate_constraints)


def unregister():
    # unregister the classes
    for cls in classes_to_register:
        bpy.utils.unregister_class(cls)

    # delete the edit bones property
    del bpy.types.EditBone.constraints

    # handle the keymap
    for keymap, keymap_item in addon_keymaps:
        keymap.keymap_items.remove(keymap_item)
    addon_keymaps.clear()

    # callbacks
    bpy.app.handlers.frame_change_pre.remove(evaluate_constraints)
