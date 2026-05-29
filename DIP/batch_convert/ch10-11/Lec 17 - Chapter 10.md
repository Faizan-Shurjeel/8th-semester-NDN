<!-- Slide number: 1 -->
Lecture - 17
Chapter 10
IMAGE SEGMENTATION

<!-- Slide number: 2 -->
# Marr-Hildreth Edge Detector
LoG (Laplacian of Gaussian) Operator
	x   y	
2
2
	
G	x, y	 exp 


22

	
2G x, y 	2G x, y 
2
G x, y 

x2	y2

  1  G x, y   y2    1  G x, y 
2 G x, y   x2

	



	
	
4
4

2
2



x   y	 2

2	2
2
	
	
 G	x, y	
G	x, y
2


 4



r2
 r 2  2 2 


2
G x, y 
exp	

4



2
2

	


CPE415 Digital Image Processing | Dr. Ikramullah Khosa

<!-- Slide number: 3 -->
# Marr-Hildreth Edge Detector
LoG (Laplacian of Gaussian) Operator

![](object4.jpg)

![](object3.jpg)
CPE415 Digital Image Processing | Dr. Ikramullah Khosa

<!-- Slide number: 4 -->
# Marr-Hildreth Edge Detector
LoG (Laplacian of Gaussian) Operator
Idea:
Smoothing
Sharpening
g x, y 	 2Gx, y  f x, y  2 Gx, y 

Algorithm:

Compute Laplacian of Gaussian filtered
Find zero-crossing
Use a 3×3 window around each pixel
ZC occurs if at least two opposing neighbors has different signs.
CPE415 Digital Image Processing | Dr. Ikramullah Khosa

<!-- Slide number: 5 -->
# Marr-Hildreth Edge Detector
LoG (Laplacian of Gaussian) Operator

![](object4.jpg)

![](object3.jpg)
CPE415 Digital Image Processing | Dr. Ikramullah Khosa

<!-- Slide number: 6 -->
# Marr-Hildreth Edge Detector
LoG = Difference of Gaussian (DoG)
LoG Approximation with DoG:
–	DoG: Difference of Gaussian:
x2
x2

1	
 y2 	1
 y2 
DoG x, y 
 ,	 
2
2
2
exp 
 
exp 
2	2
2
2
1
2
2
2
2
2	

	1		
2
1
Ratio of 1.6:1, an engineering approximation of LoG.
For same zero-crossing:
2	 2

2
 
2
ln
1 2
1





2
2

2
2		2 
1
CPE415 Digital Image Processing | Dr. Ikramullah Khosa

<!-- Slide number: 7 -->
# Marr-Hildreth Edge Detector
LoG (Laplacian of Gaussian) Operator

![](object4.jpg)

![](object3.jpg)
CPE415 Digital Image Processing | Dr. Ikramullah Khosa

<!-- Slide number: 8 -->
# Canny Edge Detector
Canny Edge Detector Steps:
Smoothing
Compute Gradients
Non-maximum Suppression
Edge Tracking by hysteresis (double ) thresholding
CPE415 Digital Image Processing | Dr. Ikramullah Khosa

<!-- Slide number: 9 -->
# Canny Edge Detector
Canny – Smoothing:
–	Using Gaussian filter:
f s x , y  G x , y 
f x , y 

![](object17.jpg)
	x	 y	
2
2
	
,	 1.4
G	x , y	 exp  


22



–	Practical Implementation:
2
4
| 4 | 5 | 4 | 2 |
| --- | --- | --- | --- |
| 9 | 12 | 9 | 4  |

1
G x , y 
5	12	15	12
9	12	9
4	5	4
5
159 4

4

2

2
CPE415 Digital Image Processing | Dr. Ikramullah Khosa

<!-- Slide number: 10 -->
# Canny Edge Detector
Canny – Gradient:
Using any gradient kernel:
gx x , y  w x x , y 	f s x , y 
g y x , y  w y x , y 	f s x , y 
Practical Implementation:
Sobel Kernel

![](object4.jpg)

![](object5.jpg)
1	0	1
w x x , y  2	0
	
1	0	1
1	2	1
w y x , y   0	0
0 
2,

1	2	1

CPE415 Digital Image Processing | Dr. Ikramullah Khosa

<!-- Slide number: 11 -->
# Canny Edge Detector
Canny - Non-maximum Suppression (1):
–	Compute magnitude and angle of gradient:
g 2  g 2  g	 g
x	y
M x, y 

y
x
 g	
	
	x, y	 tan
y
1
 g	

	x 
–	Quantize the θ(x,y) to nearest 45°, θQ (x,y)

![](object24.jpg)
CPE415 Digital Image Processing | Dr. Ikramullah Khosa

<!-- Slide number: 12 -->
# Canny Edge Detector
Canny - Non-maximum Suppression (2)
-	Quantization

![](object5.jpg)

