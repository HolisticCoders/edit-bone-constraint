from editboneconstraint.utils import lerp
from .constraint_from_property import instanciate_constraint_from_property


class ConstraintManager:
    def __init__(self, bone):
        self._bone = bone

    def evaluate(self):
        constraints = self._instantiate_constraints()
        if not constraints:
            return

        new_matrix = self._bone.editboneconstraint.initial_matrix
        for constraint in constraints:
            if not constraint.mute:
                constraint_matrix = constraint.evaluate(new_matrix)
                new_matrix = new_matrix.lerp(constraint_matrix, constraint.influence)

        self._bone.matrix = new_matrix
        extracted_length = new_matrix.to_scale()[0]
        self._bone.length = extracted_length

    def _instantiate_constraints(self):
        constraints = []
        for constraint_prop in self._bone.editboneconstraint.constraints:
            constraint = instanciate_constraint_from_property(constraint_prop)
            constraints.append(constraint)
        return constraints
