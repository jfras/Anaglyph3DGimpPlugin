#!/usr/bin/env python

from gimpfu import *

def do_work(image,drawable):
    
    image = pdb.gimp_image_duplicate(image)
    layers = image.layers
    if image.base_type != 1:
        pdb.gimp_convert_grayscale(image)
    composed = pdb.plug_in_drawable_compose(image, layers[0], layers[1], None, None, "RGB")
    gimp.Display(composed)
    #for l in composed.layers:
    #	pdb.gimp_drawable_set_visible(l, True)
    #
    #nf = pdb.gimp_image_flatten(comoposed)
    #layer = pdb.gimp_layer_new_from_visible(composed, image, "Visible")
    #new_image = gimp.Image(layer.width, layer.height, "RGB")
    #pdb.gimp_image_add_layer(image, layer, 0)
    #gimp.Display(new_image)
    #gimp.displays_flush()

register(
    "anaglyph",
    "help",
    "help",
    "ja",
    "znowu ja",
    "2014",
    "Create 3D",
    "",
    [
        (PF_IMAGE, "image", "input", None),
        (PF_DRAWABLE, "drawable", "Input", None),
    ],
    [],
    do_work, menu="<Toolbox>/Moje")


main()




