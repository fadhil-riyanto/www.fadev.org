# Set stuff

there is some intresting question about discrete math


## why \\( \mathcal{P}(\emptyset) = \lbrace \emptyset \rbrace \\)
consider \\( \mathcal(S) \\) where \\( S \\) is a set, for example

- if \\( S = \lbrace a \rbrace \\), then \\( \mathcal{P}(S) = \lbrace \emptyset, \lbrace a \rbrace \rbrace \\), same as \\( \mathcal{P}(a) \\)
- if \\( S = \lbrace a, b \rbrace \\), then \\( 
													\mathcal{P}(S) = \lbrace 
																			\emptyset, 
																			\lbrace a \rbrace,
																			\lbrace b \rbrace,
																			\lbrace a, b \rbrace 
																	 \rbrace \\), same as \\( \mathcal{P}(a, b) \\)
- if \\( S = \lbrace \emptyset \rbrace \\), then \\( \mathcal{P}(S) = \lbrace \emptyset, \lbrace \emptyset \rbrace \rbrace \\), same as \\( \mathcal{P}(\emptyset) \\)

so, because \\( \lbrace \rbrace \\) usually hidden, \\( \mathcal{P}(\emptyset) = \lbrace \emptyset \rbrace \\)

## let \\( A = \emptyset, B = \emptyset \\), how to \\( A \times B \\)
Consider \\( A \times B = \lbrace (a,b) | a \in A, b \in B \rbrace \\)

because
- A is empty, no elements can be paired
- B is also empty

conlusion: no paired element = empty

proof by cardinality
\\(
|A| = 0, |B| = 0, \text{so, when } |A \times B| = |A| \times |B| = 0 \times 0 = 0
\\)

## does \\( P(\emptyset) = \lbrace \lbrace \rbrace \rbrace = \lbrace \emptyset \rbrace \\) ?
true, this is due \\( \lbrace \emptyset \rbrace \\) same as \\( \lbrace \lbrace \rbrace \rbrace \\), then consider example 
\\( P(a) = \lbrace \lbrace \rbrace, \lbrace a \rbrace\rbrace \\)

## Suppose X and Z are independent of each other
- \\( | \mathcal{P}(X \cap Z)| \\)
- \\( | X - Z | \\)
- \\( | X \oplus Z | \\)
- \\( | X \cap Z | \\)
- \\( | \mathcal{P}(X) \cup \mathcal{P}(Z)| \\)
- \\( | \overline{\mathcal{P}(X) \cup \mathcal{P}(Z)}| \\)

nb: bagian ini belum jadi