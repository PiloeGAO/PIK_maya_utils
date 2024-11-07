"""Context managers usefull in maya."""
from maya import cmds

class TempContext():
    """A context in which cmds operations are undone when the context is closed.

    Examples:
    >>> with TempContext():
    >>>     // Commands to run temporarily.
    >>>     pass
    """
    def __enter__(self):
        """Force the usage of undo/redo and start an undo chunk.
        """
        cmds.undoInfo(state=True)
        cmds.undoInfo(chunkName="TempChanges", infinity=True, openChunk=True)
        
    def __exit__(self, *_):
        """Close the undo chunk and undo it.
        """
        cmds.undoInfo(closeChunk=True)
        cmds.undo()