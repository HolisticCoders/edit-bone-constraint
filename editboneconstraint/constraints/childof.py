from editboneconstraint.constraints.abstractconstraint import AbstractConstraint
import bpy
from mathutils import Matrix


class ChildOf(AbstractConstraint):
    def evaluate(self):
        if not self.target:
            return

        # FIXME: For some reason Y and Z locations are swapped, X is Fine
        new_mat = self.target.matrix @ self.offset
        # new_mat = self.offset @ self.target.matrix
        self.bone.matrix = new_mat


exported_constraints = [ChildOf]