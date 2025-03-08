import struct
from io import BytesIO
from math import prod
from PySide6 import QtCore, QtGui, QtWidgets
from PIL import Image, ImageOps
from PIL.ImageQt import ImageQt
from mnllib.bis import decompress

SIZING_TABLE = [[(8, 8), (16, 16), (32, 32), (64, 64)], [(16, 8), (32, 8), (32, 16), (64, 32)], [(8, 16), (8, 32), (16, 32), (32, 64)]]

def create_MObj_sprite(table_offsets, overlay, MObj_file, group_num, anim_num, lang):
    if isinstance(anim_num, int):
        anim_list = [anim_num]
    else:
        anim_list = [*anim_num]
    return create_XObj_sprite(table_offsets, overlay, overlay, MObj_file, group_num, anim_list, lang)

create_FObj_sprite = create_MObj_sprite
create_EObj_sprite = create_MObj_sprite

def create_BObjUI_sprite(table_offsets, file_data_overlay, group_data_overlay, MObj_file, group_num, anim_num, lang):
    if isinstance(anim_num, int):
        anim_list = [anim_num]
    else:
        anim_list = [*anim_num]
    return create_XObj_sprite(table_offsets, file_data_overlay, group_data_overlay, MObj_file, group_num, anim_list, lang)

