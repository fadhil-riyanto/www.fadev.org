# Set operations formula

### Union of Two Sets (cardinality)

\\[
|A \cup B| = |A| + |B| - |A \cap B|
\\]

how to read:
whole `A` and `B` add together, its make a data duplication on center of venn diagram, we remove that duplication using \\( |A \cap B|  \\)

### Intersection (steps)
its flip of Union
\\[ |A \cup B| = |A| + |B| - |A \cap B| \\]
\\[ |A \cap B| = |A| + |B| - |A \cup B| \\]

### Intersection of three sets
\\[ |A \cup B \cup C| = |A| + |B| + |C| - |A \cap B| - |A \cap C| - |B \cap C| + |A \cap B \cap C| \\]

how it works, de remove data duplication two times on \\( |A \cap B| \\), \\( |B \cap C| \\), and \\( |B \cap C| \\), then fill the empty section on the center which \\( |A \cap B \cap C| \\)

This is proof of concept by nice guy on internet: [https://www.youtube.com/watch?v=vVZwe3TCJT8](https://www.youtube.com/watch?v=vVZwe3TCJT8).

### Difference
\\[ |A - B| = |A| - |A \cup B| \\]

### Symetric difference
#### 1. General formula
\\[
A \space \triangle \space B = (A \cup B) - (A \cap B) 
\\]
Cardinals version:
\\[
| A \space \triangle \space B | = |A - B| + |B - A| 
\\]
\\[
| A \space \triangle \space B | = |A| + |B| - 2|A \cap B|
\\]

#### 2. Symetric difference properties
- \\(
 A \space \triangle \space B  =  B \space \triangle \space A 
\\)
- \\(
 (A \space \triangle \space B) \space \triangle C  =  A \space \triangle \space (B \space \triangle C)
\\)
- \\(
 (A \space \triangle \space \emptyset) =  A
\\), why?
	- \\(A \space \triangle \space B = (A \cup B) - (B \cap A) \\)
	- \\(A \space \triangle \space \emptyset = (A \cup \emptyset) - (\emptyset \cap A) \\), but
	- \\( (A \cup \emptyset) = A \\) and \\( (\emptyset \cap A) = \emptyset \\) 
	- \\( (A - \emptyset) = A \\)
	
	
- \\(
 (A \space \triangle \space A) =  \emptyset
\\)