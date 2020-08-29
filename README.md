# image_background_categorizer
This repo contains a simple python script to identify picture backround color based on the "frame" of the picture.

In many cases, you might need to tell from a picture automatically, whether it has a single or multi-colored background.
This script provides one solution to this by opening an image file, converting it to black and white and resizing it 
to 64x64 px. Then this image is converted to a numpy matrix, where the values represent the pixels and the hue by a value
between 0-255. 
After these, numpy calculate the sum of the value of a 2 px wide frame of this picture.
The assumption is, if the sum of these values should be between certain values, 
then the background pixels have fairly uniform values (e.g. single color).
At the current version only that is measured, whether the sum is above 120000 and if it is,
we can safely assume that the background is white(e.g. pixels with values ~255)
If this is true to the whole frame, then it is assumed that the same is uniformly true 
to the whole background.

However, as this decision happens on basis of the outer "frame",
this script has a hard time with such images which have a white frame,
or horizontally/vertically items on the image reach to the border.

