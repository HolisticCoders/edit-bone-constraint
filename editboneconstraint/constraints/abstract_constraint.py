import abc

import bpy
from mathutils import Matrix

from editboneconstraint.utils import flatten_matrix


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
        self.target_inverse_matrix = prop.target_inverse_matrix

    def evaluate_pre(self, context):
        """Used to do some custom stuff before acually evaluating the constraint."""

    @abc.abstractmethod
    def evaluate(self):
        """Return the computed matrix of the bone."""

    def get_target_matrix(self):
        """Return the matrix of the target bone with the scale component."""
        return self.target.matrix.copy() @ Matrix.Scale(self.target.length, 4)

    @property
    def offset(self):
        return self.property.offset

    @offset.setter
    def offset(self, value):
        self.property.offset = value

    @property
    def target_inverse_matrix(self):
        return self.property.target_inverse_matrix

    @target_inverse_matrix.setter
    def target_inverse_matrix(self, value):
        self.property.target_inverse_matrix = flatten_matrix(value)
