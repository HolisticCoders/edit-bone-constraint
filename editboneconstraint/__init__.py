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
    CreateChildOfConstraintOperator,
    CreateCopyTransformConstraintOperator,
    CreateCopyLocationConstraintOperator,
    CreateCopyRotationConstraintOperator,
    ClearConstraintOperator,
    EvaluateEditBoneConstraintsOperator,
)
from editboneconstraint.properties import EditBoneConstraintProperty

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
    EditBoneConstraintProperty,
    CreateCopyTransformConstraintOperator,
    CreateCopyLocationConstraintOperator,
    CreateCopyRotationConstraintOperator,
    CreateChildOfConstraintOperator,
    ClearConstraintOperator,
    EvaluateEditBoneConstraintsOperator,
]


def register():
    for cls in classes_to_register:
        bpy.utils.register_class(cls)
    bpy.types.EditBone.constraints = bpy.props.CollectionProperty(
        type=EditBoneConstraintProperty, name="Constraints"
    )


def unregister():
    for cls in classes_to_register:
        bpy.utils.unregister_class(cls)
    del bpy.types.EditBone.constraints
