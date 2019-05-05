from editboneconstraint.utils import lerp
from .constraint_from_property import instanciate_constraint_from_property


class ConstraintManager:

    def __init__(self, bone):
        self._bone = bone

    def evaluate(self):
        constraints = self._instantiate_constraints()
        if not constraints:
            return

        new_matrix = self._bone.initial_matrix
        new_length = self._bone.initial_length
        for constraint in constraints:
            constraint_matrix, constraint_length = constraint.evaluate()
            new_matrix = new_matrix.lerp(constraint_matrix, constraint.influence)
            new_length = lerp(new_length, constraint_length, constraint.influence)

        self._bone.matrix = new_matrix
        self._bone.length = new_length

    def _instantiate_constraints(self):
        constraints = []
        for constraint_prop in self._bone.constraints:
            constraint = instanciate_constraint_from_property(constraint_prop)
            constraints.append(constraint)
        return constraints
    
    def move_constraint(self, constraint, direction):
        constraint_index = self._bone.constraints.values.index(constraint)
        constraint_count = len(self._bone.constraints.values)

        if direction == 'UP' and constraint_index > 0:
            new_index = constraint_index - 1
        elif direction == 'DOWN' and constraint_index < constraint_count:
            new_index = constraint_index + 1
        
        if new_index != constraint_index:
            self._bone.constraints.move(constraint_index, new_index)
    
    def remove_constraint(self, constraint):
        self._bone.constraints.remove(constraint.property)
