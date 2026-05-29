DIP Exam
① Basics
② Lin vs Non-Lin
③ Low-Pass
④ High-Pass
⑤ Laplacian
⑥ Sobel
⑦ Non-Linear
⑧ Histogram Eq
⑨ Geo Transforms
⑩ Fwd/Bkwd Map
⑪ Bilinear Interp
⚡ Cheat Sheet

01

# Spatial Filtering — The Foundation

What is an Image?

An image is a 2D grid of numbers (pixels). Each pixel holds an intensity value — typically 0 (black) to 255 (white) for an 8-bit grayscale image. Color images have 3 channels (R, G, B).

Image representation
f(x, y) → value at row x, column y
Range: [0, 255] for 8-bit grayscale
Size: M × N pixels

What is Spatial Filtering?

You take a small mask (kernel) — usually 3×3 or 5×5 — and slide it over every pixel in the image. At each position, you do math between the mask values and the image pixels underneath to produce a new pixel value.

General formula (linear filter)
g(x,y) = Σ Σ w(s,t) · f(x+s, y+t)

where w = mask weights, f = input image, g = output image

📐 Key Vocabulary

Mask / Kernel / Filter / Template — all the same thing. The small weight grid you slide over the image.

Boundary problem — when the mask goes outside the image edges. **Solution: Ignore boundary pixels** (copy them as-is). This is what your quiz says "Ignore the boundary" — just keep the border row/column unchanged from the original.

Correlation vs Convolution

#### Correlation

Slide the mask as-is. Used for **pattern matching** — finding where a template exists in an image (maximum similarity point).

#### Convolution

Flip the mask 180° (horizontally AND vertically) before sliding. Used for applying **mathematical filters**.

🔑 Trick Question

When are they the same? When the mask is symmetric (looks the same after flipping). Example: averaging mask (all 1/9s), Gaussian, Laplacian. The flip doesn't change them.

02

# Linear vs Non-Linear Filters

The Core Distinction

#### LINEAR LINEAR

Output = **Weighted Sum**

Math: multiply each pixel by a weight, add them all up.

Examples: Averaging, Gaussian, Laplacian, Sobel

#### NON-LINEAR NON-LINEAR

Output = **Sorting / Logic**

No multiplication. Just sort and pick (max, min, median).

Examples: Max, Min, Median filter

Linear filter test
g(x,y) = w₁·f₁ + w₂·f₂ + ... + wₙ·fₙ ← Linear (weighted sum)
g(x,y) = max(f₁, f₂, ..., fₙ) ← Non-Linear (no weights)

Why Does This Distinction Matter?

| Property | Linear | Non-Linear |
| --- | --- | --- |
| Superposition holds? | Yes | No |
| Math operation | Multiply + Add | Sort / Compare |
| Mask weights used? | Yes | No |
| Edge-preserving? | Poor | Better (Median) |

⚡ Exam Memory Trick

Linear = "L" = Linear equation (multiply & add). Non-Linear = "No equation, just logic."

03

# Low-Pass Filters (Smoothing / Blurring)

What is a Low-Pass Filter?

A low-pass filter blurs the image by averaging nearby pixels. It removes high-frequency content (sharp edges, noise) and keeps low-frequency content (general shapes).

**Two golden rules for any smoothing/averaging mask:**

Rule 1: All weights must be POSITIVE (≥ 0)
Rule 2: Sum of all weights MUST EQUAL 1

Box Filter (Simple Averaging)

Every weight in the mask is equal. Treats the center pixel and corner pixels as equally important.

3×3 Box Filter

1/91/91/9
1/91/91/9
1/91/91/9

✏️ Worked Example — Box Filter

Apply 3×3 averaging to the center pixel (18) of this 3×3 region:

999
9189
999

1

Sum all 9 pixels: 9×8 + 18 = 72 + 18 = 90

2

Multiply each by 1/9 and sum = 90 × (1/9) = **10**

3

Center pixel 18 → 10 (the average is lower because 18 was an outlier)

Weighted Average Filter

Weights are NOT equal. Center pixel gets the highest weight; weights decrease toward edges. Less blurring than box filter because original center pixel is trusted more.

