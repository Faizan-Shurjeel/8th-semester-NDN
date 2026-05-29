## Course: Digital Image Processing (Theory)

**General Instructions for Students:**

* Use **A4 size white pages only**.
* Solve **each question step by step**.
* **Do not skip any steps**; partial steps will not be awarded marks.
* **Do not use direct or shortcut methods**.
* All mathematical workings must be clearly shown.
* Write neatly and keep your work **clean and well‑organized**.
* Submit your work as a **scanned PDF file** only.
* Upload the PDF on the LMS before the deadline.
* Treat each given image as a **2D matrix of gray‑level intensities**.
* Assume **8‑bit images** unless stated otherwise (gray levels 0–255).
* Show **all steps** for calculations. [CLO-3]

## Question 1: Image Negative Transformation

Given the following 4×4 grayscale image matrix **F**:

F = [ 25 60 120 200

40 80 140 220

10 90 160 240

0 30 70 255 ]

1. Write the **mathematical formula** for image negative transformation.
2. Compute the resulting image matrix **G** after applying the negative transformation.
3. Explain how this transformation affects visual appearance.

## Question 2: Linear Contrast Stretching

Consider the following 3×3 low‑contrast image **F**:

F = [ 90 95 100

92 97 102

94 96 98 ]

1. Identify **r\_min** and **r\_max** of the image.
2. Apply **linear contrast stretching** to map the range [r\_min, r\_max] → [0, 255].
3. Compute the transformed image matrix **G**.
4. Comment on why contrast stretching is useful.

## Question 3: Logarithmic Transformation

Given a 3×3 image matrix **F**:

F = [ 1 5 10

20 40 80

120 160 200 ]

1. Write the **log transformation equation**.
2. Using **c = 1**, compute the transformed matrix **G = log(1 + F)**.
3. Explain which intensity range (low or high) is emphasized by log transformation.

## Question 4: Power‑Law (Gamma) Transformation

Given the following normalized image matrix **F** (values between 0 and 1):

F = [ 0.10 0.30 0.50

0.60 0.75 0.90

0.20 0.40 0.80 ]

1. Apply **power‑law transformation** with **γ = 0.5** and **c = 1**.
2. Compute the resulting matrix **G**.
3. State whether dark or bright pixels are enhanced and why.

## Question 5: Bit‑Plane Slicing

Consider the following 3×3 image **F**:

F = [ 128 130 135

140 150 160

170 180 200 ]

1. Convert each pixel value into **8‑bit binary**.
2. Extract the **7th and 8th bit‑planes**.
3. Represent each extracted bit‑plane as a **binary matrix**.
4. Explain the importance of higher‑order bit‑planes.

## Question 6: Spatial Filtering Using Averaging Mask

Given the following 5×5 image **F**:

F = [ 10 20 30 40 50

20 30 40 50 60

30 40 50 60 70

40 50 60 70 80

50 60 70 80 90 ]

And a **3×3 averaging filter**:

H = (1/9) × [ 1 1 1

1 1 1

1 1 1 ]

1. Compute the filtered value at the **center pixel (3,3)** only.
2. Show all convolution steps.
3. Explain the effect of averaging filters on images.

## Question 7: Geometric Transformation

Given four pixels (0,0), (2,0), (0,2), (2,2) in an image:

1. Apply **scaling transformation** with factors **Sx = 2**, **Sy = 0.5**.
2. Apply **Translation transformation** with factors **dx = 2**, **dy = 2**.
3. Apply **shear transformation** with factors **x = 2**, **y = 1**.
4. Find the new pixel coordinates.
5. Draw coordinates before and after transformation.

## Question 8: Probabilistic Methods Using Gray‑Level Distribution

Consider the following **5×5 grayscale image** represented as a 2D matrix **F**. Pixel intensity levels lie in the range **0–7**.

F = [ 0 1 2 3 4

1 2 3 4 5

2 3 4 5 6

3 4 5 6 7

4 5 6 7 7 ]

**(a) Probability Mass Function (PMF)**

1. List all possible gray levels present in the image.
2. Count the number of occurrences of each gray level.
3. Compute the **probability p(rₖ)** of each gray level.

**(b) Mean and Variance of Gray Levels**

1. Using the PMF, compute the **mean (expected value)** of the image intensity.
2. Compute the **variance** of the gray levels.

**(c) Cumulative Distribution Function (CDF)**

1. Compute the **cumulative distribution function (CDF)** for each gray level.
2. Explain how the CDF is used in **histogram equalization**.