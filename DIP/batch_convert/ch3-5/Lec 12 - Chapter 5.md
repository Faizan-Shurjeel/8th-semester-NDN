Lecture - 12
Chapter 5
IMAGE RESTORATION
AND
RECONSTRUCTION

Periodic Noise Reduction by Frequency
Domain Filtering
• Bandreject, bandpass, and notch filters as tools for periodic noise reduction
• Bandreject filters remove or attenuate a band of frequencies about the
origin of the Fourier transform. Similar to those LPFs and HPFs studied, we
can construct ideal, Butterworth, and Gaussian bandreject filters
• Notch filters that pass, rather than suppress: H (u, v) = 1− H (u, v)
np nr
u = v = 0
• NR filters become highpass filters if
0 0
u = v = 0
• NP filters become lowpass filters if
0 0
CPE415 Digital Image Processing | Dr. Ikramullah Khosa 2

Periodic Noise Reduction by Frequency
Domain Filtering
CPE415 Digital Image Processing | Dr. Ikramullah Khosa 3

Periodic Noise Reduction by Frequency
Domain Filtering
Notch Pass
Filtering
Notch Reject
Filter
Notch Reject
Filtering
CPE415 Digital Image Processing | Dr. Ikramullah Khosa 4

Periodic Noise Reduction by Frequency
Domain Filtering
Notch Pass
Filtering
Notch Reject
Filter
Notch Reject
Filtering
CPE415 Digital Image Processing | Dr. Ikramullah Khosa 5

Optimum Notch Filtering
CPE415 Digital Image Processing | Dr. Ikramullah Khosa 6

Optimum Notch Filtering
• In the ideal case, the original image can be restored if the
noise can be estimated completely.
• That is:
f (x, y) = g(x, y) −(x, y)
• However, the noise can be only partially estimated. This
means the restored image is not exact.
• Which means
ˆ
f (x, y) = g(x, y) −ˆ(x, y)
CPE415 Digital Image Processing | Dr. Ikramullah Khosa 7

Optimum Notch Filtering
• In this section, we try to improve the restored image by introducing a
modulation function
ˆ
|     |     | f   | (x, y) | = g(x, | y)  | − w(x, |     | y)ˆ(x, |     | y)  |     |     |     |
| --- | --- | --- | ------ | ------ | --- | ------ | --- | ------- | --- | --- | --- | --- | --- |
• Here  the modulation function is a constant within a neighborhood of size (2a+1) by
(2b+1) about a point (x,y)
•
We optimize its performance by minimizing the local variance of the restored image at
the position (x,y)
|     |       |      |     | 1      |     | a   | b   |      |     |      |      |            | 2   |
| --- | ----- | ---- | --- | ------ | --- | --- | --- | ---- | --- | ---- | ---- | ---------- | --- |
|     |       |      |     |        |     |     |     |  ˆ  |     |      |      | ˆ          |    |
|     | 2(x, | y) = |     |        |     |    |    | f (x | +   | s, y | + t) | − f (x, y) |     |
|     |       |      |     |        |     |     |     |     |     |      |      |            |    |
|     |       |      | (2a | +1)(2b | +1) |     |     |     |     |      |      |            |    |
s=−at=−b
|     |     |       |      |            | 1   |     | a   | b   |      |      |     |      |     |
| --- | --- | ----- | ---- | ---------- | --- | --- | --- | --- | ---- | ---- | --- | ---- | --- |
|     |     | ˆ     |      |            |     |     |     |     | ˆ    |      |     |      |     |
|     |     | f (x, | y) = |            |     |     |    |    | f (x | + s, | y   | + t) |     |
|     |     |       |      | (2a +1)(2b |     | +1) |     |     |      |      |     |      |     |
s=−at=−b
CPE415 Digital Image Processing | Dr. Ikramullah Khosa 8