def create_XObj_sprite(table_offsets, file_data_overlay, group_data_overlay, XObj_file, group_num, anim_list, lang):
    file_data_overlay = BytesIO(file_data_overlay)
    group_data_overlay = BytesIO(group_data_overlay)
    XObj_file = BytesIO(XObj_file)

    # ==================================================================
    # start reading the data

    group_data_overlay.seek(table_offsets[1] + (group_num * 10)) # get sprite group data
    anim_id, graph_id, pal_gid, use_lang = struct.unpack('<3H2xH', group_data_overlay.read(10))

    if use_lang & 1 != 0: # check if current sprite group uses languages
        group_data_overlay.seek(table_offsets[1] + ((group_num + lang) * 10)) # get sprite group data again
        anim_id, graph_id, pal_gid = struct.unpack('<3H', group_data_overlay.read(6))
    
    group_data_overlay.seek(table_offsets[2] + (pal_gid * 4))
    pal_id = int.from_bytes(group_data_overlay.read(2), "little")

    file_data_overlay.seek(table_offsets[0] + (anim_id * 4))
    XObj_file.seek(int.from_bytes(file_data_overlay.read(4), "little"))
    animation_file = BytesIO(decompress(XObj_file))

    file_data_overlay.seek(table_offsets[0] + (graph_id * 4))
    XObj_file.seek(int.from_bytes(file_data_overlay.read(4), "little"))
    graphics_buffer = BytesIO(decompress(XObj_file))

    file_data_overlay.seek(table_offsets[0] + (pal_id * 4))
    XObj_file.seek(int.from_bytes(file_data_overlay.read(4), "little"))
    palette_file_size = int.from_bytes(XObj_file.read(4), "little")
    palette_file = define_palette(struct.unpack(f'<{palette_file_size // 2}H', XObj_file.read(palette_file_size)))

    # ==================================================================
    # start interpreting the data

    _settings_byte, anims_table, parts_table, tex_shift, graph_offset_table = struct.unpack('<2xBx2I9xB2xI', animation_file.read(0x1C))
    sprite_mode = _settings_byte & 3
    swizzle_flag = (_settings_byte >> 3) & 1 == 0

    img = Image.new("RGBA", (256, 256))

    for i in range(len(anim_list)):
        anim_num = anim_list[i]

        animation_file.seek(anims_table + (anim_num * 8))
        frame_offset = int.from_bytes(animation_file.read(2), "little")

        animation_file.seek(frame_offset)
        part_list_offset, part_amt = struct.unpack('<HxB', animation_file.read(4))

        # ==================================================================
        # start assembling the sprite

        if part_amt == 0 and len(anim_list) == 1:
            return QtGui.QPixmap(QtGui.QImage(ImageQt(Image.new("RGBA", (16, 16)))))

        for i in reversed(range(part_amt)):
            animation_file.seek(parts_table + ((part_list_offset + i) * 8))
            oam_settings, part_x, part_y = struct.unpack('<I2h', animation_file.read(8))

            part_xy = SIZING_TABLE[(oam_settings >> 6) & 0b11][(oam_settings >> 10) & 0b11]

            pal_shift = (oam_settings >> 14) & 0b1111

            animation_file.seek(graph_offset_table + ((part_list_offset + i) * 2))
            graphics_buffer.seek((int.from_bytes(animation_file.read(2), "little") << tex_shift) + 4)
            buffer_in = graphics_buffer.read(prod(part_xy))

            img_part = create_sprite_part(
                buffer_in,
                palette_file,
                part_xy,
                sprite_mode,
                pal_shift,
                swizzle_flag
            )

            x_flip = (oam_settings >> 8) & 1 != 0
            y_flip = (oam_settings >> 9) & 1 != 0

            if x_flip:
                img_part = ImageOps.mirror(img_part)
            if y_flip:
                img_part = ImageOps.flip(img_part)

            img.paste(img_part, (part_x - (part_xy[0] // 2) + 128, part_y - (part_xy[1] // 2) + 128), img_part)
    
    img = img.crop(img.getbbox())

    return QtGui.QPixmap(QtGui.QImage(ImageQt(img)))

def define_palette(current_pal):
    out_pal = []
    for color_raw in current_pal:
        red = (color_raw & 0x1F) << 3
        green = (color_raw >> 5 & 0x1F) << 3
        blue = (color_raw >> 10 & 0x1F) << 3
        out_pal.append((red, green, blue))
    return out_pal

def create_sprite_part(buffer_in, current_pal, part_xy, sprite_mode, pal_shift, swizzle, transparent_flag = True):
    pal_shift *= 16
    if (swizzle):
        part_size = 8 * 8
        tiles = (part_xy[0] * part_xy[1]) // 64
        tile_x, tile_y = 8, 8
    else:
        part_size = part_xy[0] * part_xy[1]
        tile_x, tile_y = part_xy[0], part_xy[1]
        tiles = 1
    img_out = Image.new("RGBA", (part_xy[0], part_xy[1]))
    for t in range(tiles):
        buffer_out = bytearray()
        match (sprite_mode):
            case 0:
                # 8bpp bitmap
                for i in range(part_size):
                    current_pixel = buffer_in[(t * 64) + i]
                    if current_pixel + pal_shift < len(current_pal):
                        buffer_out.extend(current_pal[current_pixel + pal_shift])
                    else:
                        buffer_out.extend([0, 0, 0])
                    # transparency
                    if transparent_flag:
                        if (current_pixel == 0): buffer_out.append(0x00)
                        else: buffer_out.append(0xFF)
                    else:
                        buffer_out.append(0xFF)
            case 1:
                # AI35
                for i in range(part_size):
                    current_pixel = buffer_in[(t * 64) + i] & 0b11111
                    if current_pixel + pal_shift < len(current_pal):
                        buffer_out.extend(current_pal[current_pixel + pal_shift])
                    else:
                        buffer_out.extend([0, 0, 0])
                    # transparency
                    if transparent_flag:
                        alpha = ceil(0xFF * ((buffer_in[(t * 64) + i] >> 5) / 7))
                        buffer_out.append(alpha)
                    else:
                        buffer_out.append(0xFF)
            case 2:
                # AI53
                for i in range(part_size):
                    current_pixel = buffer_in[(t * 64) + i] & 0b111
                    if current_pixel + pal_shift < len(current_pal):
                        buffer_out.extend(current_pal[current_pixel + pal_shift])
                    else:
                        buffer_out.extend([0, 0, 0])
                    # transparency
                    if transparent_flag:
                        alpha = buffer_in[(t * 64) + i] >> 3
                        alpha = (alpha << 3) | (alpha >> 2)
                        buffer_out.append(alpha)
                    else:
                        buffer_out.append(0xFF)
            case 3:
                # 4bpp bitmap
                for i in range(part_size):
                    current_pixel = (buffer_in[((t * 64) + i) // 2] >> ((i % 2) * 4)) & 0b1111
                    if current_pixel + pal_shift < len(current_pal):
                        buffer_out.extend(current_pal[current_pixel + pal_shift])
                    else:
                        buffer_out.extend([0, 0, 0])
                    # transparency
                    if transparent_flag:
                        if (current_pixel == 0): buffer_out.append(0x00)
                        else: buffer_out.append(0xFF)
                    else:
                        buffer_out.append(0xFF)
        # swizzle (if swizzle is disabled, x and y offset will always just be 0 and the image will display normally)
        x = (t % (part_xy[0] // tile_x)) * 8
        y = (t // (part_xy[0] // tile_x)) * 8
        img_out.paste(Image.frombytes("RGBA", (tile_x, tile_y), buffer_out), (x, y))
    return img_out



def create_MMap_image(MMap_file, mode, width, height, graphics_buffer_id, tileset_id, palette_id):
    MMap_file = BytesIO(MMap_file)

    # ==================================================================
    # start reading the data

    MMap_file.seek(tileset_id * 4)
    MMap_file.seek(int.from_bytes(MMap_file.read(4), "little"))
    tileset = BytesIO(decompress(MMap_file))

    MMap_file.seek(graphics_buffer_id * 4)
    MMap_file.seek(int.from_bytes(MMap_file.read(4), "little"))
    graphics_buffer = BytesIO(decompress(MMap_file))

    MMap_file.seek(palette_id * 4)
    MMap_file.seek(int.from_bytes(MMap_file.read(4), "little"))
    palette = define_palette(struct.unpack(f'<256H', MMap_file.read(0x200)))

    with open("test.dat", "wb") as test:
        MMap_file.seek(65 * 4)
        MMap_file.seek(int.from_bytes(MMap_file.read(4), "little"))
        test.write(decompress(MMap_file))

    # ==================================================================
    # start assembling the image

    tile_cache = {}
    img = Image.new("RGBA", (width * 8, height * 8))

    for i in range(tileset.getbuffer().nbytes // 2):
        tile = int.from_bytes(tileset.read(2), "little")

        if tile & 0b1111001111111111 not in tile_cache:
            graphics_buffer.seek((tile & 0x3FF) * 32 * (1 + mode))
            buffer_raw = graphics_buffer.read(32 * (1 + mode))

            buffer_colored = []
            match mode:
                case 0:
                    for j in range(64):
                        current_pix = (buffer_raw[j // 2] >> (4 * (j % 2))) & 0xF
                        if current_pix == 0:
                            trans = 0
                        else:
                            trans = 0xFF
                        buffer_colored.extend(palette[current_pix + ((tile >> 12) << 4)] + (trans,))
                case 1:
                    for j in range(64):
                        current_pix = buffer_raw[j]
                        if current_pix == 0:
                            trans = 0
                        else:
                            trans = 0xFF
                        buffer_colored.extend(palette[current_pix] + (trans,))
            
            tile_cache[tile & 0b1111001111111111] = Image.frombytes("RGBA", (8, 8), bytearray(buffer_colored))
        
        img_tile = tile_cache[tile & 0b1111001111111111]

        x_flip = tile & 0b0000010000000000 != 0
        y_flip = tile & 0b0000100000000000 != 0

        if x_flip:
            img_tile = ImageOps.mirror(img_tile)
        if y_flip:
            img_tile = ImageOps.flip(img_tile)

        img.paste(img_tile, ((i % width) * 8, (i // width) * 8), img_tile)

    return QtGui.QPixmap(QtGui.QImage(ImageQt(img)))