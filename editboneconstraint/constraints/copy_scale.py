import bpy
from mathutils import Matrix

from .abstract_constraint import AbstractConstraint


class CopyScale(AbstractConstraint):
    def evaluate(self, matrix_before):
        if not self.target:
            return
        translation, rotation, scale = matrix_before.decompose()
        axis_angle = rotation.to_axis_angle()
        new_mat = (
            Matrix.Translation(translation)
            @ Matrix.Rotation(axis_angle[1], 4, axis_angle[0])
            @ Matrix.Scale(self.get_target_matrix().to_scale()[0], 4)
        )
        return new_mat


exported_constraints = [CopyScale]
