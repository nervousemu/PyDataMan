def str2bool(arg):  # "true"
    return str(arg).lower() in ["true", 1, "1", "ok"]


def bool2str(arg):
    if arg:
        return "True"
    else:
        return "False"
