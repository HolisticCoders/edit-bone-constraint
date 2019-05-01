import bpy

class AbstractConstraint:
    def __init__(self, prop):
        self.property = prop
        for name, value in prop.items():
            setattr(self, name, value)