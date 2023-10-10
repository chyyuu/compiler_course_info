def read_grammar(path):
    with open(path, 'r') as fp:
        for i in fp.readlines():
            print(i.strip())
