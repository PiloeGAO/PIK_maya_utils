name = "PIK_maya_utils"

version = "0.0.1"

authors = [
    "Léo Depoix",
]

description = \
    """
    Utilies for Autodesk Maya 2025+.
    """

requires = [
    "maya-2025+",
    "python-3+",
]

uuid = "piktura.maya_utils"

build_command = 'python {root}/build.py {install}'

def commands():
    env.PYTHONPATH.append("{root}/python")
