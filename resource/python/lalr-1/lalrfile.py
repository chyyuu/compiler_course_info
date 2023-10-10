import sys
from impl import calculate_first, term_and_nonterm, get_augmented, find_states, combine_states, get_parse_table
from state import State, lalrState


class Lalr(object):
    def __init__(self, parent=None):
        print("LALR PARSER ")
        self.grammar = []
        self.define_variables();
        self.open_file()
        self.read_file()

    def define_variables(self):
        self.string = ""
        #print("!")
        self.augment_grammar = []
        self.first = {}
        self.term = []
        self.val = ''
        self.lalr_states = []
        self.non_term = []
        self.states = []
        self.parse_table = []
        State.state_count = -1
        lalrState.state_count = 0

    def check_changed(self):
        self.changed = True

    def open_file(self):
        file = open('grammar.txt', 'r')
        self.string = file.read();
        print("     ")
        print("Given Grammar")
        print("   ")
        print(self.string)
        print("--------------------------------------------------------")
        file.close();

    def read_file(self):
        # self.define_variables()
        lines = self.string  # string
        # print(lines)
        productions = lines.split('\n')  # converting into list of lines
        #print(productions)

        try:
            for line in productions:
                line = line.replace(' ', '')
                # print("1")
                if line != '':
                    line_list = line.split('->')

                    if line_list[0].isupper() and line_list[1] != '':
                        if '|' in line_list[1]:
                            prod_list = line_list[1].split('|')
                            for prod in prod_list:
                                self.grammar.append([line_list[0], prod])
                        else:
                            self.grammar.append(line_list)

                            #print(self.grammar)
                    else:

                        # self.ui.textBrowser.setText("Invalid grammar")
                        print("INVALID GRAMMAR")
                        self.grammar = []

            if self.grammar != []:
                # print("2")
                term_and_nonterm(self.grammar, self.term, self.non_term)
                #print("\nNon Terminals : " + ' '.join(self.non_term) + "\nTerminals : " + ' '.join(self.term))
                # print(self.term)
                # print(self.non_term)
                self.disp()
                calculate_first(self.grammar, self.first, self.term, self.non_term)
                #print(self.first)
                self.disp_first()
                get_augmented(self.grammar, self.augment_grammar)
                print("Augmented Grammar :")
                for q1, q2 in self.augment_grammar:
                    print(q1 + '->' + q2)

                find_states(self.states, self.augment_grammar, self.first, self.term, self.non_term)
                # print(self.states)
                combine_states(self.lalr_states, self.states)
                # print(self.lalr_states)
                self.disp_lr1_states()
                print(" ")
                print("-----------------------------------------------")
                print(" ")
                self.disp_lalr_states()
                get_parse_table(self.parse_table, self.lalr_states, self.augment_grammar)
                #print(self.parse_table)
                self.disp_parse_table()
                self.disp_parsing()
                self.changed = False

        except (KeyError, IndexError):
            #
            # self.ui.textBrowser.setText("Invalid grammar")
            print("INVALID GRAMMAR")
            self.define_variables()

    def disp(self):


        if self.grammar != []:
            print("  ")
            print("\nNon Terminals : " + ' '.join(self.non_term) + "\n \nTerminals : " + ' '.join(self.term))
            print("-----------------------------------------------------------------------")

    def disp_first(self):

        if self.first != {}:
            #
            for nonterm in self.non_term:
                print('First(' + nonterm + ') : ' + ' '.join(self.first[nonterm]) + '\n')
            print("--------------------------------------------------------------")
    def disp_lr1_states(self):

        if self.states != []:

            print("Number of LR(1) states : " + str(self.states[len(self.states) - 1].state_num + 1))
            for state in self.states:
                print('----------------------------------------------------------------')
                if state.state_num == 0:
                    print("\nI" + str(state.state_num) + ' : ' + '\n')
                else:
                    print(
                        "\nI" + str(state.state_num) + ' : ' + ' goto ( I' + str(state.parent[0]) + " -> '" + str(
                            state.parent[1]) + "' )\n")
                for item in state.state:
                    print(item[0] + ' -> ' + item[1] + ' ,  [ ' + ' '.join(item[2]) + ' ]')
                if state.actions != {}:
                    print('\nActions : ')
                    for q, v in state.actions.items():
                        print(str(q) + ' -> ' + str(abs(v)) + '\t')
                        # self.ui.textBrowser.insertPlainText(str(k) + ' -> ' + str(abs(v)) + '\t')

    def disp_lalr_states(self):

        if self.lalr_states != []:

            print("Number of LALR states : " + str(lalrState.state_count))
            for state in self.lalr_states:
                print('----------------------------------------------------------------')
                if state.state_num == 0:
                    print(
                        "\nI" + str(state.state_num) + ' : ' + '\tGot by -> ' + str(state.parent_list) + '\n')
                else:
                    print(
                        "\nI" + str(state.state_num) + ' : ' + ' goto ( I' + str(state.parent[0]) + " -> '" + str(
                            state.parent[1]) + "' )" + '\tGot by -> ' + str(state.parent_list) + '\n')
                for item in state.state:
                    print(item[0] + ' -> ' + item[1] + ' ,   [ ' + ' '.join(item[2]) + ' ]')
                if state.actions != {}:
                    # print(state.actions.items)
                    print('\nActions : ')
                    for q, v in state.actions.items():
                        print(str(q) + ' -> ' + str(abs(v)) + '\t')

    def disp_parse_table(self):

        if self.grammar != []:

            all_symb = []
            all_symb.extend(self.term)
            all_symb.append('$')
            all_symb.extend(self.non_term)
            if 'e' in all_symb:
                all_symb.remove('e')

            head = '{0:12}'.format(' ')
            for X in all_symb:
                head = head + '{0:12}'.format(X)
            # self.ui.textBrowser.setText(head + '\n')
            print(head + '\n')
            s = '------------' * len(all_symb)
            print(s)

            for index, state in enumerate(self.parse_table):
                line = '{0:<12}'.format(index)
                for X in all_symb:
                    if X in state.keys():
                        if X in self.non_term:
                            action = state[X]
                        else:
                            if state[X] > 0:
                                action = 's' + str(state[X])
                            elif state[X] < 0:
                                action = 'r' + str(abs(state[X]))
                            elif state[X] == 0:
                                action = 'accept'

                        line = line + '{0:<12}'.format(action)
                    else:
                        line = line + '{0:<12}'.format("")

                print(line)
                print(s)

    def disp_parsing(self):

        if self.grammar != []:
            line_input = input()
            self.parse(self.parse_table, self.augment_grammar, line_input)

    def parse(self, parse_table, augment_grammar, inpt):
        inpt = list(inpt + '$')
        stack = [0]
        a = inpt[0]
        try:
            head = '{0:40} {1:40} {2:40}'.format("Stack", "Input", "Actions")
            # self.ui.textBrowser.setText(head)
            print(head)
            while True:
                s1=''
                s1=s1.join(inpt)
                stackstring = [str(z) for z in stack]
                s2=''
                s2 = s2.join(stackstring)

                # p=''
                # p=p.join(stack)
                # for result, p_result in zip(stack, inpt):
                #     strings= '\n{0:<40} {1:<40}'.format(result, p_result)
                strings = ' \n{0:<40} {1:<40}  '.format(s2, s1)
                s = stack[len(stack) - 1]
                action = parse_table[s][a]
                if action > 0:
                    inpt.pop(0)
                    stack.append(action)
                    # for result, p_result in zip(stack, inpt):
                    #     print('{:3}{:20}'.format(result, p_result)+'Shift ' + a + '\n')
                    print(strings + 'Shift ' + a + '\n')
                    a = inpt[0]
                elif action < 0:
                    prod = augment_grammar[-action]
                    if prod[1] != 'e':
                        for i in prod[1]:
                            stack.pop()
                    t = stack[len(stack) - 1]
                    stack.append(parse_table[t][prod[0]])
                    # for result, p_result in zip(stack, inpt):
                    #     print('{:3}{:20}'.format(result, p_result))
                    print(strings + 'Reduce ' + prod[0] + ' -> ' + prod[1] + '\n')
                elif action == 0:
                    # for result, p_result in zip(stack, inpt):
                    #     print('{:3}{:20}'.format(result, p_result))
                    print('ACCEPT\n')
                    break
        except KeyError:
            print('\n\nERROR\n')


k = Lalr()
