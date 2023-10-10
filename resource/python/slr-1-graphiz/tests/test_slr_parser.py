from slr_parser.grammar import Grammar
from slr_parser.slr_parser import SLRParser, first_follow
import unittest


class TestSLRParser(unittest.TestCase):
    def setUp(self):
        with open('tests/test_grammar.txt') as grammar_file:
            self.G = Grammar(grammar_file.read())
            self.slr_parser = SLRParser(self.G)

    def test_first_follow(self):
        grammar_strs = ["""E -> E + T
E -> T
T -> T * F | F
F -> ( E )
F -> id""", """E -> T E'
E' -> + T E' | ^
T -> F T'
T' -> * F T' | ^
F -> ( E ) | id""", """E -> T X
X -> + E
X -> ^
T -> int Y
T -> ( E )
Y -> * T
Y -> ^""", """S -> a B D h
B -> c C
C -> b C | ^
D -> E F
E -> g | ^
F -> f | ^""", """S -> A
A -> a B | A d
B -> b
C -> g""", """S -> ( L ) | a
L -> S L'
L' -> , S L' | ^""", """S -> A a A b | B b B a
A -> ^
B -> ^""", """S -> A C B | C b B | B a
A -> d a | B C
B -> g | ^
C -> h | ^"""]

        with self.subTest(grammar_str=grammar_strs[0]):
            G = Grammar(grammar_strs[0])
            first, follow = first_follow(G)
            self.assertSetEqual({'(', 'id'}, first['E'])
            self.assertSetEqual({'(', 'id'}, first['T'])
            self.assertSetEqual({'(', 'id'}, first['F'])
            self.assertSetEqual({'$', '+', ')'}, follow['E'])
            self.assertSetEqual({'$', '+', '*', ')'}, follow['T'])
            self.assertSetEqual({'$', '+', '*', ')'}, follow['F'])

        with self.subTest(grammar_str=grammar_strs[1]):
            G = Grammar(grammar_strs[1])
            first, follow = first_follow(G)
            self.assertSetEqual({'(', 'id'}, first['E'])
            self.assertSetEqual({'(', 'id'}, first['T'])
            self.assertSetEqual({'(', 'id'}, first['F'])
            self.assertSetEqual({'+', '^'}, first["E'"])
            self.assertSetEqual({'*', '^'}, first["T'"])
            self.assertSetEqual({')', '$'}, follow['E'])
            self.assertSetEqual({')', '$'}, follow["E'"])
            self.assertSetEqual({'+', ')', '$'}, follow['T'])
            self.assertSetEqual({'+', ')', '$'}, follow["T'"])
            self.assertSetEqual({'+', '*', ')', '$'}, follow['F'])

        with self.subTest(grammar_str=grammar_strs[2]):
            G = Grammar(grammar_strs[2])
            first, follow = first_follow(G)
            self.assertSetEqual({'('}, first['('])
            self.assertSetEqual({')'}, first[')'])
            self.assertSetEqual({'+'}, first['+'])
            self.assertSetEqual({'*'}, first['*'])
            self.assertSetEqual({'int'}, first['int'])
            self.assertSetEqual({'^', '*'}, first['Y'])
            self.assertSetEqual({'^', '+'}, first['X'])
            self.assertSetEqual({'int', '('}, first['T'])
            self.assertSetEqual({'int', '('}, first['E'])
            self.assertSetEqual({')', '$', '+'}, follow['Y'])
            self.assertSetEqual({')', '$'}, follow['X'])
            self.assertSetEqual({')', '$', '+'}, follow['T'])
            self.assertSetEqual({')', '$'}, follow['E'])

        with self.subTest(grammar_str=grammar_strs[3]):
            G = Grammar(grammar_strs[3])
            first, follow = first_follow(G)
            self.assertSetEqual({'a'}, first['S'])
            self.assertSetEqual({'c'}, first['B'])
            self.assertSetEqual({'b', '^'}, first['C'])
            self.assertSetEqual({'g', 'f', '^'}, first['D'])
            self.assertSetEqual({'g', '^'}, first['E'])
            self.assertSetEqual({'f', '^'}, first['F'])
            self.assertSetEqual({'$'}, follow['S'])
            self.assertSetEqual({'g', 'f', 'h'}, follow['B'])
            self.assertSetEqual({'g', 'f', 'h'}, follow['C'])
            self.assertSetEqual({'h'}, follow['D'])
            self.assertSetEqual({'f', 'h'}, follow['E'])
            self.assertSetEqual({'h'}, follow['F'])

        with self.subTest(grammar_str=grammar_strs[4]):
            G = Grammar(grammar_strs[4])
            first, follow = first_follow(G)
            self.assertSetEqual({'a'}, first['S'])
            self.assertSetEqual({'a'}, first['A'])
            self.assertSetEqual({'b'}, first['B'])
            self.assertSetEqual({'g'}, first['C'])
            self.assertSetEqual({'$'}, follow['S'])
            self.assertSetEqual({'$', 'd'}, follow['A'])
            self.assertSetEqual({'$', 'd'}, follow['B'])
            self.assertSetEqual(set(), follow['C'])

        with self.subTest(grammar_str=grammar_strs[5]):
            G = Grammar(grammar_strs[5])
            first, follow = first_follow(G)
            self.assertSetEqual({'(', 'a'}, first['S'])
            self.assertSetEqual({'(', 'a'}, first['L'])
            self.assertSetEqual({',', '^'}, first["L'"])
            self.assertSetEqual({'$', ',', ')'}, follow['S'])
            self.assertSetEqual({')'}, follow['L'])
            self.assertSetEqual({')'}, follow["L'"])

        with self.subTest(grammar_str=grammar_strs[6]):
            G = Grammar(grammar_strs[6])
            first, follow = first_follow(G)
            self.assertSetEqual({'a', 'b'}, first['S'])
            self.assertSetEqual({'^'}, first['A'])
            self.assertSetEqual({'^'}, first['B'])
            self.assertSetEqual({'$'}, follow['S'])
            self.assertSetEqual({'a', 'b'}, follow['A'])
            self.assertSetEqual({'a', 'b'}, follow['B'])

        with self.subTest(grammar_str=grammar_strs[7]):
            G = Grammar(grammar_strs[7])
            first, follow = first_follow(G)
            self.assertSetEqual({'d', 'g', 'h', '^', 'b', 'a'}, first['S'])
            self.assertSetEqual({'d', 'g', 'h', '^'}, first['A'])
            self.assertSetEqual({'g', '^'}, first['B'])
            self.assertSetEqual({'h', '^'}, first['C'])
            self.assertSetEqual({'$'}, follow['S'])
            self.assertSetEqual({'h', 'g', '$'}, follow['A'])
            self.assertSetEqual({'$', 'a', 'h', 'g'}, follow['B'])
            self.assertSetEqual({'g', '$', 'b', 'h'}, follow['C'])

    def test_CLOSURE(self):
        self.assertDictEqual(
            {"E'": {('.', 'E')}, 'E': {('.', 'E', '+', 'T'), ('.', 'T')}, 'T': {('.', 'T', '*', 'F'), ('.', 'F')},
             'F': {('.', '(', 'E', ')'), ('.', 'id')}},
            self.slr_parser.CLOSURE({self.slr_parser.G_prime.start: {('.', self.slr_parser.G_prime.start[:-1])}}))

        grammar_str = """E -> + E"""

        with self.subTest(grammar_str=grammar_str):
            G = Grammar(grammar_str)
            slr_parser = SLRParser(G)

            self.assertDictEqual({'E': {('.', '+', 'E')}, "E'": {('.', 'E')}},
                                 slr_parser.CLOSURE({slr_parser.G_prime.start: {('.', slr_parser.G_prime.start[:-1])}}))

    def test_GOTO(self):
        self.assertDictEqual({'E': {('E', '+', '.', 'T')}, 'T': {('.', 'T', '*', 'F'), ('.', 'F')},
                              'F': {('.', '(', 'E', ')'), ('.', 'id')}},
                             self.slr_parser.GOTO({"E'": {('E', '.')}, 'E': {('E', '.', '+', 'T')}}, '+'))

    def test_items(self):
        self.assertCountEqual([{"E'": {('.', 'E')}, 'E': {('.', 'E', '+', 'T'), ('.', 'T')},
                                'T': {('.', 'T', '*', 'F'), ('.', 'F')}, 'F': {('.', '(', 'E', ')'), ('.', 'id')}},
                               {'F': {('id', '.')}}, {"E'": {('E', '.')}, 'E': {('E', '.', '+', 'T')}},
                               {'T': {('F', '.')}}, {'E': {('T', '.')}, 'T': {('T', '.', '*', 'F')}},
                               {'F': {('(', '.', 'E', ')'), ('.', '(', 'E', ')'), ('.', 'id')},
                                'E': {('.', 'E', '+', 'T'), ('.', 'T')}, 'T': {('.', 'T', '*', 'F'), ('.', 'F')}},
                               {'E': {('E', '+', '.', 'T')}, 'T': {('.', 'T', '*', 'F'), ('.', 'F')},
                                'F': {('.', '(', 'E', ')'), ('.', 'id')}},
                               {'T': {('T', '*', '.', 'F')}, 'F': {('.', '(', 'E', ')'), ('.', 'id')}},
                               {'F': {('(', 'E', '.', ')')}, 'E': {('E', '.', '+', 'T')}},
                               {'E': {('E', '+', 'T', '.')}, 'T': {('T', '.', '*', 'F')}},
                               {'T': {('T', '*', 'F', '.')}},
                               {'F': {('(', 'E', ')', '.')}}], self.slr_parser.items(self.slr_parser.G_prime))

        grammar_str = """E -> E + T | E - T
E -> T
T -> T * F | T / F | F
F -> ( E )
F -> id"""

        with self.subTest(grammar_str=grammar_str):
            G = Grammar(grammar_str)
            slr_parser = SLRParser(G)
            self.assertCountEqual([{"E'": {('.', 'E')}, 'E': {('.', 'E', '+', 'T'), ('.', 'E', '-', 'T'), ('.', 'T')},
                                    'T': {('.', 'T', '*', 'F'), ('.', 'T', '/', 'F'), ('.', 'F')},
                                    'F': {('.', '(', 'E', ')'), ('.', 'id')}}, {'F': {('id', '.')}},
                                   {'T': {('F', '.')}},
                                   {'E': {('T', '.')}, 'T': {('T', '.', '*', 'F'), ('T', '.', '/', 'F')}},
                                   {'F': {('(', '.', 'E', ')'), ('.', '(', 'E', ')'), ('.', 'id')},
                                    'E': {('.', 'E', '+', 'T'), ('.', 'E', '-', 'T'), ('.', 'T')},
                                    'T': {('.', 'T', '*', 'F'), ('.', 'T', '/', 'F'), ('.', 'F')}},
                                   {"E'": {('E', '.')}, 'E': {('E', '.', '+', 'T'), ('E', '.', '-', 'T')}},
                                   {'T': {('T', '/', '.', 'F')}, 'F': {('.', '(', 'E', ')'), ('.', 'id')}},
                                   {'T': {('T', '*', '.', 'F')}, 'F': {('.', '(', 'E', ')'), ('.', 'id')}},
                                   {'F': {('(', 'E', '.', ')')}, 'E': {('E', '.', '+', 'T'), ('E', '.', '-', 'T')}},
                                   {'E': {('E', '+', '.', 'T')},
                                    'T': {('.', 'T', '*', 'F'), ('.', 'T', '/', 'F'), ('.', 'F')},
                                    'F': {('.', '(', 'E', ')'), ('.', 'id')}}, {'E': {('E', '-', '.', 'T')},
                                                                                'T': {('.', 'T', '*', 'F'),
                                                                                      ('.', 'T', '/', 'F'), ('.', 'F')},
                                                                                'F': {('.', '(', 'E', ')'),
                                                                                      ('.', 'id')}},
                                   {'T': {('T', '/', 'F', '.')}}, {'T': {('T', '*', 'F', '.')}},
                                   {'F': {('(', 'E', ')', '.')}},
                                   {'E': {('E', '+', 'T', '.')}, 'T': {('T', '.', '*', 'F'), ('T', '.', '/', 'F')}},
                                   {'E': {('E', '-', 'T', '.')}, 'T': {('T', '.', '*', 'F'), ('T', '.', '/', 'F')}}],
                                  slr_parser.items(slr_parser.G_prime))

    def test_construct_table(self):
        self.slr_parser.construct_table()

    def test_LR_parser(self):
        expected_results = ['ERROR: unrecognized symbol -', 'ERROR: input cannot be parsed by given grammar', 'accept']

        for i, w in enumerate(['id - id', '+ id', 'id + id * id']):
            with self.subTest(w=w):
                results = self.slr_parser.LR_parser(w)
                self.assertEqual(expected_results[i], results['action'][-1])

        grammar_strs = ["""S -> L = R | R
L -> * R | id
R -> L""", """E -> T | F
T -> id
F -> id"""]
        expected_results = ['ERROR: shift-reduce conflict at state ', 'ERROR: reduce-reduce conflict at state ']

        for i, w in enumerate(['id = id', 'id']):
            with self.subTest(w=w):
                G = Grammar(grammar_strs[i])
                slr_parser = SLRParser(G)
                results = slr_parser.LR_parser(w)
                self.assertIn(expected_results[i], results['action'][-1])


if __name__ == '__main__':
    unittest.main()
