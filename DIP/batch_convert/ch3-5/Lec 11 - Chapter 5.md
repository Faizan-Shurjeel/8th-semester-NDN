Lecture - 11
Chapter 5
IMAGE RESTORATION
AND
RECONSTRUCTION

Image Degradation/Restoration Model
CPE415 Digital Image Processing | Dr. Ikramullah Khosa 2

Noise
Models
CPE415 Digital Image Processing | Dr. Ikramullah Khosa 3

Test Pattern
CPE415 Digital Image Processing | Dr. Ikramullah Khosa 4

Test Pattern after Adding Noise
CPE415 Digital Image Processing | Dr. Ikramullah Khosa 5

Test Pattern after Adding Noise
CPE415 Digital Image Processing | Dr. Ikramullah Khosa 6

Sinusoidal Noise
CPE415 Digital Image Processing | Dr. Ikramullah Khosa 7

Noisy Image Strip Histogram
CPE415 Digital Image Processing | Dr. Ikramullah Khosa 8

Restoration in the Presence of Noise Only
(De-Noising)
• Mean filters
• Arithmetic mean filter
1
|     |     | ˆ     |      |     |       |     |     |
| --- | --- | ----- | ---- | --- | ------ | --- | --- |
|     | •   | f (x, | y) = |     | g(s,t) |     |     |
g(x,y) is the corrupted image
mn
|     | • S  is the mask |     |     |     |     |     |     |
| --- | ---------------- | --- | --- | --- | --- | --- | --- |
(s,t)S
x,y
x,y
1
| •   | Geometric mean filters |       |     |    |         | mn |     |
| --- | ---------------------- | ----- | --- | --- | ------- | --- | --- |
|     |                        | ˆ     |     |    |         |     |     |
|     | •                      | f (x, | y)  | =  | g(s,t) |     |     |
Tends to preserve more details
|     |     |     |     |         |     |    |     |
| --- | --- | --- | --- | -------- | --- | --- | --- |
|     |     |     |     | (s,t)S |     |    |     |
x,y
•
Harmonic mean filter
mn
ˆ
|     | • Works well for salt noise but fails for pepper noise  |     |     |     |     | f (x, y) | =   |
| --- | ------------------------------------------------------- | --- | --- | --- | --- | -------- | --- |
1

g(s,t)
(s,t)S
x,y
• Contraharmonic mean filter
 g(s,t)Q+1
|     | • Q: order of the filter            |     |       |      |         |     |     |
| --- | ----------------------------------- | --- | ----- | ---- | ------- | --- | --- |
|     | • Positive Q works for pepper noise |     |       |      |         |     |     |
|     |                                     |     | ˆ     |      | (s,t)S |     |     |
|     |                                     |     | f (x, | y) = |         | x,y |     |
•
Negative Q works for salt noise
|     |                               |     |     |     |         |  g(s,t)Q |     |
| --- | ----------------------------- | --- | --- | --- | ------- | --------- | --- |
|     | • Q=0➔arithmetic mean filter  |     |     |     |         |           |     |
|     | • Q=-1➔harmonic mean filter   |     |     |     | (s,t)S |           |     |
x,y
CPE415 Digital Image Processing | Dr. Ikramullah Khosa 9

De-Noising
Corrupted by
Gaussian Noise
Arithmetic
Mean
Filtering
Geometric
Mean Filtering
CPE415 Digital Image Processing | Dr. Ikramullah Khosa 10

Corrupted by Corrupted by
De-Noising
pepper noise salt noise
3x3
3x3
Contraharmonic
Contraharmonic
Q=-1.5
Q=1.5
CPE415 Digital Image Processing | Dr. Ikramullah Khosa 11

De-Noising
3x3
3x3
Contraharmonic
Contraharmonic
Q=1.5
Q=-1.5
CPE415 Digital Image Processing | Dr. Ikramullah Khosa 12

Filters based on Order Statistics
(De-Noising)
• Median filter
• Median represents the 50th percentile of a ranked set of numbers
ˆ
|     |     | f (x, y) | = median{g(s,t)} |     |     |
| --- | --- | -------- | ---------------- | --- | --- |
(s,t)S
x,y
• Max and Min filter
• Max filter uses the 100th percentile of a ranked set of numbers
•
Good for removing pepper noise
• Min filter uses the 1 percentile of a ranked set of numbers
• Good for removing salt noise
• Midpoint filter
•
Works best for noise with symmetric PDF like Gaussian or uniform
| noise  |     | 1  |     |     |    |
| ------ | --- | --- | --- | --- | --- |
ˆ
|     | f (x, y) | = max | {g(s,t)}+ | min {g(s,t)} |     |
| --- | -------- | ----- | --------- | ------------ | --- |
|     |          |      |           |              |    |
2
|     |     | (s,t)S |     | (s,t)S |    |
| --- | --- | -------- | --- | ------- | --- |
|     |     |          | xy  | xy      |     |
CPE415 Digital Image Processing | Dr. Ikramullah Khosa 13

