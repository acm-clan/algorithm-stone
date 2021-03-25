class AnimationBlock:

    '''
    Stores a list of related AlgoActionPairs running concurrently

    Args:
        action_pairs (AlgoSceneActionPairs[])
        start_time (float): Point of time in the AlgoScene at which this block runs
    '''

    def __init__(self, action_pairs, start_time):
        self.action_pairs = action_pairs
        self.start_time = start_time

    def first_pair(self):
        return self.action_pairs[0]

    def act(self):
        return self.first_pair().act()

    def runtime_val(self):
        return self.first_pair().get_runtime_val()

    def add_action_pair(self, action_pair):
        self.action_pairs.append(action_pair)

    def is_action_pair_in(self, action_pair):
        return action_pair in self.action_pairs

    def run(self):
        # extract act and runtime from first pair
        first_pair = self.first_pair()
        act = first_pair.act()
        run_time = first_pair.get_runtime()
        act_can_set_runtime = first_pair.curr_action().can_set_runtime

        # collect args list recursively for all pairs in this block
        args = []
        for action_pair in self.action_pairs:
            result = action_pair.run()
            if isinstance(result, list):
                # if transform in action_pair is simply a list of arguments,
                # a list is returned which needs to be concatenated
                for arg in result:
                    args.append(arg)
            else:
                args.append(result)

        if run_time is None or not act_can_set_runtime:
            act(*args)
        else:
            if first_pair.curr_action().is_wait:
                # self.wait
                args[0] = run_time
            else:
                act(*args, run_time=run_time)