3×3 Weighted (÷16)

1/162/161/16
2/164/162/16
1/162/161/16

🔑 Key Rule

Sum of raw weights = 16, so divide by 16. This ensures sum = 1. Center weight (4) > edge weight (2) > corner weight (1).

Gaussian Filter

The Gaussian filter is a special weighted average where weights come from the Gaussian (bell curve) function. Weights fall off smoothly with distance from center.

Gaussian function
G(x,y) = (1/2πσ²) · e^(-(x²+y²)/2σ²)

σ (sigma) = controls how wide/strong the blur is
Larger σ → heavier blur → bigger kernel needed

Gaussian approx (σ≈1)

121
242
121

| Property | Value |
| --- | --- |
| Type | LINEAR LOW-PASS |
| Symmetric? | Yes → Correlation = Convolution |
| Sum of weights | Must = 1 (divide by 16) |
| Use case | Smooth + blur, remove Gaussian noise |

📌 Gaussian vs Box Filter

Gaussian gives smoother, more natural blur. Box filter is simpler but creates "ringing" artifacts. Both are low-pass linear filters.

Effect of Mask Size

| Mask Size | Effect |
| --- | --- |
| 3×3 | Mild smoothing, minor noise removal |
| 7×7 | Moderate blur, some edge loss |
| 15×15, 35×35 | Heavy blur — tiny objects disappear, only large shapes survive |

This is used in the 3-step object extraction method: Heavy Blur → Threshold → Point-by-Point Multiply with original.

04

# High-Pass Filters (Sharpening)

What is a High-Pass Filter?

The opposite of blurring. Sharpening filters highlight edges, lines, and fine details by amplifying high-frequency content. They work by detecting where the image changes rapidly.

**Two golden rules for any sharpening mask:**

Rule 1: Weights must have BOTH positive AND negative values
Rule 2: Sum of all weights MUST EQUAL 0

Generic Sharpening Kernel

8-neighbor sharpening

-1-1-1
-18-1
-1-1-1

Verify: 8 × (-1) + 8 = -8 + 8 = 0 ✓

This produces an image with only edges — bright where the image changes sharply, zero where it is flat.

High-Pass vs Low-Pass — Summary

| Property | Low-Pass (Blur) | High-Pass (Sharpen) |
| --- | --- | --- |
| Weights | All positive | Mix of + and − |
| Sum of weights | = 1 | = 0 |
| Effect | Blurs image, removes noise | Highlights edges |
| Frequency content | Keeps low freq, removes high | Keeps high freq, removes low |

05

# Laplacian Filter + Composite

What is the Laplacian?

The Laplacian is the second-order derivative of an image. It measures how much the intensity changes in all directions simultaneously. It's the main tool for edge/detail detection using second derivatives.

Second derivative definition
∂²f/∂x² = f(x+1,y) + f(x-1,y) - 2f(x,y) ← in x-direction
∂²f/∂y² = f(x,y+1) + f(x,y-1) - 2f(x,y) ← in y-direction

∇²f = ∂²f/∂x² + ∂²f/∂y² (Laplacian = sum of both)

4-Connectivity Laplacian Kernel

Expanding ∇²f gives us the kernel below. Only looks at 4 direct neighbors (up/down/left/right).

4-connectivity kernel

0-10
-14-1
0-10

8-connectivity kernel

-1-1-1
-18-1
-1-1-1

Simplified formula (4-connectivity)
L(x,y) = 4·f(x,y) - f(x-1,y) - f(x+1,y) - f(x,y-1) - f(x,y+1)

= 4·center − top − bottom − left − right

Composite (Sharpened) Image

The Laplacian alone gives edges only — the original intensity is gone. To sharpen the image while keeping detail, we add the Laplacian back to the original:

Composite filter formula
C(x,y) = f(x,y) + L(x,y) ← Sharpened image

(This is equivalent to "unsharp masking" — adds back the edges)

Full Worked Example (from your Quiz 1)

Input image:

2 3 4 1 5
1 4 5 3 1
2 7 6 5 1
1 2 1 2 1
4 4 1 2 1

