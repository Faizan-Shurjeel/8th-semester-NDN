Solution of Quiz # 2
Course: CPE415 – Digital Image Processing Date: 25-10-2023
Semester: 7th (FA20-BCE-A/B) Time Allowed: 30 min
Total Marks = 15
Name: Reg. No:
Question 1: Relate the concepts of image enhancement in the spatial and the frequency domain to answer
the following short questions. (CLO1-PLO1-C3)
A. Which spatial domain filter produces blurring in the image? (1)
Mean/Average filter
B. What type of frequency domain filter (whether used as low pass or high pass) never produces the ringing
effect? (1)
Gaussian filter
C. Does the Laplacian filter when applied in the spatial domain vs in the frequency domain produce similar
results? (1)
Yes
D. Which between spectrum and angle contributes more towards revealing significant visual information while
reconstruction from frequency domain back to the spatial domain? (1)
Angle
E. Write down the general/mathematical expression for unsharp masking. (1)
Unsharp mask = Original Image – Blurred Image
g(x,y) = f(x,y) – ꝭ(x,y)
F. Following pixel intensities are obtained by scanning the row of a 3-bit image. Compute the first and second
derivatives below them. Also write down the mathematical expression which you used to compute the
derivatives. (4)
Pixel Intensity f(x) 2 2 3 4 5 1 4 7
First Derivative 0 1 1 1 -4 3 3
Second Derivative 1 0 0 -5 7 0
Mathematical expression for First derivative = f(x+1) – f(x)
Mathematical expression for Second derivative = f(x-1) + f(x+1) – 2f(x)

G.  Label the missing intensity transformations. (2)

H.  A sample 3-bit image consisting of nine pixels is shown below. Produce the first, second and third (individual)
bit planes. Show the image reconstructed image by adding first- and third-bit planes. (4)

0  1  2
3  4  5
6  7  7

| 000  001  | 010  | 0  1  0  |     | 0  0  0  |
| --------- | ---- | -------- | --- | -------- |
0  0  1
| 011  100  | 101  | 1  0  1  |     | 0  1  1  |
| --------- | ---- | -------- | --- | -------- |
1  0  0
| 110  111  | 111  | 0  1  1  |     | 1  1  1  |
| --------- | ---- | -------- | --- | -------- |
1  1  1

(1st Bit Plane - LSB)   (2nd Bit Plane)            (3rd Bit Plane - MSB)
(Binary Equivalent)

| 0  1  0  |     | 0  0  0  | 0  1  | 0   |
| -------- | --- | -------- | ----- | --- |
| 1  0  1  |     | 0  4  4  |       |     |
1  4  5
|          |     | 4  4  4  |       |     |
| -------- | --- | -------- | ----- | --- |
| 0  1  1  |     |          | 4  5  | 5   |

(1st Bit Plane weight)        (3rd Bit Plane weight)        (Reconstructed Image = 1st + 3rd Bit plane weights)