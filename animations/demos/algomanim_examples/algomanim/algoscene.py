# pylint: disable=R0914, W0122, W0105, R0904
import ast
import inspect
import re
from collections import namedtuple
from manimlib import *
from algomanim.settings import DEFAULT_SETTINGS
from algomanim.algoaction import AlgoTransform, AlgoSceneAction, AlgoSceneActionPair, \
    fade_in_transform, fade_out_transform
from .animation_block import AnimationBlock
from .metadata_block import MetadataBlock
from .metadata import Metadata, LowerMetadata


# ----- Utility funnctions used for show_code ----- #

Import = namedtuple("Import", ["module", "name", "alias"])

def get_imports(path):
    with open(path) as path_file:
        root = ast.parse(path_file.read(), path)

    for node in ast.iter_child_nodes(root):
        if isinstance(node, ast.Import):
            module = []
        elif isinstance(node, ast.ImportFrom):
            module = node.module.split('.')
        else:
            continue

        for node_name in node.names:
            yield Import(module, node_name.name.split('.'), node_name.asname)

def remove_fn_flags(line):
    return re.sub(r'(?<=\()([^,]*)((,[^,=]*)*)(,[^,]*=.*)(?=\))', r'\1\2', line)

def is_continuation_of(line):
    return line.rstrip() and line.rstrip()[-1] == '\\'

# ------------- AlgoScene functions ------------- #