Boundary rows/cols are copied as-is. Interior pixels (rows 1–3, cols 1–3 in 0-indexing):

✏️ Laplacian calculations (4-connect)

**(1,1) center=4:** 4·4 − 3(top) − 7(bot) − 1(left) − 5(right) = 16−16 = 0

**(1,2) center=5:** 4·5 − 4(top) − 6(bot) − 4(left) − 3(right) = 20−17 = 3

**(1,3) center=3:** 4·3 − 1(top) − 5(bot) − 5(left) − 1(right) = 12−12 = 0

**(2,1) center=7:** 4·7 − 4(top) − 2(bot) − 2(left) − 6(right) = 28−14 = 14

**(2,2) center=6:** 4·6 − 5(top) − 1(bot) − 7(left) − 5(right) = 24−18 = 6

**(2,3) center=5:** 4·5 − 3(top) − 2(bot) − 6(left) − 1(right) = 20−12 = 8

**(3,1) center=2:** 4·2 − 7(top) − 4(bot) − 1(left) − 1(right) = 8−13 = -5

**(3,2) center=1:** 4·1 − 6(top) − 1(bot) − 2(left) − 2(right) = 4−11 = -7

**(3,3) center=2:** 4·2 − 5(top) − 2(bot) − 1(left) − 1(right) = 8−9 = -1

**Output Image 1 (Laplacian):**

2 3 4 1 5 (boundary — unchanged)
1 0 3 0 1
2 14 6 8 1
1 -5 -7 -1 1
4 4 1 2 1 (boundary — unchanged)

**Output Image 2 (Composite = Original + Laplacian):**

2 3 4 1 5
1 4+0 5+3 3+0 1 → 1 4 8 3 1
2 7+14 6+6 5+8 1 → 2 21 12 13 1
1 2-5 1-7 2-1 1 → 1 -3 -6 1 1
4 4 1 2 1

📌 Observation

Composite sharpens: flat areas stay similar (4→4), edges get amplified (7→21). Negative values indicate strong edges; in 8-bit output they're clamped to 0.

06

# Sobel Filter — Edge Detection

What Does Sobel Do?

Sobel detects edges using the first-order derivative — it measures how fast the pixel values are changing. Unlike Laplacian (2nd derivative), Sobel is more noise-resistant because it also does some smoothing.

There are two separate kernels: one for horizontal edges (Gy) and one for vertical edges (Gx).

The Two Sobel Kernels

Gx — Detects Vertical Edges

-10+1
-20+2
-10+1

Gy — Detects Horizontal Edges

-1-2-1
000
+1+2+1

Gradient magnitude
G = √(Gx² + Gy²) ← exact
G ≈ |Gx| + |Gy| ← approximate (used in exam questions)

Direction: θ = arctan(Gy / Gx)

How to Apply Sobel — Step by Step

1

Take the 3×3 neighborhood around your center pixel

2

Apply Gx: (-1·P1 + 0·P2 + 1·P3) + (-2·P4 + 0·P5 + 2·P6) + (-1·P7 + 0·P8 + 1·P9)

3

Apply Gy: (-1·P1 - 2·P2 - 1·P3) + (0·P4 + 0·P5 + 0·P6) + (1·P7 + 2·P8 + 1·P9)

4

Combine: G = |Gx| + |Gy|

✏️ Quick Example

3×3 neighborhood (P = pixel values):

101010
1010100
1010100

**Gx** = (-1·10 + 0·10 + 1·10) + (-2·10 + 0·10 + 2·100) + (-1·10 + 0·10 + 1·100)

= (0) + (-20 + 200) + (-10 + 100) = 0 + 180 + 90 = 270

**Gy** = (-1·10 - 2·10 - 1·10) + 0 + (1·10 + 2·10 + 1·100)

= -40 + 0 + 130 = 90

**G** = |270| + |90| = 360 (strong edge!)

Sobel vs Laplacian

