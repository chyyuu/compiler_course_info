# SLR Parser

Implementation of Simple LR (SLR) Parser for educational purposes.

```
$ slr -g grammar.txt "id + id * id"
AUGMENTED GRAMMAR:
0: E' -> E
1:  E -> E + T
2:  E -> T
3:  T -> T * F
4:  T -> F
5:  F -> ( E )
6:  F -> id

   TERMINALS: ), id, +, *, (
NONTERMINALS: E, F, E', T
     SYMBOLS: ), E, id, +, T, *, F, E', (

FIRST:
E' = { id, ( }
 E = { id, ( }
 T = { id, ( }
 F = { id, ( }

FOLLOW:
E' = { $ }
 E = { $, ), + }
 T = { ), +, $, * }
 F = { ), +, $, * }

PARSING TABLE:
+--------+-----------------------------------------------------+--------------------------+
|        |                       ACTION                        |           GOTO           |
| STATE  +--------+--------+--------+--------+--------+--------+--------+--------+--------+
|        |    )   |   id   |    +   |    *   |    (   |    $   |    E   |    F   |    T   |
+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+
|   0    |        |   s2   |        |        |   s5   |        |    1   |    4   |    3   |
|   1    |        |        |   s6   |        |        |   acc  |        |        |        |
|   2    |   r6   |        |   r6   |   r6   |        |   r6   |        |        |        |
|   3    |   r2   |        |   r2   |   s7   |        |   r2   |        |        |        |
|   4    |   r4   |        |   r4   |   r4   |        |   r4   |        |        |        |
|   5    |        |   s2   |        |        |   s5   |        |    8   |    4   |    3   |
|   6    |        |   s2   |        |        |   s5   |        |        |    4   |    9   |
|   7    |        |   s2   |        |        |   s5   |        |        |   10   |        |
|   8    |   s11  |        |   s6   |        |        |        |        |        |        |
|   9    |   r1   |        |   r1   |   s7   |        |   r1   |        |        |        |
|   10   |   r3   |        |   r3   |   r3   |        |   r3   |        |        |        |
|   11   |   r5   |        |   r5   |   r5   |        |   r5   |        |        |        |
+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+

+------+--------------+-------------+----------------+----------------------+
|      |    STACK     |   SYMBOLS   |     INPUT      |        ACTION        |
+------+--------------+-------------+----------------+----------------------+
|  (1) | 0            |             | id + id * id $ | shift                |
|  (2) | 0 2          |  id         |    + id * id $ | reduce by F -> id    |
|  (3) | 0 4          |  F          |    + id * id $ | reduce by T -> F     |
|  (4) | 0 3          |  T          |    + id * id $ | reduce by E -> T     |
|  (5) | 0 1          |  E          |    + id * id $ | shift                |
|  (6) | 0 1 6        |  E +        |      id * id $ | shift                |
|  (7) | 0 1 6 2      |  E + id     |         * id $ | reduce by F -> id    |
|  (8) | 0 1 6 4      |  E + F      |         * id $ | reduce by T -> F     |
|  (9) | 0 1 6 9      |  E + T      |         * id $ | shift                |
| (10) | 0 1 6 9 7    |  E + T *    |           id $ | shift                |
| (11) | 0 1 6 9 7 2  |  E + T * id |              $ | reduce by F -> id    |
| (12) | 0 1 6 9 7 10 |  E + T * F  |              $ | reduce by T -> T * F |
| (13) | 0 1 6 9      |  E + T      |              $ | reduce by E -> E + T |
| (14) | 0 1          |  E          |              $ | accept               |
+------+--------------+-------------+----------------+----------------------+
```

<p align="center">
  <img src="example.jpg">
  <br/>
</p>

# Installation

## Requirements
* Python 3.6+

## Stable release

To install slr-parser, run this command in your terminal:

```
pip install slr-parser
```

This is the preferred method to install slr-parser, as it will always install the most recent stable release.

If you don't have [pip](https://pip.pypa.io) installed, this [Python installation guide](http://docs.python-guide.org/en/latest/starting/installation/) can guide you through the process.

## From sources

The sources for slr-parser can be downloaded from the [Github repo](https://github.com/Vipul97/slr-parser).

You can either clone the public repository:

```
git clone git://github.com/Vipul97/slr-parser
```

Or download the [tarball](https://github.com/Vipul97/slr-parser/tarball/master):

```
curl -OJL https://github.com/Vipul97/slr-parser/tarball/master
```

Once you have a copy of the source, you can install it with:

```
python setup.py install
```

# Usage

## Grammar Syntax
* For every production, the head and the body of the production is separated by ``` -> ```.
* Capitalized symbols are treated as nonterminals and non-capitalized symbols are treated as terminals.
* All symbols in the body of the production are separated by spaces. Multicharacter symbols can be made by not including spaces between the characters.
* The choice operator ``` | ``` can be used in the body of the production to match either the expression before or the expression after the operator.
* ```^``` is treated as the null symbol.

## Grammar File
A text file containing the grammar is required. For example, the contents of a grammar file ```grammar.txt``` looks like this:

```
E -> E + T
E -> T
T -> T * F | F
F -> ( E )
F -> id
```

## Tokens
The tokens enclosed within double quotes are required as the input to the SLR Parser. All tokens are separated with spaces. For example, ```"id + id * id"```.

    usage: slr [-h] [-g] grammar_file tokens

    positional arguments:
      grammar_file  text file to be used as grammar
      tokens        tokens to be parsed - all tokens are separated with spaces

    optional arguments:
      -h, --help    show this help message and exit
      -g            generate automaton

# Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on code of conduct, and the process for submitting pull requests.

# License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
