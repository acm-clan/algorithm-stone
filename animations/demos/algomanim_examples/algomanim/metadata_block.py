class MetadataBlock:

    '''
    List of Metadata corresponding to a AnimationBlock

    Args:
        metadata (Metadata[]): List of Metadata corresponding to the animations of the block
        action_pairs (AlgoSceneActionPairs[])
        start_time (float)
        run_time (float): Total runtime of all the animations in the block
    '''

    def __init__(self, metadata, action_pairs, start_time, runtime):
        self.metadata = metadata
        self.action_pairs = action_pairs
        self.start_time = start_time
        self.runtime = runtime

    def desc(self, sep='\n'):
        ''' Get all relevant animation information stored in the action pair metadata '''
        return self.metadata.desc(sep=sep)

    def start_position(self):
        return self.start_time * 1000

    def end_position(self):
        return (self.start_time + self.runtime) * 1000

    def start_index(self):
        assert len(self.action_pairs) > 0
        return self.action_pairs[0].get_index()

    def end_index(self):
        assert len(self.action_pairs) > 0
        return self.action_pairs[-1].get_index()

    def can_set_runtime(self):
        return any([ap.can_set_runtime() for ap in self.action_pairs])