| Property | Sobel | Laplacian |
| --- | --- | --- |
| Derivative order | 1st | 2nd |
| Direction sensitive? | Yes (Gx, Gy) | No (isotropic) |
| Noise sensitivity | Lower (has smoothing) | Higher |
| Kernels needed | Two (Gx + Gy) | One |

07

# Non-Linear Filters

Median Filter

Sort all values under the mask. Pick the middle value.

Sort pixels → pick middle value (median)

| Property | Value |
| --- | --- |
| Type | NON-LINEAR |
| Best for | Removing **Salt and Pepper noise** (random black AND white dots) |
| Key advantage | Preserves edges better than averaging filter |

✏️ Example

Values under 3×3 mask: 2, 3, 4, 6, 5, 4, 1, 2, 1

Sorted: 1, 1, 2, 2, **3**, 4, 4, 5, 6 → Median = 3

Max Filter

Pick the largest value under the mask.

| Property | Value |
| --- | --- |
| Type | NON-LINEAR |
| Best for | Removing **Pepper noise** (pure black 0-value dots) |
| Why? | Black = 0. Taking the max eliminates zeros → removes black dots |

Min Filter

Pick the smallest value under the mask.

| Property | Value |
| --- | --- |
| Type | NON-LINEAR |
| Best for | Removing **Salt noise** (pure white 255-value dots) |
| Why? | White = 255. Taking the min eliminates 255s → removes white dots |

⚡ Memory Trick

**Salt** (white dots) = Min filter. **Pepper** (black dots) = Max filter. **Both** (salt+pepper) = Median filter.

Summary Comparison

| Filter | Operation | Noise Type |
| --- | --- | --- |
| Max | Pick highest value | Pepper (black dots) |
| Min | Pick lowest value | Salt (white dots) |
| Median | Pick middle value | Salt + Pepper |
| Average | Sum × weight | Gaussian noise |

08

# Histogram Equalization

What is a Histogram?

A histogram of an image counts how many pixels have each intensity value. X-axis = intensity (0–255), Y-axis = count.

h(rk) = nk / (M × N)

nk = number of pixels with intensity rk
M×N = total number of pixels
h(rk) = probability of that intensity

Why Equalize?

A dark image has most pixels bunched near 0. A washed-out image has them bunched near 255. Histogram equalization spreads the intensities across the full 0–255 range to improve contrast.

Algorithm — Step by Step

Transformation formula
sk = T(rk) = (L-1) × Σ[j=0 to k] h(rj)

sk = new intensity for pixels with old intensity rk
L = number of gray levels (256 for 8-bit)
Σh = CDF (Cumulative Distribution Function)

1

**Count pixels** at each intensity level → histogram h(r)

2

**Normalize** by total pixels → probability p(r) = count / total

3

**Cumulative Sum** (CDF): add each p(r) progressively from 0 up

4

**Multiply CDF by (L−1)** = 255 and round → new intensity level

5

**Replace** all original pixels with their new values

Worked Example

4-bit image (L=16, so max intensity = 15). Total pixels = 64.

✏️ Histogram Equalization

| r (intensity) | Count nk | p(r) = nk/64 | CDF Σp | s = round(15 × CDF) |
| --- | --- | --- | --- | --- |
| 0 | 10 | 0.156 | 0.156 | 2 |
| 2 | 8 | 0.125 | 0.281 | 4 |
| 5 | 15 | 0.234 | 0.515 | 8 |
| 9 | 20 | 0.313 | 0.828 | 12 |
| 14 | 11 | 0.172 | 1.000 | 15 |

Notice how the dark image (bunched at 0,2) gets spread out to use values 2,4,8,12,15.

📌 Key Points

• The shape of the output histogram is approximately flat (uniform) — that's the goal.
• CDF always ends at exactly 1.0.
• This is a **point/pixel operation** — each output pixel depends only on its own input value (no neighborhood needed).

09

# Geometric Transformations

What are Geometric Transformations?

Instead of changing pixel values, geometric transforms change where pixels are located. They move, scale, or rotate the image.

All geometric transforms can be written as a **matrix multiplication** using homogeneous coordinates:

