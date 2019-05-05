from .abstract_constraint import AbstractConstraint
import bpy
from mathutils import Matrix


class CopyLocation(AbstractConstraint):
    def evaluate(self):
        if not self.target:
            return

        head_mat = Matrix.Translation(self.target.head)
        tail_mat = Matrix.Translation(self.target.tail)
        new_mat = head_mat.lerp(tail_mat, self.head_tail)

        bone_mat = self.bone.matrix.copy()
        bone_mat.translation = new_mat.to_translation()
        self.bone.matrix = bone_mat

exported_constraints = [CopyLocation]
