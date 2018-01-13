# Primality test

Fermat primality tests using modular exponentiation.

## Running the tests

Since Fermat is a probabilistic test to determine if a number is a prime in the tests I tried to trick the Algorithm by using many semiprime numbers.

### Inputs

The inputs for these test were the following ([semiprimes](http://oeis.org/A066265)):

```
3, 34, 299, 2625, 23378, 210035, 1904324, 17427258, 160788536, 1493776443, 13959990342
```

And also, real primes:

```
11, 13, 17, 209669, 143555297
```

Finally, the algorithm ran for k = 1000 tries and 100000 tries.

### Outputs

The output table is formatted as:

The number, number of times it was counted as prime, number of times it was counted as not prime, the percentage of the time that was counted as prime or not, and the algorithm's final verdict as to whether it it prime or not.


Output for k = 1000
```
Table output
```

Output for k = 100000
```
Table output
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* Algorithms - S. Dasgupta, C. H. Papadimitriou, and U. V. Vazirani