[x'] [T] × [x]
[y'] = [y]
[1 ] [1]

Translation

Shifts the image by (tx, ty). Every point moves by the same amount.

Equations
x' = x + tx
y' = y + ty

Matrix form:
|1 0 tx| |x| |x + tx|
|0 1 ty| × |y| = |y + ty|
|0 0 1| |1| | 1 |

✏️ Quiz 2 Example — Translation by (-1, -1)

| Point | Original | Formula | Translated |
| --- | --- | --- | --- |
| A | (1,1) | (1-1, 1-1) | A'(0,0) |
| B | (3,1) | (3-1, 1-1) | B'(2,0) |
| C | (3,3) | (3-1, 3-1) | C'(2,2) |
| D | (1,3) | (1-1, 3-1) | D'(0,2) |

Shape, size, and orientation are preserved. Only position changes. This is a **rigid body transformation**.

Scaling

Resizes the image by factors sx (horizontal) and sy (vertical).

x' = sx · x
y' = sy · y

Matrix:
|sx 0 0|
|0 sy 0|
|0 0 1|

📌 Cases

sx = sy → Uniform scaling (aspect ratio preserved)
sx ≠ sy → Non-uniform (stretches/squishes)
sx = sy = 2 → Image doubles in size
sx = sy = 0.5 → Image halves in size

Rotation

Rotates the image by angle θ around the origin.

x' = x·cosθ - y·sinθ
y' = x·sinθ + y·cosθ

Matrix:
|cosθ -sinθ 0|
|sinθ cosθ 0|
|0 0 1|

⚡ Memory Aid

x' = cos, -sin row. y' = sin, cos row. Think: "cos-sin / sin+cos"

These equations come from the quiz past paper (Q2B): "Show Laplacian is isotropic" uses x = x'cosθ − y'sinθ, y = x'sinθ + y'cosθ.

All Three — Summary Matrix

| Transform | Equations | Changes |
| --- | --- | --- |
| Translation | x'=x+tx, y'=y+ty | Position only |
| Scaling | x'=sx·x, y'=sy·y | Size (+ position) |
| Rotation | x'=x·cosθ-y·sinθ, y'=x·sinθ+y·cosθ | Orientation (+ position) |

10

# Forward vs Backward Mapping

The Problem

When you apply a geometric transform, you need to fill in the pixels of the output image. How? There are two approaches:

Forward Mapping

For each pixel in the input image, compute where it goes in the output image.

For each (x, y) in INPUT:
compute (x', y') = T(x, y)
output[x'][y'] = input[x][y]

⚠️ Problem

**Holes!** Multiple input pixels might map to the same output location, or some output pixels might get no input pixel at all (gaps appear). This makes forward mapping impractical for most use cases.

Backward (Inverse) Mapping ← Preferred

For each pixel in the output image, compute where it came from in the input image. Uses the **inverse transform T⁻¹**.

For each (x', y') in OUTPUT:
compute (x, y) = T⁻¹(x', y')
output[x'][y'] = input[x][y]

→ Every output pixel is always filled (no holes!)
→ Interpolation used when (x,y) falls between pixels

✅ Why Backward is Better

No holes in the output. Every output pixel gets a value. The input coordinates might be fractional — we use **interpolation** to handle that.

Comparison Table

| Property | Forward Mapping | Backward Mapping |
| --- | --- | --- |
| Direction | Input → Output | Output → Input |
| Transform used | T(x,y) = (x',y') | T⁻¹(x',y') = (x,y) |
| Holes in output? | Yes — problem! | No |
| Preferred? | No | Yes |
| Interpolation needed? | No | Yes (fractional coords) |

11

# Bilinear Interpolation

Why Do We Need Interpolation?

In backward mapping, the calculated source coordinates (x, y) are often fractional (e.g., 2.3, 4.7). But image pixels only exist at integer coordinates! Interpolation estimates the value at the fractional position.

Nearest Neighbor (Simplest — for comparison)

Just round to the nearest pixel. Fast but produces blocky, pixelated results.

f(2.3, 4.7) ≈ f(2, 5) ← just round

Bilinear Interpolation

Uses the 4 nearest pixels (the surrounding 2×2 square). Does linear interpolation twice — once in x, once in y.

Setup — 4 surrounding pixels
Let fractional point = (x, y) where x = i + a, y = j + b (a,b between 0 and 1)

Q11 = f(i, j) Q12 = f(i, j+1)
Q21 = f(i+1, j) Q22 = f(i+1, j+1)

Bilinear formula
f(x,y) ≈ (1-a)(1-b)·Q11 + (1-a)·b·Q12
+ a·(1-b)·Q21 + a·b·Q22

✏️ Worked Example

Find value at (1.5, 1.5). Surrounding pixels:

f(1,1)=10f(1,2)=20
f(2,1)=30f(2,2)=40

Here a = 0.5, b = 0.5

f(1.5, 1.5) = (0.5)(0.5)·10 + (0.5)(0.5)·20 + (0.5)(0.5)·30 + (0.5)(0.5)·40

= 0.25·10 + 0.25·20 + 0.25·30 + 0.25·40

= 2.5 + 5 + 7.5 + 10 = 25 (the average of all four — makes sense!)

Comparison — Interpolation Methods

| Method | Pixels Used | Quality | Speed |
| --- | --- | --- | --- |
| Nearest Neighbor | 1 | Blocky/pixelated | Fastest |
| Bilinear | 4 (2×2) | Smooth | Medium |
| Bicubic | 16 (4×4) | Best quality | Slowest |

📌 Exam Tip

Bilinear = linear interp done twice (in x, then in y). The formula weights each of the 4 neighbors by its proximity — closer neighbor gets higher weight.

⚡

# Exam Cheat Sheet

Filters — Quick Reference

| Filter | Type | Sum of weights | Use |
| --- | --- | --- | --- |
| Box / Averaging | LINEAR LOW | = 1 | Blur, noise removal |
| Weighted Average | LINEAR LOW | = 1 (center highest) | Smoother blur |
| Gaussian | LINEAR LOW | = 1 | Smooth natural blur |
| Sharpening | LINEAR HIGH | = 0 | Highlight edges |
| Laplacian (4-conn) | LINEAR HIGH | = 0 | Edge detection (2nd deriv) |
| Sobel Gx / Gy | LINEAR HIGH | = 0 | Edge detection (1st deriv) |
| Composite | LINEAR | — | f + L(x,y) = sharpened |
| Median | NON-LINEAR | N/A | Salt+pepper noise |
| Max | NON-LINEAR | N/A | Pepper (black) noise |
| Min | NON-LINEAR | N/A | Salt (white) noise |

Key Kernels to Memorize

Laplacian (4-conn)

0-10
-14-1
0-10

Sobel Gx

-10+1
-20+2
-10+1

Sobel Gy

-1-2-1
000
+1+2+1

Gaussian (÷16)

121
242
121

Formulas to Know

Laplacian: L(x,y) = 4·f(x,y) − top − bottom − left − right
Composite: C(x,y) = f(x,y) + L(x,y)
Gradient (Sobel): G ≈ |Gx| + |Gy|
Translation: x' = x + tx, y' = y + ty
Scaling: x' = sx·x, y' = sy·y
Rotation: x' = x·cosθ − y·sinθ, y' = x·sinθ + y·cosθ
Hist. Equalize: sk = (L−1) × CDF(rk)

One-Liners for MCQs

| Question | Answer |
| --- | --- |
| What removes pepper noise? | Max filter |
| What removes salt+pepper noise? | Median filter |
| Sum of weights for sharpening? | 0 |
| Sum of weights for blurring? | 1 |
| Correlation = Convolution when? | Mask is symmetric |
| Why backward mapping > forward? | No holes in output |
| Bilinear uses how many pixels? | 4 (2×2 neighborhood) |
| Laplacian is what order derivative? | 2nd |
| Sobel is what order derivative? | 1st |
| What does histogram eq improve? | Contrast (spreads intensities) |
| Translation preserves? | Shape, size, orientation |
| Low-pass keeps what frequencies? | Low (slow changes, shapes) |
| High-pass keeps what frequencies? | High (fast changes, edges) |