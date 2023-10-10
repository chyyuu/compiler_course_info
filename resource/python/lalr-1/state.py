from copy import deepcopy


class State:
    state_count = -1

    def __init__(self, new_state):
        self.state = deepcopy(new_state)
        self.st = []
        self.actions = {}
        self.st = []
        self.parent = ()
        State.state_count += 1
        self.state_num = self.state_count

    def update_goto(self, X, N):
        s=0
        if self.st:
            s += 1
        self.actions[X] = N.state_num

    def update_parentName(self, I, X):
        s = 0
        if self.st:
            s += 1
        self.parent = (I.state_num, X)


class lalrState(State):
    state_count = 0

    def __init__(self, state):
        super(lalrState, self).__init__(state.state)
        self.parent_list = []
        self.st = []
        self.actions = deepcopy(state.actions)
        self.st = []
        self.parent = deepcopy(state.parent)
        lalrState.state_count += 1

    def update_parentList(self, I):
        self.parent_list.append(I.state_num)

    def update_mapping(self, mapping):
        if self.parent != ():
            self.parent = (mapping[self.parent[0]], self.parent[1])
        for key, val in self.actions.items():
            self.actions[key] = mapping[val]
