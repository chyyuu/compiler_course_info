from slr_parser.grammar import Grammar
import unittest


class TestGrammar(unittest.TestCase):
    def test_grammar(self):
        with open('tests/test_grammar.txt') as grammar_file:
            self.G = Grammar(grammar_file.read())
            self.assertDictEqual(
                {'E': {('E', '+', 'T'), ('T',)}, 'T': {('T', '*', 'F'), ('F',)}, 'F': {('(', 'E', ')'), ('id',)}},
                self.G.grammar)
            self.assertEqual('E', self.G.start)
            self.assertSetEqual({'+', '*', '(', ')', 'id'}, self.G.terminals)
            self.assertSetEqual({'E', 'T', 'F'}, self.G.nonterminals)
            self.assertSetEqual({'+', '*', '(', ')', 'id', 'E', 'T', 'F'}, self.G.symbols)

        self.grammar_str = ["""E -> E + T
e -> T
T -> T * F | F
F -> ( E )
F -> id""", """E -> E ^ + T
E -> T
T -> T * F | F
F -> ( E )
F -> id"""]

        with self.assertRaises(ValueError):
            Grammar(self.grammar_str[0])

        with self.assertRaises(ValueError):
            Grammar(self.grammar_str[1])


if __name__ == '__main__':
    unittest.main()
