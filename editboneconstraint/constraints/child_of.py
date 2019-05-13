from .abstract_constraint import AbstractConstraint
import bpy
from mathutils import Matrix
from editboneconstraint.utils import flatten_matrix


class ChildOf(AbstractConstraint):
    def evaluate_pre(self, context):
        """Re-compute the offset between the bone and the target."""
        if context.get("bone_moved"):
            target_mat_with_scale = self.target.matrix.copy() @ Matrix.Scale(
                self.target.length, 4
            )
            self.target_inverse_matrix = target_mat_with_scale.inverted()
            bone_mat_with_scale = self.bone.matrix.copy() @ Matrix.Scale(
                self.bone.length, 4
            )

            self.offset = flatten_matrix(
                self.target_inverse_matrix @ bone_mat_with_scale
            )

    def evaluate(self, matrix_before):
        if not self.target:
            return
        target_mat_with_scale = self.target.matrix.copy() @ Matrix.Scale(
            self.target.length, 4
        )
        new_mat = target_mat_with_scale @ self.offset
        return new_mat


exported_constraints = [ChildOf]
