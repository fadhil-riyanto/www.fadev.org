# Logika

Ringkasan ini dibuat sebagian sebagian dari Kuliah IF1220 Matematika Diskrit ITB oleh bapak Rinaldi Munir. dan berbagai sumber seperti Wikipedia, ChatGPT dsb

## Proposisi
adalah pernyataan bahwa suatu dua perbandingan adalah sama besar, contoh

- \\( \frac{a}{b}=\frac{c}{d} \\)
- \\( 4 = 2 * 2 \\)
- 13 adalah bilangan ganjil
- Untuk sembarang bilangan bulat \\( n >= 0 \\), maka \\( 2n \\) adalah genap

contoh yang bukan
- Isilah gelas tersebut dengan air
- \\( x + 3 = 8 \\)
- \\( x > 3 \\)

dan, Proposisi dilambangkan dengan huruf kecil seperti \\( p, q, r, ... \\)

## Bentuk bentuk nya

- Proposisi atomik
	bentuk proposisi tunggal, contoh
	- 2n selalu genap untuk n=0, 1, 2, …
	- Ibukota Maluku Utara adalah Ternate
- proposisi majemuk
	diantaranya: 
	- conjunction (and): \\( \wedge \\)
	- disjunction (or): \\( \vee \\)
	- negation (!n): \\( ~ \\)
	- exclusive disjunction (xor): \\( \oplus \\)
	
## Table

<table border="1" cellspacing="0" cellpadding="5">
  <tr>
    <th>p</th>
    <th>q</th>
    <th>r</th>
    <th>p ∧ q</th>
    <th>¬q</th>
    <th>¬q ∧ r</th>
    <th>(p ∧ q) ∨ (¬q ∧ r)</th>
  </tr>
  <tr>
    <td>T</td>
    <td>T</td>
    <td>T</td>
    <td>T</td>
    <td>F</td>
    <td>F</td>
    <td>T</td>
  </tr>
  <tr>
    <td>T</td>
    <td>T</td>
    <td>F</td>
    <td>T</td>
    <td>F</td>
    <td>F</td>
    <td>T</td>
  </tr>
  <tr>
    <td>T</td>
    <td>F</td>
    <td>T</td>
    <td>F</td>
    <td>T</td>
    <td>T</td>
    <td>T</td>
  </tr>
  <tr>
    <td>T</td>
    <td>F</td>
    <td>F</td>
    <td>F</td>
    <td>T</td>
    <td>F</td>
    <td>F</td>
  </tr>
  <tr>
    <td>F</td>
    <td>T</td>
    <td>T</td>
    <td>F</td>
    <td>F</td>
    <td>F</td>
    <td>F</td>
  </tr>
  <tr>
    <td>F</td>
    <td>T</td>
    <td>F</td>
    <td>F</td>
    <td>F</td>
    <td>F</td>
    <td>F</td>

  </tr>
  <tr>
    <td>F</td>
    <td>F</td>
    <td>T</td>
    <td>F</td>
    <td>T</td>
    <td>T</td>
    <td>T</td>

  </tr>
  <tr>
    <td>F</td>
    <td>F</td>
    <td>F</td>
    <td>F</td>
    <td>T</td>
    <td>F</td>
    <td>F</td>

  </tr>
</table>

nb: 
- Tautologi adalah pernyataan logika yang selalu benar, tidak peduli nilai kebenaran dari komponen-komponennya. contoh
<table border="1" cellspacing="0" cellpadding="5">
  <tr>
    <th>p</th>
    <th>q</th>
    <th>p ∧ q</th>
    <th>¬(p ∧ q)</th>
    <th>p ∨ ¬(p ∧ q)</th>
  </tr>
  <tr>
    <td>T</td><td>T</td><td>T</td><td>F</td><td><span style="color:red;">T</span></td>
  </tr>
  <tr>
    <td>T</td><td>F</td><td>F</td><td>T</td><td><span style="color:red;">T</span></td>
  </tr>
  <tr>
    <td>F</td><td>T</td><td>F</td><td>T</td><td><span style="color:red;">T</span></td>
  </tr>
  <tr>
    <td>F</td><td>F</td><td>F</td><td>T</td><td><span style="color:red;">T</span></td>
  </tr>
