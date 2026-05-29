<!-- Slide number: 1 -->
Lecture - 13
Chapter 6
COLOR IMAGE PROCESSING

<!-- Slide number: 2 -->
# Color Fundamentals
Why use color in image processing?
Color is a powerful descriptor
Object identification and extraction
E.g. Face detection using skin colors

Humans can detect thousands of color shades and intensities
Human detect only two dozen shades of grays

![](object4.jpg)
2

<!-- Slide number: 3 -->
# Color Fundamentals
Two category of color image processing

Full color processing
Images are developed from full-color sensor or equipments

Pseudo-color processing
In the past decades, color sensors and processing hardware were not available
Colors were assigned to a range of monochrome intensities
CPE415 Digital Image Processing
3

<!-- Slide number: 4 -->
# Color Fundamentals

![](object3.jpg)

![](object4.jpg)

![](object5.jpg)

![](object6.jpg)
4

<!-- Slide number: 5 -->
# Color Fundamentals
6~7M Cones are the sensors in the eye

3 principal sensing categories in eyes: Red light 65%, green light 33%, and blue light 2%

![](object4.jpg)

![](object5.jpg)
5
CPE415 Digital Image Processing | Dr. Ikramullah Khosa

<!-- Slide number: 6 -->
# Color Fundamentals
The color that human perceive in an object = the 	light reflected from the object

scene
Illumination source

![](object10.jpg)

reflection

eye
CPE415 Digital Image Processing | Dr. Ikramullah Khosa
6

<!-- Slide number: 7 -->
# Primary colors of light vs. primary colors of pigments

![](object14.jpg)

![](object13.jpg)
Primary color of pigments
Color that subtracts or absorbs a primary 	color of light and reflects or transmits the 	other two
Color of light:
R
G
B

| Color of pigments: | absorb R | absorb G | absorb B |
| --- | --- | --- | --- |
|  | Cyan | Magenta | Yellow |
CPE415 Digital Image Processing | Dr. Ikramullah Khosa

### Notes:

<!-- Slide number: 8 -->
# Chromaticity Diagram

![](object4.jpg)
Chromaticity refers to the quality of a color independent of its brightness. It describes what color looks like in terms of:
Hue (red, green, blue, etc.)
Saturation (how pure or intense the color is) but not how light or dark it is.

Normalized tristimulus values
X
x 
X  Y  Z Y

y 
X  Y  Z
Z

z 
X  Y  Z

![](object5.jpg)
x+y+z=1

x, y (chromaticity coordinate) is enough to describe all colors
z = 1 – (x+y)
CPE415 Digital Image Processing | Dr. Ikramullah Khosa

### Notes:
Chromaticity refers to the quality of a color independent of its brightness. It describes what color looks like in terms of:
Hue (red, green, blue, etc.)
Saturation (how pure or intense the color is)
…but not how light or dark it is.

<!-- Slide number: 9 -->
# Chromaticity Diagram

![](object6.jpg)

![](object4.jpg)
RGB gamut of monitors

Color gamut of
printers
CPE415 Digital Image Processing | Dr. Ikramullah Khosa

<!-- Slide number: 10 -->
# Color Model
Color model, color space, color system
Specify colors in a standard way
A coordinate system that each color is represented by a 	single point
RGB model
CYM model
CYMK model

Suitable for display/hardware
HSI model
- Software processing (match the human description)
CPE415 Digital Image Processing | Dr. Ikramullah Khosa

<!-- Slide number: 11 -->
# The RGB Color Model

![](object5.jpg)

![](object6.jpg)
Pixel depth: the number of bits used 	to represent each pixel in RGB space

Full-color image: 24-bit RGB color 	image
(R, G, B) = (8 bits, 8 bits, 8 bits)

![](object7.jpg)

![](object8.jpg)
CPE415 Digital Image Proces
sing | Dr. Ikramullah Khosa

<!-- Slide number: 12 -->
# The RGB Color Model

![](object4.jpg)

![](object3.jpg)

<!-- Slide number: 13 -->
# Safe RGB Colors
Subset of colors is enough for some application
Safe RGB colors (safe Web colors, safe browser colors)

![](object4.jpg)
(6)3 = 216
CPE415 Digital Image Processing | Dr. Ikramullah Khosa

<!-- Slide number: 14 -->
# Safe RGB Colors

![](object3.jpg)

![](object4.jpg)
Full color cube
Safe color cube
CPE415 Digital Image Processing | Dr. Ikramullah Khosa

<!-- Slide number: 15 -->
# CMY (+Black = CMYK) Color Model
CMY: secondary colors of light, or primary colors of 	pigments
Used to generate hardcopy output

![](object8.jpg)
 C 	1	R
M   1  G
		 		
1
 Y 
B

<!-- Slide number: 16 -->
# HSI Color Model
Will you describe a color using its R, G, B 	components?
Human describe a color by its hue, saturation, and 	brightness
Hue : color attribute
Saturation: purity of color (white->0, primary color->1)
Brightness: achromatic notion of intensity

<!-- Slide number: 17 -->
# HSI Color Model
Colors on this triangle Have the same hue (Iso-hue triangle)
Intensity line

![](object4.jpg)

![](object6.jpg)
saturation
CPE415 Digital Image Processing | Dr. Ikramullah Khosa

<!-- Slide number: 18 -->
# HSI Color Model

![](object3.jpg)

![](object4.jpg)
CPE415 Digital Image Processing | Dr. Ikramullah Khosa

<!-- Slide number: 19 -->

![](object3.jpg)
# HSI Color Model

![](object4.jpg)
CPE415 Digital Image Processing | Dr. Ikramullah Khosa

<!-- Slide number: 20 -->
# HSI Color Model

![](object5.jpg)

![](object3.jpg)

![](object4.jpg)

<!-- Slide number: 21 -->
# HSI Color Model

![](object3.jpg)

![](object4.jpg)
CPE415 Digital Image Processing | Dr. Ikramullah Khosa

<!-- Slide number: 22 -->
# HSI Color Model

![](object3.jpg)

![](object4.jpg)
CPE415 Digital Image Processing | Dr. Ikramullah Khosa

<!-- Slide number: 23 -->
# Pseudo-color Image Processing
Assign colors to gray values based on a specified 	criterion

For human visualization and interpretation of gray-	scale events

Intensity slicing
Gray level to color transformations

CPE415 Digital Image Processing | Dr. Ikramullah Khosa

<!-- Slide number: 24 -->
# Intensity Slicing

![](object3.jpg)

![](object4.jpg)

![](object5.jpg)

![](object6.jpg)
CPE415 Digital Image Processing | Dr. Ikramullah Khosa

<!-- Slide number: 25 -->
# Intensity Slicing Application

![](object3.jpg)

![](object4.jpg)

![](object5.jpg)

![](object10.jpg)

![](object6.jpg)

![](object7.jpg)

![](object8.jpg)
CPE415 Digital Image Processing | Dr. Ikramullah Khosa

<!-- Slide number: 26 -->
# Intensity Slicing Application

![](object4.jpg)

![](object5.jpg)
CPE415 Digital Image Processing | Dr. Ikramullah Khosa