**1. Morphology (Overview)**

Morphology is a set of image processing techniques that analyze and manipulate the **shape and structure** of objects in an image. It is mainly applied to **binary images** (where pixels are 0 or 1), but it can also be extended to grayscale images.

Morphological operations use a small matrix called a **Structuring Element (SE)**. This SE is placed over the image and moved (slid) across it. At each position, a rule is applied to the pixels covered by the SE (called “pixels under the SE”) to produce the output pixel.

**Key uses:**

* Noise removal
* Shape extraction
* Boundary detection
* Object separation and connection

**2. Structuring Element (SE)**

A structuring element is a small matrix (commonly 3×3) used to probe the image.

Example SE:

1 1 1
1 1 1
1 1 1

The SE is centered on each pixel of the image, and the values covered by it are used to compute the output.

**3. Erosion**

Erosion is a morphological operation that **shrinks objects** in an image.

**Rule**

The output pixel is **1 only if all pixels under the SE are 1**.
Otherwise, the output is 0.

**Effect**

* Removes boundary pixels
* Eliminates small noise
* Breaks thin connections

**Example 1 (Erosion)**

**Input Image**

0 1 1 1 0 0
1 1 1 1 1 0
1 1 1 1 1 1
0 1 1 1 1 0
0 0 1 1 0 0
0 0 0 0 0 0

**Step Explanation**

We check only inner pixels.

**Check pixel (3,3):**

Neighborhood:

1 1 1
1 1 1
1 1 1

All 1 → Output = 1

**Check pixel (2,2):**

0 1 1
1 1 1
1 1 1

Contains 0 → Output = 0

**Check pixel (4,4):**

1 1 1
1 1 1
1 0 0

Contains 0 → Output = 0

**Final Output (Erosion)**

0 0 0 0 0 0
0 0 0 0 0 0
0 0 1 1 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0

**Example 2 (Erosion)**

**Input Image**

0 0 1 1 1 0
0 1 1 1 1 1
1 1 1 1 1 1
1 1 1 1 1 0
0 1 1 1 0 0
0 0 0 0 0 0

**Key Checks**

**Center region:**

1 1 1
1 1 1
1 1 1

→ Output = 1

**Edge regions contain 0 → Output = 0**

**Final Output**

0 0 0 0 0 0
0 0 0 1 0 0
0 0 1 1 1 0
0 0 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0

**4. Dilation**

Dilation is a morphological operation that **expands objects** in an image.

**Rule**

The output pixel is **1 if at least one pixel under the SE is 1**.

**Effect**

* Adds pixels to boundaries
* Fills small holes
* Connects nearby objects

**Example 1 (Dilation)**

**Input Image**

0 1 1 1 0 0
1 1 1 1 1 0
1 1 1 1 1 1
0 1 1 1 1 0
0 0 1 1 0 0
0 0 0 0 0 0

**Step Explanation**

**Check pixel (1,1):**

0 1 1
1 1 1
1 1 1

Contains 1 → Output = 1

**Check pixel (5,5):**

1 0 0
1 0 0
0 0 0

Contains 1 → Output = 1

**Final Output (Dilation)**

1 1 1 1 1 0
1 1 1 1 1 1
1 1 1 1 1 1
1 1 1 1 1 1
0 1 1 1 1 0
0 0 1 1 0 0

**Example 2 (Dilation )**

**Input Image**

0 0 0 0 0
0 1 0 1 0
0 0 0 0 0
0 1 0 0 0
0 0 0 0 0

**Step**

Each 1 expands into a 3×3 region.

**Final Output**

1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 0
1 1 1 0 0

**5. Key Differences**

|  |  |  |
| --- | --- | --- |
| Operation | Condition | Effect |
| Erosion | All values under SE must be 1 | Shrinks object |
| Dilation | At least one value under SE is 1 | Expands object |

**6. Important Notes**

* “Under SE” means the **3×3 neighborhood covered when SE is centered on a pixel**
* Output is calculated **pixel-by-pixel**
* Erosion is strict (like AND)
* Dilation is relaxed (like OR)