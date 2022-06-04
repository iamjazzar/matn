# Matn | مَتن [![Tests](https://github.com/iamjazzar/matn/actions/workflows/ci.yml/badge.svg)](https://github.com/iamjazzar/matn/actions/workflows/ci.yml) [![PyPI version](https://badge.fury.io/py/matn.svg)](https://badge.fury.io/py/matn)

A Python mathematical tool for simple access to Arabic letters counting systems.


## About
This library is just a host for all possible [processors](#processors) required to do the counting over Arabic text.


## Getting started

```bash
pip install matn
```
## Processors
### Jummal | حِسَاب ٱلْجُمَّل
Or Abjad numerals, a decimal alphabetic numeral system/alphanumeric code, in which the 28 letters of the Arabic alphabet are assigned numerical values. They have been used in the Arabic-speaking world since before the eighth century when positional Arabic numerals were adopted.

#### Methods
There are different ways and values people use for jummal.
1. The normal method which doesn't include the hamza count.
2. The method that considers hamza as a seperate character.
3. The tarkeeb method; Used to express the numbers from 2000 to 1,000,000, using the rule based on the letter "غ". The rule is fairly simple, any character that comes before "غ" its value will be multiplied with 1000 instead of accumalated to it.

#### Usage
```python
>>> from matn import jummal

>>> text = "شغل الدموع عن الديار بكاؤنا   لبكاء فاطمــة على أولادها"

>>> jummal(text)
2_273  # شغ's value is 1000 + 300 and hamza value is 0

# To include Hamza count
>>> jummal(text, use_hamza=True)
2_274  # شغ's value is 1000 + 300 and hamza value is 1

# To use tarkeeb
jummal(text, use_tarkeeb=True)
300_973  # شغ's value is 300 * 1000 and hamza value is 0

# To use hamza and tarkeeb
jummal(text, use_hamza=True, use_tarkeeb=True)
300_974  # شغ's value is 300 * 1000 and hamza value is 1
```
