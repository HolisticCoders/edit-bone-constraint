from mathutils import Matrix
from editboneconstraint.utils import lerp, flatten_matrix, matrices_are_equal
from .constraint_from_property import instanciate_constraint_from_property


class ConstraintManager:
    def __init__(self, bone):
        self._bone = bone

    def evaluate(self):
        constraints = self._instantiate_constraints()
        if not constraints:
            return

        # change the rest_matrix if the user has modified the bone's matrix since the last evaluation
        context = {}
        rest_matrix = self._bone.editboneconstraint.rest_matrix
        previously_computed_matrix = (
            self._bone.editboneconstraint.previously_computed_matrix
        )
        current_matrix = self._bone.matrix @ Matrix.Scale(self._bone.length, 4)
        if not matrices_are_equal(current_matrix, previously_computed_matrix):
            self._bone.editboneconstraint.rest_matrix = flatten_matrix(current_matrix)
            rest_matrix = current_matrix
            context["bone_moved"] = True

        new_matrix = rest_matrix
        for constraint in constraints:
            if not constraint.mute:
                constraint.evaluate_pre(context)
                constraint_matrix = constraint.evaluate(new_matrix)
                new_matrix = new_matrix.lerp(constraint_matrix, constraint.influence)

        self._bone.matrix = new_matrix
        extracted_length = new_matrix.to_scale()[0]
        self._bone.length = extracted_length

        self._bone.editboneconstraint.previously_computed_matrix = flatten_matrix(
            new_matrix
        )

    def _instantiate_constraints(self):
        constraints = []
        for constraint_prop in self._bone.editboneconstraint.constraints:
            constraint = instanciate_constraint_from_property(
                constraint_prop, self._bone
            )
            constraints.append(constraint)
        return constraints
