import abc

import bpy
from mathutils import Matrix


class AbstractConstraint(metaclass=abc.ABCMeta):
    def __init__(self, prop, bone):
        self.property = prop
        self.armature = self.property.id_data
        self.type = prop.type
        self.bone = bone
        self.target = self.armature.edit_bones[prop.target]
        self.influence = prop.influence
        self.head_tail = prop.head_tail
        self.mute = prop.mute
        self.offset = prop.offset
        self.invert_x = prop.invert_x
        self.invert_y = prop.invert_y
        self.invert_z = prop.invert_z

    @abc.abstractmethod
    def evaluate(self):
        """Return the computed matrix and length of the bone."""

    def get_target_matrix(self):
        """Return the matrix of the target bone with the scale component."""
        return self.target.matrix.copy() @ Matrix.Scale(self.target.length, 4)
