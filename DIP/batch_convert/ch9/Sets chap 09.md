**1. What is a Set?**

A **set** is a collection of items (elements).

**Examples:**

A = {1, 2, 3}
B = {3, 4, 5}

**2. Element of a Set ( ∈ and ∉ )**

**Meaning**

* a ∈ A → “a is inside A”
* a ∉ A → “a is NOT inside A”

**Example**

Let:
A = {1, 2, 3}

Then:
2 ∈ A (true)
5 ∈ A (false)
5 ∉ A (true)

**3. Subset ( ⊆ )**

**Meaning**

A ⊆ B → All elements of A are inside B

**Example**

A = {1, 2}
B = {1, 2, 3, 4}

A ⊆ B (true)
(because every element of A is in B)

**4. Union ( ∪ )**

**Meaning**

Combine all elements from both sets (no repetition)

C = A ∪ B

**Example**

A = {1, 2, 3}
B = {3, 4, 5}

A ∪ B = {1, 2, 3, 4, 5}

**5. Intersection ( ∩ )**

**Meaning**

Common elements in both sets

D = A ∩ B

**Example**

A = {1, 2, 3}
B = {3, 4, 5}

A ∩ B = {3}

**6. Disjoint Sets**

**Meaning**

Two sets are disjoint if they have no common elements

A ∩ B = ∅

(∅ means empty set)

**Example**

A = {1, 2}
B = {3, 4}

A ∩ B = ∅

**7. Complement ( Aᶜ )**

**Meaning**

All elements that are **NOT in A**

Aᶜ = { ω | ω ∉ A }

(Read as: set of all elements ω such that ω is not in A)

**Example**

Universal Set:
U = {1, 2, 3, 4, 5}

Let:
A = {1, 2, 3}

Then:
Aᶜ = {4, 5}

**8. Difference ( A − B )**

**Meaning**

Elements that are in A but NOT in B

A − B = { ω | ω ∈ A and ω ∉ B }

Also written as:
A − B = A ∩ Bᶜ

**Example**

A = {1, 2, 3}
B = {3, 4, 5}

A − B = {1, 2}

**Why A − B = A ∩ Bᶜ ?**

Step-by-step:

Universal Set:
U = {1, 2, 3, 4, 5}

B = {3, 4, 5}

Bᶜ = {1, 2}

Now:
A ∩ Bᶜ = {1, 2, 3} ∩ {1, 2} = {1, 2}

Same result as A − B

**9. Key Concepts Summary**

| **Symbol** | **Meaning** |
| --- | --- |
| ∈ | inside |
| ∉ | not inside |
| ⊆ | subset |
| ∪ | union (combine) |
| ∩ | intersection (common) |
| ∅ | empty set |
| Aᶜ | complement (outside A) |
| A − B | difference (remove B from A) |

**10. One-line Summary**

* Union → Combine elements
* Intersection → Common elements
* Complement → Opposite elements
* Difference → Subtract one set from another