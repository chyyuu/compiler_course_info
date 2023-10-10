class Grammar:
    def __init__(self, grammar_str):
        self.grammar_str = '\n'.join(filter(None, grammar_str.splitlines()))
        self.grammar = {}
        self.start = None
        self.terminals = set()
        self.nonterminals = set()

        for production in list(filter(None, grammar_str.splitlines())):
            head, _, bodies = production.partition(' -> ')

            if not head.isupper():
                raise ValueError(
                    f'\'{head} -> {bodies}\': Head \'{head}\' is not capitalized to be treated as a nonterminal.')

            if not self.start:
                self.start = head

            self.grammar.setdefault(head, set())
            self.nonterminals.add(head)
            bodies = {tuple(body.split()) for body in ' '.join(bodies.split()).split('|')}

            for body in bodies:
                if '^' in body and body != ('^',):
                    raise ValueError(f'\'{head} -> {" ".join(body)}\': Null symbol \'^\' is not allowed here.')

                self.grammar[head].add(body)

                for symbol in body:
                    if not symbol.isupper() and symbol != '^':
                        self.terminals.add(symbol)
                    elif symbol.isupper():
                        self.nonterminals.add(symbol)

        self.symbols = self.terminals | self.nonterminals
