import abc
import bpy
from mathutils import Matrix


class AbstractConstraint(metaclass=abc.ABCMeta):
    def __init__(self, prop):
        self.property = prop
        self.armature = self.property.id_data
        self.type = prop.type
        self.bone = self.armature.edit_bones[prop.bone]
        self.target = self.armature.edit_bones[prop.target]
        self.influence = prop.influence
        self.head_tail = prop.head_tail

        self.offset = prop.offset
        self.initial_matrix = prop.initial_matrix
        self.initial_length = prop.initial_length

    @abc.abstractmethod
    def evaluate(self):
        """Return the computed matrix and length of the bone."""

