from algomanim.empty_animation import is_empty_anim


# Formats text on animation blocks
def format_anim_block_str(metablock, sep='\n'):
    if is_empty_anim(metablock):
        return metablock.desc()

    # extract metadata from the block
    meta = metablock.metadata

    return f"{meta.meta_name}{sep}" \
           f"#{meta.fid}"


# Formats title of a customisation panel option
def format_customise_name(lower_meta):
    if lower_meta.val is None or not lower_meta.val:
        # no value to show
        return lower_meta.meta_name

    return f"{lower_meta.meta_name}: {lower_meta.val}"
