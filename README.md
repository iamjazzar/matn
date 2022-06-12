
<h1 align="center">
  Matn | مَتن
  <br>
  <a href="https://github.com/iamjazzar/matn/actions/workflows/ci.yml">
    <img style="max-width: 100%;" alt="Tests" src="https://github.com/iamjazzar/matn/actions/workflows/ci.yml/badge.svg" />
  </a>
  <a href="https://badge.fury.io/py/matn">
    <img style="max-width: 100%;" alt="Tests" src="https://badge.fury.io/py/matn.svg" />
  </a>
  <a href="https://github.com/iamjazzar/matn/actions/workflows/codeql-analysis.yml">
    <img src="https://github.com/iamjazzar/matn/actions/workflows/codeql-analysis.yml/badge.svg" />
  </a>
</h1>
<p align="center">
  <a href="https://www.ahmedjazzar.com/">
  <picture>
      <source srcset="https://user-images.githubusercontent.com/11036472/172036047-b60ad299-e30f-4a16-85f7-645d95edd1b8.png" media="(prefers-color-scheme: dark)" />
      <img width="400" id="screenshot" src="https://user-images.githubusercontent.com/11036472/172036055-b0a9c55c-3986-411d-955f-790130c49c27.png" />
    </picture>
  </a>
</p>
<p align="center">
  <br>
    A shared space for Arabic text processors.
  <br>
</p>


## 1. Getting started

```bash
pip install matn
```
## 2. Counters
### 2.1. Jummal | حِسَاب ٱلْجُمَّل
Or Abjad numerals, a decimal alphabetic numeral system/alphanumeric code, in which the 28 letters of the Arabic alphabet are assigned numerical values. They have been used in the Arabic-speaking world since before the eighth century when positional Arabic numerals were adopted.

#### 2.1.1. Methods
There are different ways and values people use for jummal.
1. The normal method which doesn't include the hamza count.
1. The method that considers hamza as a seperate character.
1. The tarkeeb method; Used to express the numbers from 2000 to 1,000,000, using the rule based on the letter "غ". The rule is fairly simple, any character that comes before "غ" its value will be multiplied with 1000 instead of accumalated to it.
1. Normalized hamzas method, where we treat all hamza forms as a regular alef instead of the letter it appears on. Defaults to False.

#### 2.1.2. Usage
##### Python
```python
>>> from matn.counters import jummal

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
>>> jummal(text, use_tarkeeb=True)
300_973  # شغ's value is 300 * 1000 and hamza value is 0

# To use hamza and tarkeeb
>>> jummal(text, use_hamza=True, use_tarkeeb=True)
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

### 2.2. Word Count
Counts the number of characters in a given string.

#### 2.2.1. Methods
The method is very obvious. However, some researchers tend to split words into multiple parts. The only word we took interest in, so far, is بعدما. The `word_count` method will give you the option to split it into two words or count it as one.

#### 2.2.2. Usage
##### Python
```python
>>> from matn.counters import word_count

>>> text = "فَمَنۢ بَدَّلَهُۥ بَعۡدَمَا سَمِعَهُۥ"

>>> word_count(text)
4

# To split badama
>>> word_count(text, split_badama=True)
5  # بَعۡدَمَا was split into two words
```

##### CLI
```shell
matn wc "فَمَنۢ بَدَّلَهُۥ بَعۡدَمَا سَمِعَهُۥ"

# To split badama
matn wc --split-badama "فَمَنۢ بَدَّلَهُۥ بَعۡدَمَا سَمِعَهُۥ"
```

### 2.3. Char Count
Counts the number of characters in a given string.

#### 2.3.1. Methods
- In some cases, we need to consinder spaces as seperate characters, in some cases we don't.
- In some cases, we consider the hamza-madda (أٓ) character two characters. This character appears in the word الأٓخرة for example.

#### 2.3.2. Usage
##### Python
```python
>>> from matn.counters import char_count

>>> text = "ٱلدَّارُ ٱلۡأٓخِرَةُ"

>>> char_count(text)
11

# To Include spaces
>>> char_count(text, include_spaces=True)
12

# To Include hamza-madda
>>> char_count(text, hamza_madda=True)
12

# To Include hamza-madda and spaces
>>> char_count(text, hamza_madda=True)
13
```

##### CLI
```shell
matn cc "ٱلدَّارُ ٱلۡأٓخِرَةُ"

# To Include hamza-madda
matn wc --hamza-madda "فَمَنۢ بَدَّلَهُۥ بَعۡدَمَا سَمِعَهُۥ"

# To Include spaces
matn wc --include-spaces "فَمَنۢ بَدَّلَهُۥ بَعۡدَمَا سَمِعَهُۥ"

# To Include hamza-madda and spaces
matn wc --include-spaces --hamza-madda "فَمَنۢ بَدَّلَهُۥ بَعۡدَمَا سَمِعَهُۥ"
```