![](object4.jpg)
CPE415 Digital Image Processing | Dr. Ikramullah Khosa

<!-- Slide number: 13 -->
# Canny Edge Detector
Canny - Non-maximum Suppression (3)
Quantization

Compare M (x,y) with M (x´,y´) in positive and negative gradient direction.
If greater than both then keep it, gN (x,y)=M(x,y) 	else suppress it, gN (x,y)=0
If θQ (x,y) = 0°◦, then the pixels (x+1, y), (x, y), and (x−1, y) are examined.
If θQ (x,y) = 90°◦, then the pixels (x, y+1), (x, y), and (x, y−1) are examined.
If θQ (x,y) = 45°, then the pixels (x+1, y+1), (x, y), and (x−1, y−1) are examined.
If θQ (x,y) = 135°◦, then the pixels (x+1, y-1), (x, y), and (x−1, y+1) are examined.
CPE415 Digital Image Processing | Dr. Ikramullah Khosa

<!-- Slide number: 14 -->
# Canny Edge Detector
Canny – Edge Tracking (1):
Select two threshold (TH, TL), TH = kTL
Form two images using two threshold:
1	g N  x , y  TH
0	g N  x , y  TH
1	g N  x , y  TL
0	g N  x , y  TL
x , y  
Fewer and Strong Edge
g NH
g NL x , y  
More and Weak/Strong Edge
–	Eliminate strong edge from gNH
g NL x , y  g NL x , y  g NH  x , y 
CPE415 Digital Image Processing | Dr. Ikramullah Khosa

<!-- Slide number: 15 -->
# Canny Edge Detector
Canny – Edge Tracking (2):
All strong edge in gNH are store and marked immediately.
Gaps in gNH  with fill using gNL
Locate the next unvisited pixel, p, in gNH (x,y)
Mark as valid edge all weak pixels in gNL (x,y) that are
connected to p, using N8 criteria.
If all nonzero pixel in gNH (x,y) has been visited go to step #4 else go to step #1
Set to zero all pixels in gNL (x,y) that were not marked as
valid edge.
Append gNH (x,y) and nonzero elements of gNL (x,y)
CPE415 Digital Image Processing | Dr. Ikramullah Khosa

<!-- Slide number: 16 -->
# Canny Edge Detector
Canny Example (1):
– Original and Smoothed

![](object4.jpg)
CPE415 Digital Image Processing | Dr. Ikramullah Khosa

<!-- Slide number: 17 -->
# Canny Edge Detector
Canny Example (1):
– Gradient Image

![](object4.jpg)
CPE415 Digital Image Processing | Dr. Ikramullah Khosa

<!-- Slide number: 18 -->
# Canny Edge Detector
Canny Example (1):
– Non-maximum Suppression

![](object4.jpg)
CPE415 Digital Image Processing | Dr. Ikramullah Khosa

<!-- Slide number: 19 -->
# Canny Edge Detector
Canny Example (1):
– Double Thresholding

![](object4.jpg)
CPE415 Digital Image Processing | Dr. Ikramullah Khosa

<!-- Slide number: 20 -->
# Canny Edge Detector
Canny Example (1):
– Edge Tracking

![](object4.jpg)
CPE415 Digital Image Processing | Dr. Ikramullah Khosa

<!-- Slide number: 21 -->
# Canny Edge Detector
Canny Example (2):

![](object4.jpg)

![](object5.jpg)
CPE415 Digital Image Processing | Dr. Ikramullah Khosa

<!-- Slide number: 22 -->
# Canny Edge Detector
Canny Example (3):

![](object4.jpg)

![](object5.jpg)
CPE415 Digital Image Processing | Dr. Ikramullah Khosa

<!-- Slide number: 23 -->
# Edge Linking
Edge Linking (Local Processing):

Similarity of two edge pixels at (x,y) and (s,t):
M s,t  M x, y   E	and	 s,t x, y   A
Connect if both condition satisfied
Computational Expensive
CPE415 Digital Image Processing | Dr. Ikramullah Khosa

<!-- Slide number: 24 -->
# Edge Linking
Edge Linking (Local Processing):
A simple algorithm:
Compute M(x,y) and (x,y) for input image.
Form a binary image g(x,y):
M x, y  TM	x, y  A  TA
otherwise
and
1
g x, y  0

TM : Threshold, A: Specified angle direction, ±TA:acceptable direction margin
Scan rows of g and fill (set to 1) all gap (0’s) that do not exceed a
specified length, K.
Detect gaps in any direction, , by rotation the g by , and apply 	the horizontal scanning scheme. Rotate the result back to -
CPE415 Digital Image Processing | Dr. Ikramullah Khosa

<!-- Slide number: 25 -->
# Edge Linking

![](object4.jpg)

![](object3.jpg)
CPE415 Digital Image Processing | Dr. Ikramullah Khosa