Optimum Notch Filtering
|     |       |      |            | 1   |     | a b   |      |        |
| --- | ----- | ---- | ---------- | --- | --- | ----- | ---- | ------ |
|     | 2(x, |      |            |     |    |      |      |        |
|     |       | y) = |            |     |     | {[g(x | + s, | y + t) |
|     |       |      | (2a +1)(2b |     | +1) |       |      |        |
s=−at=−b
|     |     |     | − w(x  | + s, | y + t)ˆ(x | + s,    | y + t)] |     |
| --- | --- | --- | ------ | ---- | ---------- | ------- | ------- | --- |
|     |     |     |        |      |            | y)ˆ(x, | y]}2    |     |
|     |     |     | −[g(x, | y)   | − w(x,     |         |         |     |
Assumption:
| w(x | + s, y | + t) = w(x, | y)  | for    | − a  | s  a and | −b  | t  b |
| --- | ------ | ----------- | --- | ------ | ----- | --------- | ---- | ----- |
|     |        | y)ˆ(x,     |     |        | y)ˆ  |           |      |       |
|    | w(x,   |             | y)  | = w(x, |       | (x, y)    |      |       |
CPE415 Digital Image Processing | Dr. Ikramullah Khosa 9

Optimum Notch Filtering
|     |     |     | 1   |     |     |     | b   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
a
| 2(x, |     |     |     |     |    |     |    |       |      |        |
| ----- | --- | --- | --- | --- | --- | --- | --- | ----- | ---- | ------ |
|       | y)  | =   |     |     |     |     |     | {[g(x | + s, | y + t) |
s=−a
|     |     | (2a | +1)(2b |     | +1) |     |     |     |     |     |
| --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
t=−b
t)ˆ(x
|              |     | −      | w(x | + s, | y +    |      | + s, | y + t)] |     |     |
| ------------ | --- | ------ | --- | ---- | ------ | ---- | ---- | ------- | --- | --- |
|              |     |        |     |      |        | y)ˆ |      | y)}2    |     |     |
|              |     | −[g(x, |     | y)   | − w(x, |      | (x,  |         |     |     |
| To minimize  |     | 2(x,  | y)  |      |        |      |      |         |     |     |
2(x,
y)
= 0
|     |        |     |      | w(x, | y)      |     |          |      |        |     |
| --- | ------ | --- | ---- | ----- | ------- | --- | -------- | ---- | ------ | --- |
|     |        |     |      |       | y)ˆ(x, |     |          | y)ˆ |        |     |
|     |        |     | g(x, |       |         | y)  | − g(x,   |      | (x, y) |     |
|     |  w(x, | y)  | =    |       |         |     |          |      |        |     |
|     |        |     |      |       | ˆ2(x,  | y)  | −ˆ 2(x, | y)   |        |     |
CPE415 Digital Image Processing | Dr. Ikramullah Khosa 10

Optimum Notch Filtering
| g(x, y) |     |     | ˆ(x, | y)  |     |
| ------- | --- | --- | ----- | --- | --- |
w(x, y)
ˆ
y)ˆ(x,
| f (x, | y) = | g(x, | y) − | w(x, | y)  |
| ----- | ---- | ---- | ---- | ---- | --- |
CPE415 Digital Image Processing | Dr. Ikramullah Khosa 11

Optimum Notch Filtering
CPE415 Digital Image Processing | Dr. Ikramullah Khosa 12

Estimating the Image Degradation Function
• Degradation Model (with noise)
g(x, y) = H[ f (x, y)] +(x, y)
• Principal way to estimate the degradation function for use in image restoration:
▪ Observation
▪ Experimentation
▪ Mathematical modeling
CPE415 Digital Image Processing | Dr. Ikramullah Khosa 13

Estimating by Image Observation
• We look for a small section of the image that has strong signal
g (x, y)
content ( ) and then construct an un-degradation of this
s
ˆ
section by using sample gray levels ( f ( x , y ) ).
s
G (u,v)
H (u,v) = s
s ˆ
F (u,v)
s
• Now, we construct a function H ( u , v ) on a large scale, but having
the same shape.
CPE415 Digital Image Processing | Dr. Ikramullah Khosa 14

Estimating by Experimentation
• We try to obtain impulse response of the degradation by imaging
an impulse (small dot of light) using the system. Therefore
G(u,v)
H (u,v) =
A
CPE415 Digital Image Processing | Dr. Ikramullah Khosa 15

Estimating by Modeling
Severe
2 2 5/6
−k(u +v ) turbulence
• Atmospheric turbulence model: H(u,v) = e
k=0.0025
Negligible
turbulence
Mild
turbulence
Low
k=0.001
turbulence
CPE415 Digital Image Processing | Dr. Ikramullah Khosa 16
k=0.00025

Estimating by Modeling
Blurring by linear motion:
T
|     |     | g(x, | y) =  | f [x − | x (t), y − | y (t)]dt |     |
| --- | --- | ---- | ------ | ------ | ---------- | -------- | --- |
|     |     |      |        |        | 0          | 0        |     |
0
T
|     |     |        |            |     | − j2[ux (t)+vy | (t)] |     |
| --- | --- | ------ | ---------- | --- | --------------- | ---- | --- |
|     |     | G(u,v) | = F(u,v)e |     |                 | dt   |     |
0 0
0
T
|     |     |          |     | e−j2[ux | (t)+vy (t)]dt |     |     |
| --- | --- | -------- | --- | --------- | ------------- | --- | --- |
|     |     |  H(u,v) |     | =         | 0 0           |     |     |
0
T
| if x | (t) = | at /T | and | y (t) | = 0  |          | e−2uat/Tdt |
| ---- | ----- | ----- | --- | ----- | ----- | -------- | ----------- |
|      |       |       |     |       |       | H(u,v) = |            |
|      | 0     |       |     | 0     |       |          |             |
0
T
sin(ua)e− jua
=
ua
CPE415 Digital Image Processing | Dr. Ikramullah Khosa 17

Estimating by Modeling
| if  | x (t) = | at / T | and | y (t) | = bt | / T  |
| --- | ------- | ------ | --- | ----- | ---- | ----- |
|     | 0       |        |     | 0     |      |       |
T
|     | H (u,v) | =    |       | sin[(ua | +   | vb)]e − j(ua+vb) |
| --- | ------- | ---- | ----- | -------- | --- | ----------------- |
|     |         | (ua | + vb) |          |     |                   |
CPE415 Digital Image Processing | Dr. Ikramullah Khosa 18

Inverse Filtering
• The simplest approach to restoration is direct inverse filtering:
Even if we know the degradation
G(u,v)
ˆ
F(u,v) = function, we cannot recover the
H(u,v)
un-degraded image
N(u,v)
ˆ
F(u,v) = F(u,v) +
H(u,v)
If the degradation has zero or very small values, then the ratio
N/H could easily dominate our estimation of F .
One approach to get around the zero or small-value problem
is to limit the filter frequencies to value near the origin.
CPE415 Digital Image Processing | Dr. Ikramullah Khosa 19

Inverse Filtering
40
Degraded
Image
CPE415 Digital Image Processing | Dr. Ikramullah Khosa 20
70 85

Minimum Mean Square Error Filtering
(Wiener Filtering)
This approach incorporate both the degradation function and
statistical characteristic of noise into the restoration process.
ˆ
e2 = E[( f − f )2]
The objective is to find an estimation for f such that minimized
e2
CPE415 Digital Image Processing | Dr. Ikramullah Khosa 21

Wiener Filtering
Full inverse Radially limited
Wiener filtering
filtering inverse filtering
CPE415 Digital Image Processing | Dr. Ikramullah Khosa 22

Inverse filtering Wiener filtering
Wiener Filtering
Reduced
noise
variance
CPE415 Digital Image Processing | Dr. Ikramullah Khosa 23