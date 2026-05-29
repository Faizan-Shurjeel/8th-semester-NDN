<!-- Slide number: 1 -->
Lecture - 15
Chapter G
MORPHOLOGICAL IMAGE PROCESSING

<!-- Slide number: 2 -->
# Preliminaries: Morphology
Morphology in image processing is a tool for extracting image components that are useful in the representation and description of region shape, such as boundaries and skeletons.

Furthermore, the morphological operations can be used for filtering, thinning and pruning.

The language of the Morphology comes from the set theory, where image objects can be represented by sets. For example, an image object containing black pixels can be considered a set of black pixels in 2D space of Z2.
CPE415 Digital Image Processing | Dr. Ikramullah Khosa

<!-- Slide number: 3 -->
# Preliminaries: Set Theory Fundamentals
Given that A is a set in Z2and a=(a1,a2), then

a is an element in A:	a  A
a  A
a is not an element in A:
A  B
given sets A and B, A is said to be the subset of B:
C  A	B
The union of A and B is denoted by:

![](object12.jpg)
D  A	B
The intersection of A and B is denoted by:

![](object14.jpg)
Two sets are disjoint/mutually exclusive if	A	B 

![](object15.jpg)
Ac      A Bc
The complement of set A is the set of elements not contained in A,
The difference of two sets:	A  B     A,  B  A

![](object20.jpg)
CPE415 Digital Image Processing | Dr. Ikramullah Khosa

<!-- Slide number: 4 -->
# Preliminaries: Set Theory Fundamentals
Given 2 sets A and B

![](object5.jpg)
CPE415 Digital Image Processing | Dr. Ikramullah Khosa

<!-- Slide number: 5 -->
# Preliminaries: Set Theory Fundamentals
Bˆ     b,	for b  B
The reflection of set B is defined by:

The translation of set A by point z=(z1,z2) is defined by:
z      a  z,	for a  A

![](object9.jpg)
Reflection of B
Translation of A by z
CPE415 Digital Image Processing | Dr. Ikramullah Khosa

<!-- Slide number: 6 -->
# Reflection and Translation of a Set
CPE415 Digital Image Processing | Dr. Ikramullah Khosa

<!-- Slide number: 7 -->
# Preliminaries

![](object4.jpg)

![](object3.jpg)
CPE415 Digital Image Processing | Dr. Ikramullah Khosa

<!-- Slide number: 8 -->
# Preliminaries

![](object4.jpg)

![](object3.jpg)
CPE415 Digital Image Processing | Dr. Ikramullah Khosa

<!-- Slide number: 9 -->
# Preliminaries

![](object4.jpg)

![](object3.jpg)
CPE415 Digital Image Processing | Dr. Ikramullah Khosa

<!-- Slide number: 10 -->
# Erosion
A	B  z (B)z  A
The erosion of A by structuring element B is the set of all points z, such that B, translated by z, is
contained in A.
Erosion: Given A and B sets in Z2, the erosion of A by structuring element B, is defined by:

![](object6.jpg)

![](object5.jpg)

![](object8.jpg)

![](object7.jpg)

<!-- Slide number: 11 -->
# Erosion

![](object4.jpg)

![](object3.jpg)
CPE415 Digital Image Processing | Dr. Ikramullah Khosa

<!-- Slide number: 12 -->
Dilation
Dilation: Given A and B sets in Z2, the dilation of A by structuring element B,
is defined by:
A  B z (Bˆ)z	A  

The dilation of A and B is a set of all displacements, z , such that B and A
overlap by at least one element. The dilation can also be defined by:
A  B  z (Bˆ)z	A  A

![](object5.jpg)

![](object8.jpg)
CPE415 Digital Image Processing | Dr. Ikramullah Khosa

<!-- Slide number: 13 -->
# Dilation

![](object4.jpg)

![](object3.jpg)
CPE415 Digital Image Processing | Dr. Ikramullah Khosa

<!-- Slide number: 14 -->
# Dilation

![](object4.jpg)

![](object3.jpg)
CPE415 Digital Image Processing | Dr. Ikramullah Khosa

<!-- Slide number: 15 -->
# Opening
The process of erosion followed by dilation is called opening. It has the effect of eliminating small and thin objects, breaking the objects at thin points and smoothing the boundaries/contours of the objects.
Given set A and the structuring element B. Opening of A by structuring element B is defined by:
A ∘ B  ( A  B)  B

![](object4.jpg)

![](object5.jpg)

![](object6.jpg)
CPE415 Digital Image Processing | Dr. Ikramullah Khosa

<!-- Slide number: 16 -->
# Closing
The process of dilation followed by erosion is called closing. It has the effect of filling small and thin holes, connecting nearby objects and smoothing the boundaries/contours of the objects.
Given set A and the structuring element B, closing of A by structuring element B is defined by:
A  B  ( A  B)  B

![](object5.jpg)

![](object4.jpg)
CPE415 Digital Image Processing | Dr. Ikramullah Khosa

<!-- Slide number: 17 -->
# Opening Vs Closing

![](object4.jpg)

![](object3.jpg)
CPE415 Digital Image Processing | Dr. Ikramullah Khosa

<!-- Slide number: 18 -->
# Opening s Closing

![](object4.jpg)

![](object3.jpg)
CPE415 Digital Image Processing | Dr. Ikramullah Khosa

<!-- Slide number: 19 -->
# Applications of Morphological Image Processing
Boundary Extraction

![](object3.jpg)

![](object4.jpg)

![](object6.jpg)

![](object5.jpg)
CPE415 Digital Image Processing | Dr. Ikramullah Khosa

<!-- Slide number: 20 -->
# Applications of Morphological Image Processing
Hole Filling

![](object4.jpg)

![](object3.jpg)

![](object5.jpg)
CPE415 Digital Image Processing | Dr. Ikramullah Khosa

<!-- Slide number: 21 -->
# Applications of Morphological Image Processing
Hole Filling

![](object4.jpg)

![](object3.jpg)
CPE415 Digital Image Processing | Dr. Ikramullah Khosa

<!-- Slide number: 22 -->
# Applications of Morphological Image Processing
Connected Component Detection

![](object3.jpg)

![](object5.jpg)

![](object4.jpg)
CPE415 Digital Image Processing | Dr. Ikramullah Khosa

<!-- Slide number: 23 -->
# Applications of Morphological Image Processing
Connected Component Detection

![](object3.jpg)

![](object4.jpg)
CPE415 Digital Image Processing | Dr. Ikramullah Khosa

<!-- Slide number: 24 -->
# Applications of Morphological Image Processing
Hole Filling

![](object4.jpg)

![](object3.jpg)
CPE415 Digital Image Processing | Dr. Ikramullah Khosa