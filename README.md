
<h1 align="center">
  Matn | مَتن
  <br>
  <a href="https://github.com/iamjazzar/matn/actions/workflows/ci.yml">
    <img style="max-width: 100%;" alt="Tests" src="https://github.com/iamjazzar/matn/actions/workflows/ci.yml/badge.svg" />
  </a>
  <a href="https://badge.fury.io/py/matn">
    <img style="max-width: 100%;" alt="Tests" src="https://badge.fury.io/py/matn.svg" />
  </a>
</h1>
<p align="center">
  <a href="https://www.ahmedjazzar.com/">
<img width="350" alt="Screen Shot 2022-06-04 at 4 45 04 PM" src="https://user-images.githubusercontent.com/11036472/172029190-94d06808-9b70-487c-a83a-52549e43d5e7.png">

  </a>
</p>
<p align="center">
  <br>
    A shared space for Arabic text processors.
  <br>
</p>


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
1. The method that considers hamza as a seperate character.
1. The tarkeeb method; Used to express the numbers from 2000 to 1,000,000, using the rule based on the letter "غ". The rule is fairly simple, any character that comes before "غ" its value will be multiplied with 1000 instead of accumalated to it.
1. Normalized hamzas method, where we treat all hamza forms as a regular alef instead of the letter it appears on. Defaults to False.

#### Usage
##### Python
```python
>>> from matn import jummal

>>> text = "شغل الدموع عن الديار بكاؤنا   لبكاء فاطمــة على أولادها"

>>> jummal(text)
2_273  # شغ's value is 1000 + 300 and hamza value is 0

# To include Hamza count
>>> jummal(text, use_hamza=True)
2_274  # شغ's value is 1000 + 300 and hamza value is 1

# To include hamza normalization
>>> jummal(text, normalize_hamza=True)
2_268  # شغ's value is 1000 + 300, hamza value is 1, and ؤ value is 1

# To use tarkeeb
jummal(text, use_tarkeeb=True)
300_973  # شغ's value is 300 * 1000 and hamza value is 0

# To use hamza and tarkeeb
jummal(text, use_hamza=True, use_tarkeeb=True)
300_974  # شغ's value is 300 * 1000 and hamza value is 1
```

##### CLI
```shell
matn jummal "شغل الدموع عن الديار بكاؤنا   لبكاء فاطمــة على أولادها"

# To include Hamza count
matn jummal --use-hamza "شغل الدموع عن الديار بكاؤنا   لبكاء فاطمــة على أولادها"

# To use tarkeeb
matn jummal --use-tarkeeb "شغل الدموع عن الديار بكاؤنا   لبكاء فاطمــة على أولادها"

# To normalize hamza
matn jummal --normalize-hamza "شغل الدموع عن الديار بكاؤنا   لبكاء فاطمــة على أولادها"

# All methods at once
matn jummal -z -n -t  "شغل الدموع عن الديار بكاؤنا   لبكاء فاطمــة على أولادها"
```
