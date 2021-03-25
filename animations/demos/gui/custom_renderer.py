#!/usr/bin/env python

"""
Interface to render default or customized manim animations
created via the Algomanim API into videos
"""

from argparse import Namespace
import manimlib.config
import manimlib.constants
from manimlib.extract_scene import get_scene_classes_from_module, get_scenes_to_render
from gui.video_quality import VideoQuality

# Modification of internal manim function using algomanim API
def custom_renderer(file_path, scene_name, video_quality,
                    post_customize_fns, post_config_settings):
    args = Namespace(color=post_config_settings.get('background_color'),
                     file=file_path,
                     file_name=None,
                     high_quality=video_quality == VideoQuality.high,
                     leave_progress_bars=False,
                     low_quality=video_quality == VideoQuality.low,
                     media_dir="./media/algomanim",
                     medium_quality=video_quality == VideoQuality.med,
                     preview=True,
                     quiet=False,
                     resolution=None,
                     save_as_gif=False,
                     save_last_frame=False,
                     save_pngs=False,
                     scene_names=[scene_name],
                     show_file_in_finder=False,
                     sound=False,
                     start_at_animation_number=None,
                     tex_dir=None,
                     transparent=False,
                     video_dir=None,
                     video_output_dir="./media/algomanim/videos",
                     write_all=False,
                     write_to_movie=False)
    config = manimlib.config.get_configuration(args)
    manimlib.constants.initialize_directories(config)

    module = config["module"]
    all_scene_classes = get_scene_classes_from_module(module)
    scene_class = get_scenes_to_render(all_scene_classes, config)[0]

    scene_kwargs = {
        key: config[key] for key in ["camera_config",
                                     "file_writer_config",
                                     "skip_animations",
                                     "start_at_animation_number",
                                     "end_at_animation_number",
                                     "leave_progress_bars",
                                     ]
    }

    scene_kwargs.update({
        'post_customize_fns': post_customize_fns,
        'post_config_settings': post_config_settings
    })

    return scene_class(**scene_kwargs)
