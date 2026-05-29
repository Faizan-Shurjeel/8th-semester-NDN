# Gray Level Co-occurrence Matrix (GLCM) – Detailed Beginner Explanation

Given Image :

2 1 2 4
4 1 2 2
1 5 4 3
5 4 5 1
2 3 1 3

Gray levels present: {1,2,3,4,5}
So GLCM size = 5 × 5

---------------------------------
WHAT IS GLCM?
---------------------------------
A Gray Level Co-occurrence Matrix (GLCM) is a table that counts how often a pixel with value i occurs with a neighboring pixel with value j for a specified direction (position operator).

Rows represent reference pixel values.
Columns represent neighboring pixel values.

---------------------------------
POSITION OPERATOR 1
---------------------------------
Definition: One pixel to the right and one pixel down.
Direction: Diagonal down-right.

Procedure:
1. Select a pixel.
2. Move one step to the right AND one step down.
3. Record the pair (current pixel, neighbor pixel).

Valid pixel pairs obtained:
(2,1), (1,2), (2,2), (4,5), (1,4), (2,3), (1,4), (5,1), (4,1), (5,3), (4,1), (5,3)

GLCM for Operator 1:

Row\Col 1 2 3 4 5
1 0 1 0 2 0
2 1 1 1 0 0
3 0 0 0 0 0
4 2 0 1 0 1
5 1 0 2 0 0

---------------------------------
POSITION OPERATOR 2
---------------------------------
Definition: One pixel to the left and one pixel up.
Direction: Diagonal up-left.

Important concept:
This direction is the reverse of Operator 1.
Therefore, GLCM for Operator 2 is the TRANSPOSE of GLCM for Operator 1.

GLCM for Operator 2 (Transpose):

Row\Col 1 2 3 4 5
1 0 1 0 2 1
2 1 1 0 0 0
3 0 1 0 1 2
4 2 0 0 0 0
5 0 0 0 1 0

---------------------------------
SUMMARY
---------------------------------
• GLCM is a counting matrix.
• Operator defines neighbor direction.
• Operator 1 counts diagonal down-right neighbors.
• Operator 2 counts diagonal up-left neighbors.
• Operator 2 matrix is transpose of Operator 1.