</table>

- Kontradiksi adalah pernyataan logika yang selalu salah, tidak peduli nilai kebenaran dari komponen-komponennya. contoh
<table border="1" cellspacing="0" cellpadding="5">
  <tr>
    <th>p</th>
    <th>q</th>
    <th>p ∧ q</th>
    <th>p ∨ q</th>
    <th>¬(p ∨ q)</th>
    <th>(p ∧ q) ∧ ¬(p ∨ q)</th>
  </tr>
  <tr>
    <td>T</td><td>T</td><td>T</td><td>T</td><td>F</td><td><span style="color:red;">F</span></td>
  </tr>
  <tr>
    <td>T</td><td>F</td><td>F</td><td>T</td><td>F</td><td><span style="color:red;">F</span></td>
  </tr>
  <tr>
    <td>F</td><td>T</td><td>F</td><td>T</td><td>F</td><td><span style="color:red;">F</span></td>
  </tr>
  <tr>
    <td>F</td><td>F</td><td>F</td><td>F</td><td>T</td><td><span style="color:red;">F</span></td>
  </tr>
</table>
- ekivalen
Intinya, jika dioperasikan, dia punya hasil tabel kebenaran yang identik, walau rumusnya beda.

![gambar wikipedia hukum de morgan](https://upload.wikimedia.org/wikipedia/commons/8/83/In_Quest_of_Univeral_Logic_Morgan.png)

<table border="1" cellspacing="0" cellpadding="5">
  <tr>
    <th>p</th>
    <th>q</th>
    <th>p ∧ q</th>
    <th>¬(p ∧ q)</th>
    <th>¬p</th>
    <th>¬q</th>
    <th>¬p ∨ ¬q</th>
  </tr>
  <tr>
    <td>T</td><td>T</td><td>T</td><td><span style="color:red;">F</span></td><td>F</td><td>F</td><td><span style="color:red;">F</span></td>
  </tr>
  <tr>
    <td>T</td><td>F</td><td>F</td><td><span style="color:red;">T</span></td><td>F</td><td>T</td><td><span style="color:red;">T</span></td>
  </tr>
  <tr>
    <td>F</td><td>T</td><td>F</td><td><span style="color:red;">T</span></td><td>T</td><td>F</td><td><span style="color:red;">T</span></td>
  </tr>
  <tr>
    <td>F</td><td>F</td><td>F</td><td><span style="color:red;">T</span></td><td>T</td><td>T</td><td><span style="color:red;">T</span></td>
  </tr>
</table>


## Hukum hukum nya
| Bahasa Indonesia        | Bahasa Inggris| Contoh                                       |
|-------------------------|----------------------------|-----------------------------------------------|
| Hukum Identitas         | Identity Law               | `p ∧ T ≡ p`, `p ∨ F ≡ p`                      |
| Hukum Dominasi          | Domination Law             | `p ∨ T ≡ T`, `p ∧ F ≡ F`                      |
| Hukum Idempotensi       | Idempotent Law             | `p ∨ p ≡ p`, `p ∧ p ≡ p`                      |
| Hukum Negasi            | Negation Law               | `p ∨ ¬p ≡ T`, `p ∧ ¬p ≡ F`                    |
| Hukum Komutatif         | Commutative Law            | `p ∨ q ≡ q ∨ p`, `p ∧ q ≡ q ∧ p`              |
| Hukum Asosiatif         | Associative Law            | `(p ∨ q) ∨ r ≡ p ∨ (q ∨ r)`                  |
| Hukum Distributif       | Distributive Law           | `p ∨ (q ∧ r) ≡ (p ∨ q) ∧ (p ∨ r)`            |
| Hukum De Morgan         | De Morgan’s Laws           | `¬(p ∧ q) ≡ ¬p ∨ ¬q`, `¬(p ∨ q) ≡ ¬p ∧ ¬q`    |
| Hukum Involusi          | Double Negation / Involution | `¬(¬p) ≡ p`                                |
| Hukum Implikasi         | Implication Law            | `p → q ≡ ¬p ∨ q`                             |
| Hukum Biimplikasi       | Biconditional Law          | `p ↔ q ≡ (p → q) ∧ (q → p)`                  |

## Implikasi
Disebut juga proposisi bersyarat, seperti jika x maka y, notasinya \\( p \rightarrow q\\). \\( p \\) nya adalah condition, \\( q \\) nya adalah conlusion

| p   | q   | p → q |
|-----|-----|--------|
| T   | T   | T      |
| T   | F   | F      |
| F   | T   | T      |
| F   | F   | T      |

versi versinya jika dijadikan teks
- Jika p, maka q (if p, then q)
- Jika p, q (if p, q)
- p mengakibatkan q (p implies q)
- q jika p (q if p)
- p hanya jika q (p only if q)
- p syarat cukup untuk q (p is sufficient condition for q)
- q syarat perlu bagi p (q is necessary condition for q)
- q bilamana p (q whenever p)
- q mengikuti dari p (q follows from p)

### penjelasan kenapa \\( F \rightarrow F = T \\)
```
“If I win the lottery, I’ll buy you a car.”
I didn't win the lottery → (False)

I didn't buy a car → (False)
```
dan juga \\( P \rightarrow Q \\) sebenarnya sama dengan \\( \sim{P} \vee Q \\)

### Penjelasan kenapa \\( \sim (p \rightarrow q )\\) itu sama dengan \\( p \space \wedge \sim{q} \\)
Kita tahu bahwa \\( p \rightarrow q \\) itu sebenarnya sama dengan \\( \sim{p} \vee p \\) , maka steps yang dibutuhkan hanya

- \\( \sim(p \rightarrow q) \\)
- \\( \sim(\sim{p} \vee q) \\)
- \\( p \space \wedge \sim{q} \\)


### tabel varian implikasi (Proporsi bersyarat)

- Konvers (kebalikan): \\( q \rightarrow p \\)
- Invers : \\( \sim p \rightarrow \sim q \\)
- Kontraposisi : \\( \sim q \rightarrow \sim p \\)


| p   | q   | ¬p  | ¬q  | p → q | q → p | ¬p → ¬q | ¬q → ¬p |
|-----|-----|-----|-----|--------|--------|-----------|-----------|
| T   | T   | F   | F   | T      | T      | T         | T         |
| T   | F   | F   | T   | F      | T      | T         | F         |
| F   | T   | T   | F   | T      | F      | F         | T         |
| F   | F   | T   | T   | T      | T      | T         | T         |

## Bi-impication 
Intinya, operand kanan kiri harus sama, entah sama sama true, atau sama sama false. 
notasinya: \\( p \leftrightarrow q \\)

tabel kebenaran

| p | q | p ↔ q |
|:-:|:-:|:-----:|
| T | T |   T   |
| T | F |   F   |
| F | T |   F   |
| F | F |   T   |

contoh

| p | q | p ↔ q | p → q | q → p | (p → q) ∧ (q → p) |
|:-:|:-:|:-----:|:-----:|:-----:|:------------------:|
| T | T |   T   |   T   |   T   |         T          |
| T | F |   F   |   F   |   T   |         F          |
| F | T |   F   |   T   |   F   |         F          |
| F | F |   T   |   T   |   T   |         T          |

analogi simple:
- `Jika suatu bilangan genap, maka habis dibagi 2`: \\( \text{true} \leftrightarrow \text{true} = \text{true} \\)

- `Jika suatu bilangan bukan genap, maka tidak akan habis dibagi 2`: \\( \text{false} \leftrightarrow \text{false} = \text{true} \\)