class AlgoScene(Scene):

    '''
    Superclass of all scenes using the AlgoManim library

    Args:
        **kwargs: Variable arguments passed to the Manim Scene superclass
            Receives post_customize_fns and post_config_settings which are set from the GUI

    Attributes:
        settings (dict): General scene settings to be configured in preconfig()
        save_mobjects (Mobject[]): Reobtain objects removed by certain animations
        algo_objs (AlgoObject[]): Tracker for all items in the scene
        post_customize_fns (function[]): GUI-generated animation customizations
        post_config_settings (dict): GUI-generated configuration settings
        action_pairs (AlgoSceneActionPair[]): Chronological list of scene actions
        anim_blocks (AnimationBlock[]): action_pairs organized into AnimationBlocks
        meta_trees (Metadata[]): Information corresponding to each action_pair
        metadata_block (MetadataBlock[]): meta_trees organized into MetadataBlocks
    '''

    def __init__(self, **kwargs):
        self.settings = DEFAULT_SETTINGS.copy()
        self.save_mobjects = None
        self.algo_objs = []
        self.kwargs = kwargs
        self.post_customize_fns = kwargs.get('post_customize_fns', [])
        self.post_config_settings = kwargs.get('post_config_settings', {})
        self.action_pairs = []
        self.anim_blocks = []
        self.meta_trees = []
        self.metadata_blocks = []

        Scene.__init__(self, **kwargs)

    # ---------- Algorithm default creation ----------- #

    def algo(self):
        ''' For users to overwrite '''

    # ---------- Customizability / Pinning utilities ----------- #

    def preconfig(self, settings):
        ''' For users to overwrite '''

    def customize(self):
        ''' For users to overwrite '''

    def add_transform(self, index=None, custom_transform=None, args=[], metadata=None):  # pylint: disable=W0102
        ''' Adds a custom Manim animation to a particular action_pair '''
        anim_action = self.create_play_action(AlgoTransform(args, transform=custom_transform))
        action_pair = AlgoSceneActionPair(anim_action, anim_action)
        self.insert_action_pair(action_pair, index)

        if metadata is None:
            curr_metadata = Metadata('custom')
            lower_meta = LowerMetadata('custom', action_pair)
            curr_metadata.add_lower(lower_meta)

            self.add_metadata(curr_metadata)
        else:
            self.add_metadata(metadata)

    def insert_pin(self, desc, *args):
        '''
        Insert a pin in algo() so that specific action_pairs can be found and customized
        either in customize() or the GUI
        '''
        empty_action = AlgoSceneAction.create_empty_action(list(args))
        empty_pair = self.add_action_pair(empty_action)

        lower_meta = LowerMetadata(desc, empty_pair)
        metadata = Metadata(desc)
        metadata.add_lower(lower_meta)

        self.add_metadata(metadata)

    def find_pin(self, desc):
        action_pairs = self.find_action_pairs(desc)
        return action_pairs

    def find_action_pairs(self, metadata_name, occurence=None, lower_level=None,
                          w_children=True):
        action_pairs = []
        for meta_tree in self.meta_trees:
            if metadata_name == meta_tree.meta_name and\
                    (occurence is None or occurence == meta_tree.fid):
                if lower_level:
                    for lower in meta_tree.children:
                        if lower_level == lower.meta_name:
                            action_pairs.append(lower.action_pair)
                elif w_children:
                    # if w_children is True, add all action_pairs of this metadata
                    for action_pair in meta_tree.get_all_action_pairs():
                        action_pairs.append(action_pair)
                else:
                    # else, add only the first action_pair of this metadata
                    action_pairs.append(meta_tree.get_all_action_pairs()[0])
        return action_pairs

    # ----------- AlgoObject customisability ---------

    def chain_pin_highlight(self, pin_str, highlight_color=None, dehighlight=True):
        '''
        Adds highlight animations to the animations immediately after the pins
        insert_pin() must've been given an AlgoNode
        Consult algomanim_examples/binarytreesort.py for an example
        '''

        pins = self.find_pin(pin_str)
        prev_node = None

        highlight_color = highlight_color if highlight_color else self.settings['highlight_color']

        node_highlight = lambda node: \
            ApplyMethod(node.node.set_fill, highlight_color)
        node_dehighlight = lambda node: \
            ApplyMethod(node.node.set_fill, self.settings['node_color'])
        for pin in pins:
            if len(pin.get_args()) > 0:
                node = pin.get_args()[0]
                self.add_transform(pin.get_index(), node_highlight, [node])
                if dehighlight and prev_node is not None:
                    self.add_transform(pin.get_index() + 1, node_dehighlight, [prev_node])
                prev_node = node

    def chain_pin_highlight_line(self, pin_str, highlight_color=None, dehighlight=True):
        ''' chain_pin_highlight of lines between nodes (graphs/trees) '''
        pins = self.find_pin(pin_str)
        prev_node = None
        prev_edge = None

        highlight_color = highlight_color if highlight_color else self.settings['highlight_color']

        line_highlight = lambda node, edge: \
            ApplyMethod(node.lines[edge][0].set_stroke, highlight_color)
        line_dehighlight = lambda node, edge: \
            ApplyMethod(node.lines[edge][0].set_stroke, self.settings['line_color'])
        for pin in pins:
            node = pin.get_args()[0]
            edge = pin.get_args()[1]
            self.add_transform(pin.get_index(), line_highlight, [node, edge])
            if dehighlight and prev_node is not None:
                self.add_transform(pin.get_index() + 1, line_dehighlight, [prev_node, prev_edge])
                prev_node = node
                prev_edge = edge

    def chain_pin_dehighlight_line(self, pin_str):
        pins = self.find_pin(pin_str)

        line_dehighlight = lambda node, edge: \
            ApplyMethod(node.lines[edge][0].set_stroke, self.settings['line_color'])
        for pin in pins:
            node = pin.get_args()[0]
            edge = pin.get_args()[1]
            self.add_transform(pin.get_index(), line_dehighlight, [node, edge])


    # ------------ Text customizability --------------

    def add_text(self, text, index=0, position=ORIGIN):
        '''
        Add a text object and the Write transform
        Returns the created text object
        '''
        assert index is not None

        text = self.create_text(text)
        text.shift(position)
        transform = lambda: Write(text)
        self.add_transform(index, transform)
        return text

    def create_text(self, text_string, for_node=False):
        '''
        Factory method to return a Text-kind object depending on the current configuration.
        Defaults to the manim-configured default font if configuration does not describe
        a valid installed font.

        Args:
            text_string (str): The text to create
            for_node (bool): To use the node font configuration
        '''
        font_key = 'node_font' if for_node else 'text_font'
        color_key = 'node_font_color' if for_node else 'text_font_color'
        font = self.settings[font_key].lower()
        font_color = self.settings[color_key]
        if font == 'latex':
            return Text(text_string, color=font_color)
        return Text(text_string, color=font_color, font=font)

    def change_text(self, new_text_string, old_text_object=None, index=0, position=ORIGIN):
        '''
        Edit existing text objects via Manim's ReplacementTransform
        Requires the previous text object to be edited
        Returns the replacement text object
        '''
        assert index is not None

        if old_text_object is None:
            return self.add_text(new_text_string, index=index, position=position)
        position = old_text_object.get_center()
        new_text_object = self.create_text(new_text_string)
        new_text_object.shift(position)

        # Create the transform to be run at that point
        transform = lambda old_text, new_text: \
            [FadeOut(old_text), ReplacementTransform(old_text, new_text)]
        self.add_transform(index, transform, args=[old_text_object, new_text_object])
        return new_text_object

    def remove_text(self, old_text_object, index=None):
        ''' FadeOut an existing text object '''
        transform = lambda: FadeOut(old_text_object)
        self.add_transform(index, transform)

    # ------------ Scene customizability --------------

    def add_complexity_analysis_line(self, linenum, position=2 * DOWN, custom_text=None):
        '''
        Displays the number of times a line is called
        Note that the linenum inputted should be the linenum in display_sourcecode,
        not the linenum in algo(), so this can only be used if show_anim is on
        '''
        codeindex_pins = self.find_pin('__codeindex__')
        relevant_pins = list(filter(lambda pin: pin.get_args()[0] == linenum, codeindex_pins))
        old_text = None
        for i, pin in enumerate(relevant_pins):
            index = pin.get_index()
            new_text = (custom_text + f'{i+1}') \
                if custom_text \
                   else f'Line {linenum} called: {i + 1} times'
            old_text = self.change_text(new_text, old_text, index=index, position=position)

    def add_complexity_analysis_fn(self, fn_method, position=2 * DOWN, custom_text=None):
        '''
        Displays the number of times a fn_method is called - specified by a pin or metadata
        '''
        action_pairs = self.find_action_pairs(metadata_name=fn_method, w_children=False)
        old_text = None
        for i, pin in enumerate(action_pairs):
            index = pin.get_index()
            new_text = (custom_text+f'{i+1}') \
                if custom_text \
                else f'{fn_method} called: {i + 1} times'
            old_text = self.change_text(new_text, old_text, index=index, position=position)

    def shift_scene(self, vector, metadata=None, w_prev=False):
        ''' Shifts all TRACKED objects in the scene by some vector '''
        first = True
        for algo_obj in self.algo_objs:
            # Shift all items UP
            if first:
                algo_obj.set_next_to(algo_obj, vector, metadata=metadata, animated=True,
                    w_prev=w_prev)
                first = False
            else:
                algo_obj.set_next_to(algo_obj, vector, metadata=metadata, animated=True,
                    w_prev=True)

    def skip(self, start, end=None):
        if end is None:
            end = len(self.action_pairs)

        for action_pair in self.action_pairs[start:end]:
            action_pair.skip()

    def fast_forward(self, start, end=None, speed_up=2):
        if end is None:
            end = len(self.action_pairs)

        for action_pair in self.action_pairs[start:end]:
            action_pair.fast_forward(speed_up)

    def add_slide(self, text, index, text_position=ORIGIN, duration=1):
        self.add_fade_out_all(index)
        text_anim = self.add_text(text, index + 1, position=text_position)
        self.add_wait(index + 2, wait_time=duration)
        self.remove_text(text_anim, index + 3)
        self.add_fade_in_all(index + 4)

    def add_fade_out_all(self, index):
        anim_action = self.create_play_action(AlgoTransform([self], transform=fade_out_transform))
        action_pair = AlgoSceneActionPair(anim_action, anim_action)
        self.insert_action_pair(action_pair, index)

        curr_metadata = Metadata('fade_out')
        lower_meta = LowerMetadata('fade_out', action_pair)
        curr_metadata.add_lower(lower_meta)

        self.add_metadata(curr_metadata)

    def add_fade_in_all(self, index):
        anim_action = self.create_play_action(AlgoTransform([self], transform=fade_in_transform))
        action_pair = AlgoSceneActionPair(anim_action, anim_action)
        self.insert_action_pair(action_pair, index)

        curr_metadata = Metadata('fade_in')
        lower_meta = LowerMetadata('fade_in', action_pair)
        curr_metadata.add_lower(lower_meta)

        self.add_metadata(curr_metadata)

    def add_wait(self, index, wait_time=1):
        anim_action = AlgoSceneAction(self.wait, AlgoTransform([wait_time]), can_set_runtime=True,
            is_wait=True)
        # Using a dummy function to skip wait
        static_action = AlgoSceneAction.create_empty_action()
        action_pair = AlgoSceneActionPair(anim_action, static_action)
        self.insert_action_pair(action_pair, index)

        curr_metadata = Metadata('wait')
        lower_meta = LowerMetadata('wait', action_pair)
        curr_metadata.add_lower(lower_meta)

        self.add_metadata(curr_metadata)

    def add_clear(self, index):
        action_pair = AlgoSceneAction.create_static_action(self.clear)
        self.insert_action_pair(AlgoSceneActionPair(action_pair), index)

        curr_metadata = Metadata('clear')
        lower_meta = LowerMetadata('clear', action_pair)
        curr_metadata.add_lower(lower_meta)

        self.add_metadata(curr_metadata)

    # ----- Data Structure utilities -------

    def track_algoitem(self, algo_item):
        ''' Add item so they can subscribe themselves to scene transformations like Shifts '''
        self.algo_objs.append(algo_item)

    def untrack_algoitem(self, algo_item):
        if algo_item in self.algo_objs:
            self.algo_objs.remove(algo_item)

    def create_play_action(self, transform, w_prev=False):
        return AlgoSceneAction(
            self.play, transform,
            w_prev=w_prev, can_set_runtime=True
        )

    def add_action_pair(self, anim_action, static_action=None, animated=True, index=None):
        pair = AlgoSceneActionPair(anim_action, static_action,
                                   run_time=None if animated else 0)
        self.insert_action_pair(pair, index)
        return pair

    def insert_action_pair(self, action_pair, index=None):
        if index is not None:
            self.push_back_action_pair_indices(index)
        else:
            index = len(self.action_pairs)

        action_pair.attach_index(index)
        self.action_pairs.insert(index, action_pair)

    def push_back_action_pair_indices(self, index):
        for action_pair in self.action_pairs[index:]:
            action_pair.attach_index(action_pair.get_index() + 1)

    def add_static(self, index, static_fn, args=[], metadata=None):  # pylint: disable=W0102
        static_action = AlgoSceneAction.create_static_action(static_fn, args)
        action_pair = AlgoSceneActionPair(static_action, static_action)
        self.insert_action_pair(action_pair, index)

        if metadata is None:
            curr_metadata = Metadata('custom')
            lower_meta = LowerMetadata('custom', action_pair)
            curr_metadata.add_lower(lower_meta)
            self.add_metadata(curr_metadata)
        else:
            self.add_metadata(metadata)

    def add_metadata(self, metadata):
        self.meta_trees.append(metadata)

    # ------------ AlgoScene Internal Wiring --------------
    def is_show_code(self):
        return self.settings['show_code']

    def algo_codeanim(self):
        ''' For animation of code alongside data structure '''
        # import necessary modules
        file_path = inspect.getsourcefile(self.algo)
        imports = get_imports(file_path)
        for imp in imports:
            module = '.'.join(imp.module)
            names = ','.join(imp.name)
            if imp.module:
                exec(f'from {module} import {names}')
            else:
                exec(f'import {names}')
        # get algo source lines
        sourcelines, _ = inspect.getsourcelines(self.algo)

        display_sourcelines = []
        exec_sourcelines = []

        # get redundant spacing for first code line that is not def
        redundant_space_count = len(sourcelines[1]) - len(sourcelines[1].lstrip())
        # insert pin at every alternate source line
        for i, line in enumerate(sourcelines):
            front_space_count = len(line) - len(line.lstrip())

            # Do not execute first def line, empty line, or comment
            if i == 0 or not line.strip() or line[front_space_count] == '#':
                continue

            line_tab = ' ' * (front_space_count - redundant_space_count)

            # If inner fn, add global declaration
            if line[front_space_count:].split()[0] == 'def':
                inner_fn_name = line[front_space_count:].split()[1]
                inner_fn_name = inner_fn_name.split('(')[0]
                exec_sourcelines.append(f'{line_tab}global {inner_fn_name}\n')
                display_line = remove_fn_flags(line)
                display_sourcelines.append(display_line)

            # Insert pin if line is not a pin, line is not a continuation, and not an else statement
            elif 'insert_pin' not in line \
                 and not is_continuation_of(sourcelines[i-1]) \
                 and 'else' not in line:
                pin = f'{line_tab}self.insert_pin(\'__codeindex__\', {len(display_sourcelines)})\n'
                exec_sourcelines.append(pin)
                # Remove flags and add display code
                display_line = remove_fn_flags(line)
                display_sourcelines.append(display_line)

            # Add code to be executed
            exec_sourcelines.append(line[redundant_space_count:])

        # insert pin at the beginning to show all code
        display_sourcecode = [line.replace('\n', '') for line in display_sourcelines]
        pin_sourcecode = f'self.insert_pin(\'__sourcecode__\', {display_sourcecode})\n'
        exec_sourcelines.insert(0, pin_sourcecode)

        # get modified source code and execute
        exec_sourcecode = ''.join(exec_sourcelines)
        print(exec_sourcecode)
        exec(f'{exec_sourcecode}')

    def algo_construct(self):
        # Add parallel code animation
        if self.is_show_code():
            self.algo_codeanim()
        # Run normal algo animation
        else:
            self.algo()

    def customize_codeanim(self):
        # ----- helper static fns ----- #
        def zoom_out():
            new_center = self.camera_frame.get_right()
            self.camera_frame.set_width(self.camera_frame.get_width() * 2)
            self.camera_frame.move_to(new_center)

        def show_sourcecode(textobjs, num_spaces):
            if not textobjs or not num_spaces:
                return
            # move first line to the desired position
            mid_index = len(textobjs)/2
            textobjs[0].move_to(self.camera_frame.get_center() + RIGHT*0.2
                                + RIGHT*textobjs[0].get_width()/2)
            textobjs[0].shift(mid_index * UP * 0.7)
            # arrange text group downwards aligned to the left
            text = VGroup(*textobjs)
            text.arrange(DOWN, center=False, aligned_edge=LEFT)
            # add tabbing to shown text
            for i, textobj in enumerate(textobjs):
                textobj.shift(num_spaces[i] * RIGHT)
            # add text
            self.add(text)

        def add_arrow_beside(arrow, textobj):
            arrow.next_to(textobj, LEFT)
            self.add(arrow)
        # ----------------------------- #

        # zoom camera out
        self.add_static(0, zoom_out)

        # show source code text
        sourcecode_pin = self.find_pin('__sourcecode__')[0]
        index = sourcecode_pin.get_index()
        sourcecode = sourcecode_pin.get_args()[0]
        num_spaces = [len(line) - len(line.lstrip(' ')) for line in sourcecode]
        min_spaces = min([n for n in num_spaces if n != 0])
        num_spaces = [(n / min_spaces - 1) for n in num_spaces]
        textobjs = [Text(line.lstrip(), font='Inconsolata') for line in sourcecode]
        self.add_static(index, show_sourcecode, [textobjs, num_spaces])

        # move arrow to which code line is executed
        arrow = Arrow(ORIGIN, RIGHT)
        self.add_static(index+1, add_arrow_beside, [arrow, textobjs[0]])
        codeindex_pins = self.find_pin('__codeindex__')
        for pin in codeindex_pins:
            index = pin.get_index()
            codeindex = pin.get_args()[0]
            self.add_transform(index, ApplyMethod, args=[arrow.next_to,
                                                         textobjs[codeindex], LEFT])

    def customize_construct(self):
        # Add customisation needed for parallel code anim
        if self.is_show_code():
            self.customize_codeanim()
        # Run user-defined customize fn
        self.customize()

    def post_config(self, settings):
        settings.update(self.post_config_settings)

    def create_animation_blocks(self, action_pairs, anim_blocks): # pylint: disable=R0201
        ''' Convert action_pairs into anim_blocks '''
        start_time = 0
        for action_pair in action_pairs:
            action = action_pair.curr_action()
            if action.w_prev and anim_blocks and anim_blocks[-1].act() == action.act:
                # anim_blocks should have at least 1 element
                # if action is supposed to be executed with previous action and
                # act function is the same as that of current block, bundle actions
                # together
                anim_blocks[-1].add_action_pair(action_pair)
            else:
                # else, create new Animation Block
                anim_blocks.append(AnimationBlock([action_pair], start_time))
                start_time += anim_blocks[-1].runtime_val()

            # attach block to action pair so that time data can be
            # extracted later to be used in GUI
            action_pair.attach_block(anim_blocks[-1])

    def create_metadata_blocks(self):
        self.metadata_blocks = []

        for tree in self.meta_trees:
            action_pairs = tree.get_all_action_pairs()

            blocks = {action_pair.get_block() for action_pair in action_pairs}
            if not blocks:
                # metadata has no action pairs attached to it
                continue

            start_time = min(map(lambda block: block.start_time, blocks))
            end_time = max(map(lambda block: block.start_time + block.runtime_val(), blocks))

            runtime = end_time - start_time

            self.metadata_blocks.append(
                MetadataBlock(tree, action_pairs, start_time, runtime)
            )

        # some metadata might be added out of order, sort the blocks by start_time
        self.metadata_blocks.sort(key=lambda meta_block: meta_block.start_time)

    def execute_action_pairs(self, action_pairs, anim_blocks):
        # wait action is required at the end if last animation is not
        # a play/wait, else the last animation will not be rendered

        if action_pairs:
            # action_pairs should not be empty
            last_action_pair = action_pairs[-1]
            last_act = last_action_pair.act()
            if not str(last_act).startswith('<bound method Scene.handle_play_like_call'): # pylint: disable=W0143
                # wait action is required at the end if last animation is not
                # a play/wait, else the last animation will not be rendered
                self.add_wait(len(self.action_pairs))

        # attach indexes to action_pair to be used in GUI
        # customizations
        for (i, action_pair) in enumerate(action_pairs):
            action_pair.attach_index(i)

        # run post customize functions from the GUI
        for post_customize in self.post_customize_fns:
            post_customize(self)

        # bundle animations together according to time
        self.create_animation_blocks(action_pairs, anim_blocks)

        # and run them
        for anim_block in self.anim_blocks:
            anim_block.run()

    def construct(self):
        ''' Run the pipeline needed for the animations '''
        Metadata.reset_counter()
        self.preconfig(self.settings)
        self.post_config(self.settings)

        self.algo_construct()
        self.customize_construct()

        self.execute_action_pairs(self.action_pairs, self.anim_blocks)
        self.create_metadata_blocks()
