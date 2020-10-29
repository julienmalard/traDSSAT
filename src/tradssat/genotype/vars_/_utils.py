def _gen_vars(dict_vars):
    vars_set = set()
    for name, d_var in dict_vars.items():
        vars_set.add(d_var['class'](name, **d_var['args']))

    return vars_set


def _return_vars(info_dict, rename=None, exclude=None):
    if exclude is None:
        exclude = []
    if rename is None:
        rename = {}

    info_dict_copy = info_dict.copy()
    for old, new in rename.items():
        info_dict_copy[new] = info_dict_copy.pop(old)

    d_vars = {vr: d_vr for vr, d_vr in info_dict_copy.items() if vr not in exclude}
    return _gen_vars(d_vars)
