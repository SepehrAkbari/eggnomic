image = import["egg.png"]
image = FillingTransform[Closing[image, 2]]

comp = componentMeasurement[
    image, 
    {"Centroid", "Orientation", "Length"}
    ]

HighlightImage[img,
               comp /. (index -> {centroid_, orientation_, length_}) :> {
                   Rotate[Line[{centroid - {length/2, 0}, centroid + {length/2, 0}}],
                   orientation]
               }]