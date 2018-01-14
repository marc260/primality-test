# Primality test

Fermat primality tests using modular exponentiation.

## Pseudocode

### Modular exponentiation

```python
function modexp(x,y,N)
Input: Two n-bit integers x and N, an integer exponent y
Output: x y mod N

if y = 0: return 1
z = modexp(x,floor(y/2),N)
if y is even:
    return z 2 mod N
else:
    return x · z 2 mod N
```

### Fermat 

```python
function primality(N)
Input: Positive integer N
Output: yes/no

Pick a positive integer a < N at random
if a N−1 ≡ 1 (mod N):
    return yes
else:
    return no
```

## Running the tests

Since Fermat is a probabilistic test to determine if a number is a prime in the tests I tried to trick the Algorithm by using many semiprime numbers.

### Inputs

The inputs for these test were the following ([semiprimes](http://oeis.org/A066265)):

```
2625, 23378, 210035, 1904324, 17427258, 160788536, 1493776443, 13959990342
```

And also, real primes:

```
209669, 104743, 105023, 105359, 105613
```

Finally, the algorithm ran for k = 100 tries.

### Outputs

The output table is formatted as:

The number, number of times it was counted as prime, number of times it was counted as not prime, the percentage of the time that was counted as prime or not, and the algorithm's final verdict as to whether it it prime or not.

Output for k = 100
```
Enter N: 2625, 23378, 210035, 1904324, 17427258, 160788536, 1493776443, 13959990342, 209669, 104743, 105023, 105359, 105613
Enter k: 100
------------------------------------------------------------------
N           Passed    !Passed   Prime?              Yes %     Not %     
2625        0         100       !Prime              0.000	100.000
23378       0         100       !Prime              0.000	100.000
210035      0         100       !Prime              0.000	100.000
1904324     0         100       !Prime              0.000	100.000
17427258    0         100       !Prime              0.000	100.000
160788536   0         100       !Prime              0.000	100.000
1493776443  0         100       !Prime              0.000	100.000
13959990342 0         100       !Prime              0.000	100.000
209669      100       0         Prime               100.000	0.000
104743      100       0         Prime               100.000	0.000
105023      100       0         Prime               100.000	0.000
105359      100       0         Prime               100.000	0.000
105613      100       0         Prime               100.000	0.000
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* Algorithms - S. Dasgupta, C. H. Papadimitriou, and U. V. Vazirani
