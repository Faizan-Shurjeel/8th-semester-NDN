Lecture - 6
Chapter 3
INTENSITY TRANSFORMATION
AND SPATIAL FILTERING

Histogram Processing
| h  r | = n | ,            |           |             |            |     |
| ---- | --- | ------------ | --------- | ----------- | ---------- | --- |
|      |     |              |          |            |           |    |
| (    | )   |              |           |             |            |     |
|      |     |            r |  0, L −1 | ,         n |  0,M  N  |     |
| k    |     | k            | k         |             | k          |     |
|      |     |              | n         | 1           |            |     |
|      |     | (            | )         |             |            |     |
|      |     | p r          | = k =     |             | n          |     |
|      |     | k            |           |             | k          |     |
|      |     |              | n         | M  N       |            |     |
CPE415 Digital Image Processing | Dr. Ikramullah Khosa 2

Histogram Processing
CPE415 Digital Image Processing | Dr. Ikramullah Khosa 3

Histogram Processing
CPE415 Digital Image Processing | Dr. Ikramullah Khosa 4

Histogram Equalization
|     |     |     | k   |     |     | k   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
L −1
( )
|     | ( ) | (      | )  | p r = |    |      |          |        |
| --- | --- | ------ | --- | ----- | --- | ---- | -------- | ------ |
| S = | T r | = L −1 |     |       |     | n  , | k = 0,1, | , L −1 |
| k   | k   |        |     | r j   | MN  | k    |          |        |
|     |     |        | j=0 |       | J=0 |      |          |        |
|     |     |        |     |       |     |      | 𝑆        | 𝑆      |
𝑘
|     |     |     |     | (   | )   |     |     | 𝑘   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

|     |     |     | S = 7 | p r |     |     | 1.33 | 1   |
| --- | --- | --- | ----- | --- | --- | --- | ---- | --- |
|     |     |     | k     | r j |     |     |      |     |
|     |     |     |       |     |     |     | 3.08 | 3   |
j=0
|                                                        |     |     |     |     |     |     | 4.55 | 5   |
| ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | ---- | --- |
|                                                        |     |     |     |     |     |     | 5.67 | 6   |
|                                                        |     |     |     |     |     |     | 6.23 | 6   |
|                                                        |     |     |     |     |     |     | 6.65 | 7   |
|                                                        |     |     |     |     |     |     | 6.86 | 7   |
|                                                        |     |     |     |     |     |     | 7.00 | 7   |
| CPE415 Digital Image Processing | Dr. Ikramullah Khosa |     |     |     |     |     |     |      | 5   |

Histogram Equalization
CPE415 Digital Image Processing | Dr. Ikramullah Khosa 6

Histogram Matching (Specification)
| (   | )      | (    | )   |      |     |     |     |     |     |
| --- | ------ | ---- | --- | ---- | --- | --- | --- | --- | --- |
| p   | r ⎯?⎯→ | p    | z   |      |     |     |     |     |     |
| r   |        | z    |     |      |     |     |     |     |     |
|     |        |      | r   |      |    |     |     |     |     |
|     | ( )    | (    | )  | ( )  |     |     |     |     |     |
| s = | T r =  | L −1 | p   | w dw |     |     |     |     |     |

r

|     |     |     | 0   |     |     | G−1 | ( )   | G−1 |    |
| --- | --- | --- | --- | --- | --- | --- | ----- | ---- | --- |
|     |     |     |     |     |  z | =   | T r  |  =  | s   |
|     |     |     |     |     |    |     |      |     |     |
z

| (   | ) (    | )  | ( ) |     |    |     |     |     |     |
| --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
| G z | = L −1 |     | p t | dt  |     |     |     |     |     |
z

0
CPE415 Digital Image Processing | Dr. Ikramullah Khosa 7

Histogram Matching (Specification)
CPE415 Digital Image Processing | Dr. Ikramullah Khosa 8

Histogram Matching (Specification)
CPE415 Digital Image Processing | Dr. Ikramullah Khosa 9

Histogram Matching (Specification)
CPE415 Digital Image Processing | Dr. Ikramullah Khosa 10

Histogram Matching (Specification)
CPE415 Digital Image Processing | Dr. Ikramullah Khosa 11

Histogram Matching (Specification)
CPE415 Digital Image Processing | Dr. Ikramullah Khosa 12

Local Histogram Equalization
CPE415 Digital Image Processing | Dr. Ikramullah Khosa 13

Image Enhancement using Local Histogram
Statistics
|     | (   | )      |     |     | ( ) |     |        |     | (   | )   |     |     |     |     |     |     |
| --- | --- | ------ | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| m   |     | x, y = | r   | p   | r  |     |         |     | f   | s,t |     |     |     |     |     |     |
|     | S   |        | i   | S   | i   |     |         |     |     |     |     |     |     |     |     |     |
|     | xy  |        |     | xy  |     | S   |         |     |     |     |     |     |     |     |     |     |
|     |     |        | i=0 |     |     | xy  | (s,t)S |     |     |     |     |     |     |     |     |     |
xy
|      |     | L−1    |     |     |     |      |     |     |       | 1   |         |       |     |     |     |     |
| ---- | --- | ------ | --- | --- | --- | ---- | --- | --- | ----- | --- | ------- | ----- | --- | --- | --- | --- |
|      |     |        | (   |     |     |      | )2  |     |       |     |         |       |     |     |     | 2   |
|   2 | (   | )     |     |     | (   | )    |     | (   | r )  |     |        |  (   | )   |     | (   | )  |
|      |     | x, y = | r   | − m |     | x, y | p   |     |       |     |         | f s,t | −   | m   | x,  | y   |
| S    |     |        |     | i   | S   |      |     | S   | i     |     |         |      |     | S   |     |    |
|      | xy  |        |     |     | xy  |      |     | xy  |       | S   |         |       |     | xy  |     |     |
|      |     | i=0    |     |     |     |      |     |     |       | xy  | (s,t)S |       |     |     |     |     |
xy
|     |                |     |     |          |     |     | (   |      | )   |     |     |     |     |     |     |     |
| --- | -------------- | --- | --- | -------- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
| S   | : Neighborhood |     |     | centered |     | on  |     | x, y |     |     |     |     |     |     |     |     |
xy
CPE415 Digital Image Processing | Dr. Ikramullah Khosa 14

Image Enhancement using Local Histogram
Statistics
CPE415 Digital Image Processing | Dr. Ikramullah Khosa 15