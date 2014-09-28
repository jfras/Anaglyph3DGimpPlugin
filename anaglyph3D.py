#!/usr/bin/env python

from gimpfu import *
from math import atan2, asin, sqrt

def getPointsFromStroke(stroke):
    p,c = stroke.points
    return [p[i:i+2] for i in range(2, len(p), 6)]

def do_work(image,drawable):
    
    image = pdb.gimp_image_duplicate(image)
    layers = image.layers
    vectors = pdb.gimp_image_get_active_vectors(image)
    if vectors != None:
        points = getPointsFromStroke(vectors.strokes[0])
        if len(points) >=4:
            v0 = [points[1][0]-points[0][0], points[1][1] - points[0][1]]
            v1 = [points[3][0]-points[2][0], points[3][1] - points[2][1]]
            l = sqrt(v0[0]**2 + v0[1]**2)
            angle = asin(v1[1]/l) - atan2( v0[1], v0[0])
            pdb.gimp_drawable_transform_rotate_default(layers[0], angle, 0, points[0][0], points[0][1], 1, 0)
            #if len(points) >= 6:
            pdb.gimp_layer_translate(layers[0],  (points[2][0] - points[0][0])/2,  (points[2][1] - points[0][1])/2)
            pdb.gimp_layer_translate(layers[1], -(points[2][0] - points[0][0])/2, -(points[2][1] - points[0][1])/2)

            pdb.gimp_layer_resize_to_image_size(layers[0])
            pdb.gimp_layer_resize_to_image_size(layers[1])
            #pdb.gimp_image_crop(image, image.width, image.height, 0,0)

    if image.base_type != 1:
        pdb.gimp_convert_grayscale(image)
    composed = pdb.plug_in_drawable_compose(image, layers[0], layers[1], None, None, "RGB")
    gimp.Display(composed)
    pdb.gimp_image_delete(image)
    pdb.gimp_image_delete(composed)


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




