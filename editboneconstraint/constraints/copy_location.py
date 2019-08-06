from .abstract_constraint import AbstractConstraint
import bpy
from mathutils import Matrix


class CopyLocation(AbstractConstraint):
    def evaluate(self, matrix_before):
        if not self.target:
            return

        head_mat = Matrix.Translation(self.target.head)
        tail_mat = Matrix.Translation(self.target.tail)
        new_mat = head_mat.lerp(tail_mat, self.head_tail)

        translation = new_mat.to_translation()

        if self.invert_x:
            translation[0] *= -1
        if self.invert_y:
            translation[1] *= -1
        if self.invert_z:
            translation[2] *= -1

        bone_mat = matrix_before.copy()
        bone_mat.translation = translation
        return bone_mat


exported_constraints = [CopyLocation]