Corrupted by salt One pass median
De-Noising
& pepper noise filtering
Three pass
Two pass
median filtering
median filtering
CPE415 Digital Image Processing | Dr. Ikramullah Khosa 14

Corrupted by pepper Corrupted by Salt
De-Noising
noise noise
Max Filtering
Min Filtering
CPE415 Digital Image Processing | Dr. Ikramullah Khosa 15

Alpha-Trimmed Mean Filter
(De-Noising)
• Alpha-trimmed mean filter takes the mean value of the
pixels enclosed by an m×n mask after deleting the pixels
with the d/2 lowest and the d/2 highest gray-level values
1
ˆ

f (x, y) = g (s,t)
r
mn − d
(s,t)S
xy
• g (s,t) represent the remaining mn-d pixels
r
• It is useful in situations involving multiple types of
noise like a combination of salt-and-pepper and
Gaussian
CPE415 Digital Image Processing | Dr. Ikramullah Khosa 16

Added Salt &
Pepper noise
De-Noising
Corrupted by Additive
Uniform Noise
5x5
Arithmetic
Mean Filtering
5x5 Geo-Mean
Filtering
5x5 Median
5x5 Alpha-
Filtering
trimmed Mean
Filter
CPE415 Digital Image Processing | Dr. Ikramullah Khosa 17

Adaptive Filters (De-Noising)
• Adaptive Local Noise Reduction Filter
• Assume the variance of the noise       2    is either known or can be

estimated satisfactorily
• Filtering operation changes at different regions of an image
according to local variance      2  calculated within an M×N
L
region
| • If       | 2            | 2    , the filtering operation is defined as |     |     |     |     |     |
| ----------- | -------------- | -------------------------------------------- | --- | --- | --- | --- | --- |
|             | L              |                                             |     |     |     |     |     |
2
|     |     | ˆ        |        |      |      |        |     |
| --- | --- | -------- | ------ | ---- | ----- | ------ | --- |
|     |     | f (x, y) | = g(x, | y) − | [g(x, | y) − m | ]   |

|     |     |     |     | 2  |     |     | L   |
| --- | --- | --- | --- | --- | --- | --- | --- |
L
| If       | 2             | 2                                   |     |     |     |     |     |
| --------- | --------------- | ----------------------------------- | --- | --- | --- | --- | --- |
| •         |                 |   , the output takes the mean value |     |     |     |     |     |
|           | L               |                                    |     |     |     |     |     |
2

is set to be 1
| •   | That is: |     |     |     |     |     |     |
| --- | -------- | --- | --- | --- | --- | --- | --- |
2

L
|     |     |     |     | 2  | 2 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
•
At edges, it is assumes that
L 
CPE415 Digital Image Processing | Dr. Ikramullah Khosa 18

Corrupted by Arithmetic Mean
De-Noising
Gaussian noise Filtering
Geo-Mean Adaptive
Filtering Filtering
CPE415 Digital Image Processing | Dr. Ikramullah Khosa 19

Adaptive Median Filter (De-Noising)
• Median filter is effective for removing salt-and-pepper noise
• The density of the impulse noise can not be too large
• Adaptive median filter
• Notation
• Z : minimum gray value in S
min xy
• Z : maximum gray value in S
max xy
• Z : median of gray levels in S
med xy
• Z : gray value of the image at (x,y)
xy
• S : maximum allowed size of S
max xy
CPE415 Digital Image Processing | Dr. Ikramullah Khosa 20

Adaptive Median Filter (De-Noising)
• Two levels of operations
Used to test whether Z
med
is part of s-and-p noise. If
• Level A:
yes, window size is
• A1= Z –Z increased
med min
• A2= Z –Z
med max
• If A1 > 0 AND A2 < 0, Go to level B
else increase the window size by 2
• If window size <= S repeat level A
max
else output Z
xy
Used to test whether Z
xy
is part of s-and-p noise. If
• Level B:
yes, apply regular median
• B1= Z –Z
xy min
filtering
• B2= Z –Z
xy max
• If B1 > 0 AND B2 < 0, output Z
xy
else output Z
med
CPE415 Digital Image Processing | Dr. Ikramullah Khosa 21

De-Noising
Median Adaptive Median
Filtering Filtering
CPE415 Digital Image Processing | Dr. Ikramullah Khosa 22