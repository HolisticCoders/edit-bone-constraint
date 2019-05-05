import os
import importlib
from collections import OrderedDict


def instanciate_constraint_from_property(prop):
    if prop.type in _all_constraints:
        return _all_constraints[prop.type](prop)
    else:
        raise TypeError("No class named corresponding to constraint type {}".format(prop.type))


def _get_all_constraints_classes():
    all_constraints = {}
    current_dir = os.path.dirname(__file__)
    for mod in os.listdir(current_dir):
        is_dir = os.path.isdir(os.path.join(current_dir, mod))
        is_py_file = mod.endswith('.py')
        is_init = mod == os.path.basename(__file__)
        if is_dir or not is_py_file or is_init:
            continue
        mod_name = 'editboneconstraint.constraints.' + mod.split('.')[0]
        current_mod = importlib.import_module(mod_name)
        if hasattr(current_mod, 'exported_constraints'):
            for constraint in current_mod.exported_constraints:
                all_constraints[constraint.__name__] = constraint
    return OrderedDict(sorted(all_constraints.items()))


_all_constraints = _get_all_constraints_classes()
