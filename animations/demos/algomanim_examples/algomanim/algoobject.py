# pylint: disable=W0105, R0913
from abc import ABC
from manimlib import *
from algomanim.algoaction import AlgoTransform, AlgoSceneAction
from algomanim.metadata import LowerMetadata, attach_metadata


class AlgoObject(ABC):

    '''
    Base class for objects created with this library

    Note that the convention for creating a fn that results in an action_pair is:
    1. Create metadata if metadata was not previously initialised
    2. Create action pair
    3. Create LowerMetadata
    4. Add metadata if metadata is initialised in the fn
    '''

    def __init__(self, scene):
        super().__init__()
        # Every object is connected to a scene
        self.scene = scene
        # Every object has a grp
        self.grp = None
        # Custom texts associated with this obj
        self.text = {' ': Tex(' ')}
        # Optional to have a val
        self.val = None

    ''' Set obj position next to the given obj at vector side '''
    @attach_metadata
    def set_next_to(self, obj, vector, panel_name=None, specific_val=None,
                    metadata=None, animated=False, w_prev=False):
        # Create action pair
        action = AlgoSceneAction.create_static_action(self.grp.next_to, [obj.grp, vector])
        anim_action = self.scene.create_play_action(
            AlgoTransform(
                [obj],
                transform=lambda o: ApplyMethod(self.grp.next_to, o.grp, vector)
            ),
            w_prev=w_prev
        )

        action_pair = self.scene.add_action_pair(anim_action, action, animated=animated)

        # customise the value to save
        val_to_use = [self.val, obj.val] if specific_val is None else specific_val

        # Create LowerMetadata
        if panel_name is None:
            lower_meta = LowerMetadata.create(action_pair, val_to_use, show_in_panel=animated)
        else:
            # use the panel name
            lower_meta = LowerMetadata(meta_name=panel_name, action_pair=action_pair,
                                       val=val_to_use, show_in_panel=animated)
        metadata.add_lower(lower_meta)

    # Static function of set_relative_of to be executed later
    def static_set_relative_to(self, obj, vector):
        self.grp.move_to(obj.grp.get_center() + vector)

    ''' Set obj position relative to the given obj by a vector '''
    @attach_metadata
    def set_relative_to(self, obj, vector, metadata=None, animated=False, w_prev=False):
        # Create action pair
        action = AlgoSceneAction.create_static_action(self.static_set_relative_to, [obj, vector])
        anim_action = self.scene.create_play_action(
            AlgoTransform(
                [obj],
                transform=lambda o: ApplyMethod(self.grp.move_to, o.grp.get_center(), vector)
            ),
            w_prev=w_prev
        )

        action_pair = self.scene.add_action_pair(anim_action, action, animated=animated)
        # Create LowerMetadata
        lower_meta = LowerMetadata.create(action_pair, [self.val, obj.val], show_in_panel=animated)
        metadata.add_lower(lower_meta)

    # Static function of swap_with to be executed later
    def static_swap_with(self, obj):
        self_center = self.grp.get_center()
        obj_center = obj.grp.get_center()
        self.grp.move_to(obj_center)
        obj.grp.move_to(self_center)

    ''' Swap the positions of this obj and the given one '''
    @attach_metadata
    def swap_with(self, obj, metadata=None, animated=True, w_prev=False):
        # Create action pair
        anim_action1 = self.scene.create_play_action(
            AlgoTransform([self.grp, obj.grp], transform=CyclicReplace), w_prev=w_prev
        )
        anim_action2 = self.scene.create_play_action(
            AlgoTransform([obj.grp, self.grp], transform=CyclicReplace), w_prev=True
        )
        static_action1 = AlgoSceneAction.create_static_action(self.static_swap_with, [obj])
        static_action2 = AlgoSceneAction.create_empty_action()
        action_pair1 = self.scene.add_action_pair(anim_action1, static_action1, animated=animated)
        action_pair2 = self.scene.add_action_pair(anim_action2, static_action2, animated=animated)
        # Create LowerMetadata
        lower_meta1 = LowerMetadata.create(action_pair1, [self.val, obj.val])
        lower_meta2 = LowerMetadata.create(action_pair2, [self.val, obj.val])
        metadata.add_lower(lower_meta1)
        metadata.add_lower(lower_meta2)

    ''' Center object on screen '''
    @attach_metadata
    def center(self, metadata=None, animated=True, w_prev=False):
        # Create action pair
        anim_action = self.scene.create_play_action(
            AlgoTransform([self.grp], transform=lambda grp: \
                ApplyMethod(grp.move_to, ORIGIN + np.array([0, grp.get_center()[1], 0]))
            ),
            w_prev=w_prev
        )
        static_action = AlgoSceneAction.create_static_action(lambda grp: \
            grp.move_to(ORIGIN + np.array([0, grp.get_center()[1], 0])), args=[self.grp])
        action_pair = self.scene.add_action_pair(anim_action, static_action, animated=animated)
        # Create LowerMetadata
        lower_meta = LowerMetadata.create(action_pair, [self.val], show_in_panel=animated)
        metadata.add_lower(lower_meta)

    ''' Show object on screen '''
    @attach_metadata
    def show(self, metadata=None, animated=True, w_prev=False):
        # Create action pair
        anim_action = self.scene.create_play_action(
            AlgoTransform([self.grp], transform=FadeIn), w_prev=w_prev
        )
        static_action = AlgoSceneAction.create_static_action(self.scene.add, [self.grp])
        action_pair = self.scene.add_action_pair(anim_action, static_action, animated=animated)
        # Create LowerMetadata
        lower_meta = LowerMetadata.create(action_pair, [self.val], show_in_panel=animated)
        metadata.add_lower(lower_meta)

    ''' Hide object from screen '''
    @attach_metadata
    def hide(self, metadata=None, animated=True, w_prev=False):
        # Create action pair
        anim_action = self.scene.create_play_action(
            AlgoTransform([self.grp], transform=FadeOut), w_prev=w_prev
        )
        static_action = AlgoSceneAction.create_static_action(self.scene.remove, [self.grp])
        action_pair = self.scene.add_action_pair(anim_action, static_action, animated=animated)
        # Create LowerMetadata
        lower_meta = LowerMetadata.create(action_pair, [self.val], show_in_panel=animated)
        metadata.add_lower(lower_meta)

    @attach_metadata
    def hide_group(self, grp, metadata=None, animated=True, w_prev=False):
        # Create action pair
        anim_action = self.scene.create_play_action(
            AlgoTransform([grp], transform=FadeOut), w_prev=w_prev
        )
        static_action = AlgoSceneAction.create_static_action(self.scene.remove, [grp])
        action_pair = self.scene.add_action_pair(anim_action, static_action, animated=animated)

        # Create LowerMetadata
        lower_meta = LowerMetadata.create(action_pair, show_in_panel=animated)
        metadata.add_lower(lower_meta)

    ''' Add custom text associated to this obj '''
    @attach_metadata
    def add_text(self, text, key=' ', vector=UP, metadata=None, animated=False, w_prev=True):
        # If key exists, hide it
        if key in self.text:
            # Create hide action pair
            anim_action = self.scene.create_play_action(
                AlgoTransform([self.text[key]], transform=FadeOut), w_prev=w_prev
            )
            static_action = AlgoSceneAction.create_static_action(self.scene.remove,
                                                                 [self.text[key]])
            action_pair = self.scene.add_action_pair(anim_action, static_action, animated=animated)
            # Create hide LowerMetadata
            lower_meta = LowerMetadata('hide', action_pair, show_in_panel=False)
            metadata.add_lower(lower_meta)
        # Add new text object to text dictionary
        self.text[key] = self.scene.create_text(text)
        # Move it next to the obj with given vector
        anim_action = self.scene.create_play_action(
            AlgoTransform([self.text[key].next_to, self.grp, vector], transform=ApplyMethod)
        )
        static_action = AlgoSceneAction.create_static_action(self.text[key].next_to,
                                                             [self.grp, vector])
        action_pair = self.scene.add_action_pair(anim_action, static_action, animated=False)
        # Create set_next_to LowerMetadata
        lower_meta = LowerMetadata('set_next_to', action_pair, show_in_panel=False)
        metadata.add_lower(lower_meta)
        # Add text to screen
        anim_action = self.scene.create_play_action(
            AlgoTransform([self.text[key]], transform=Write)
        )
        static_action = AlgoSceneAction.create_static_action(self.scene.add, [self.text[key]])
        action_pair = self.scene.add_action_pair(anim_action, static_action, animated=animated)
        # Create add_text LowerMetadata
        lower_meta = LowerMetadata.create(action_pair)
        metadata.add_lower(lower_meta)

    ''' Remove text associated to this obj '''
    @attach_metadata
    def remove_text(self, key=None, metadata=None, animated=False, w_prev=True):
        # If no key is given, remove all text
        if not key:
            for k in list(self.text):
                # Create hide action pair
                anim_action = self.scene.create_play_action(
                    AlgoTransform([self.text[k]], transform=FadeOut), w_prev=w_prev
                )
                static_action = AlgoSceneAction.create_static_action(self.scene.remove,
                                                                     [self.text[k]])
                action_pair = self.scene.add_action_pair(anim_action, static_action,
                                                         animated=animated)
                # Create hide LowerMetadata
                lower_meta = LowerMetadata('remove_text', action_pair)
                metadata.add_lower(lower_meta)
                del self.text[k]
            # Reset text attribute
            self.text = {" ": TexMobject(" ")}
        # Else if key exists
        elif key in self.text:
            # Create hide action pair
            anim_action = self.scene.create_play_action(
                AlgoTransform([self.text[key]], transform=FadeOut), w_prev=w_prev
            )
            static_action = AlgoSceneAction.create_static_action(self.scene.remove,
                                                                 [self.text[key]])
            action_pair = self.scene.add_action_pair(anim_action, static_action,
                                                     animated=animated)
            # Create hide LowerMetadata
            lower_meta = LowerMetadata('remove_text', action_pair)
            metadata.add_lower(lower_meta)
            del self.text[key]

    ''' Moves the VGroup grp_start to the centre point of VGroup grp_end'''
    @staticmethod
    @attach_metadata
    def move_group_to_group(scene, grp_start, grp_end,
                            panel_name=None, specific_val=None, metadata=None, animated=True):
        move_pt = grp_end.get_center
        anim_action = scene.create_play_action(
            AlgoTransform(
                [grp_start],
                transform=lambda grp: ApplyMethod(grp.move_to, move_pt())
            )
        )
        static_action = AlgoSceneAction.create_static_action(
            function=lambda grp: AlgoTransform(grp.move_to, move_pt()),
            args=[grp_start]
        )
        action_pair = scene.add_action_pair(anim_action, static_action, animated=animated)

        if panel_name is None:
            lower_meta = LowerMetadata.create(action_pair, val=specific_val,
                                              show_in_panel=animated)
        else:
            lower_meta = LowerMetadata(panel_name, action_pair,
                                       specific_val, show_in_panel=animated)

        metadata.add_lower(lower_meta)

    ''' Returns a destination point for obj_to_move that is aligned vertically
     with all relative_objs, but still has the same y, z-coords. '''
    @staticmethod
    def center_pt(obj_to_move, relative_objs):
        new_x = sum([obj.grp.get_x() for obj in relative_objs]) / len(relative_objs)
        return np.array([new_x, obj_to_move.grp.get_y(), obj_to_move.grp.get_z()])

    ''' Returns the 2D centre point of all relative_objs.
     Assumes relative_objs are horizontally aligned. '''
    @staticmethod
    def center_up_pt(obj, relative_objs):
        new_x = sum([obj.grp.get_x() for obj in relative_objs]) / len(relative_objs)
        new_y = relative_objs[0].grp.get_y()
        return np.array([new_x, new_y, obj.grp.get_z()])

    ''' Aligns obj_to_move vertically with the midpoint of all relative_objs '''
    def center_x(self, relative_objs, metadata=None, animated=True):
        self.move_to_calculated_pt(relative_objs, pt_fn=AlgoObject.center_pt,
                                   metadata=metadata, animated=animated)

    ''' Moves obj_to_move to a point calculated by pt_fn, in relation to relative_objs '''
    @attach_metadata
    def move_to_calculated_pt(self, relative_objs, pt_fn,
                              panel_name=None, specific_val=None,
                              metadata=None, animated=True):
        anim_action = self.scene.create_play_action(
            AlgoTransform(
                [self],
                transform=lambda obj: ApplyMethod(obj.grp.move_to, pt_fn(obj, relative_objs))
            )
        )
        static_action = AlgoSceneAction.create_static_action(
            function=lambda obj: obj.grp.move_to(pt_fn(obj, relative_objs)),
            args=[self]
        )
        action_pair = self.scene.add_action_pair(anim_action, static_action, animated=animated)

        if panel_name is None:
            lower_meta = LowerMetadata.create(action_pair, specific_val,
                                              show_in_panel=animated)
        else:
            lower_meta = LowerMetadata(panel_name, action_pair,
                                       specific_val, show_in_panel=animated)

        metadata.add_lower(lower_meta)

    ''' Applies a function to a list of objects such that the animation takes place at the same time
    for all objects '''
    @staticmethod
    def loop_fn_w_prev(objs, fn_to_apply, animated, metadata, init_w_prev):
        first = True
        for obj in objs:
            if first:
                first = False
                fn_to_apply(obj, animated=animated, metadata=metadata, w_prev=init_w_prev)
            else:
                fn_to_apply(obj, animated=animated, metadata=metadata, w_prev=True)
