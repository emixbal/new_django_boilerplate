import imp

def load_module(name):
    """Load module using imp.find_module"""
    names = name.split(".")
    path = None
    for name in names:
        f, path, info = imp.find_module(name, path)
        path = [path]
    return imp.load_module(name, f, path[0], info)

# HOW TO USE
# constants = load_module("app.constants")
