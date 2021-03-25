# pylint: disable=R0903
import inspect
from collections import Counter


def attach_metadata(func):
    def wrapped_func(*args, **kwargs):
        # retrieve metadata from arguments
        metadata = kwargs["metadata"] if "metadata" in kwargs else None

        # if metadata was not given in arguments, create it for the given function
        animated = kwargs["animated"] if "animated" in kwargs else True
        meta = Metadata(func.__name__, animated) if metadata is None else metadata

        if metadata is None:
            # set metadata argument if it was not previously set
            kwargs["metadata"] = meta

        # run function, get back result
        result = func(*args, **kwargs)

        # if metadata was created, add it to the scene
        if metadata is None and len(meta.children) > 0:
            args[0].scene.add_metadata(meta)

        return result
    return wrapped_func


class Metadata:

    '''
    Information corresponding to top-level operation on a AlgoManim data structure

    Args:
        meta_name (string): Function name corresponding to this operation
        animated (bool): Whether this operation is to be played with the previous one

    Attributes:
        fid (int): Id of this operation, indicating its position respective
            to other operations with the same name
        children (LowerMetadata[]): Information corresponding to the lower level functions
            associated with this operation
    '''

    counter = Counter()

    def __init__(self, meta_name, animated=True):
        self.meta_name = meta_name

        Metadata.counter[meta_name] += 1
        self.fid = Metadata.counter[meta_name]

        self.animated = animated

        self.children = []

    def add_lower(self, lowermeta):
        self.children.append(lowermeta)

    def get_all_action_pairs(self):
        return list(map(lambda lower: lower.action_pair, self.children))

    def desc(self, sep='\n'):
        return f'{self.meta_name}{sep}#{self.fid}'

    @staticmethod
    def reset_counter():
        Metadata.counter = Counter()

    def __str__(self):
        return f'Metadata(meta={self.meta_name}, fid={self.fid}' + \
            f', children=[{self.__print_children()}])'

    def __print_children(self):
        strings = []
        for i in self.children:
            strings.append(str(i) + ', ')
        return ''.join(strings)


class LowerMetadata:

    '''
    Information corresponding to lower-level operations nested in a Metadata

    Args:
        meta_name (string): Name of the Metadata that this is nested under
        action_pair (AlgoSceneActionPair): Animations corresponding to this operation
        val ([]): List of values affected by function
        show_in_panel: Whether this operation is shown in the GUI side panel
    '''

    def __init__(self, meta_name, action_pair, val=None, show_in_panel=True):
        if val is None:
            # default to empty list
            val = []
        else:
            val = list(filter(lambda v: v is not None, val))
        self.meta_name = meta_name
        self.action_pair = action_pair
        self.val = val
        self.show_in_panel = show_in_panel

    def __str__(self):
        return f'LowerMetadata(meta={self.meta_name}, val={self.val}' + \
            f', action_pair={self.action_pair})'

    @staticmethod
    def create(action_pair, val=None, show_in_panel=True):
        ''' Returns LowerMetadata with the name of the function that called this '''
        currframe = inspect.currentframe()
        return LowerMetadata(inspect.getouterframes(currframe, 2)[1][3],
                             action_pair, val, show_in_panel)
