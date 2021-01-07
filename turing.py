# Simulation of a Turing Machine
# Based on the explanations in the book: 
#  - Annotated Turing by Charles Petzold (2008)


class TuringMachine():
    """Simulation of a Turing machine"""

    def __init__(self, behaviour):
        self.behaviour = behaviour
        self.tape = [' ']
        self.pos = 0
        self.m_config = 'b'

    def step(self):
        config = (self.m_config, self.tape[self.pos])
        try:
            actions, next_m_config = self.behaviour[config]
        except KeyError:
            if self.tape[self.pos] == ' ':
                raise KeyError
            actions, next_m_config = self.behaviour[(config[0], 'Any')]
        for action in actions:
            self.act(action)
        self.m_config = next_m_config

    def extend_tape(self):
        while self.pos >= len(self.tape):
            self.tape.append(' ')

    def act(self, action):
        if action == 'L':
            if self.pos == 0:
                raise ValueError("cannot move left at start of tape")
            self.pos -= 1
        elif action == 'R':
            self.pos += 1
            self.extend_tape()
        elif action.startswith('P'):
            self.extend_tape()
            self.tape[self.pos] = action[1:]
        elif action.startswith('E'):
            self.tape[self.pos] = ' '
        else:
            raise ValueError("unrecognized action")

    def compute(self, n_digits):
        while len(self.tape) < n_digits + 1:
            self.step()
        # Return every second value on the tape which 
        # should all be binary digits
        return ''.join([b for b in self.tape[0:n_digits]])


# Machine to compute 1/3
# (This is the first machine described in Turing's paper)
behaviour1 = {
    ('b', ' '): (['P0'], 'b'),
    ('b', '0'): (['R', 'R', 'P1'], 'b'),
    ('b', '1'): (['R', 'R', 'P0'], 'b'),
}
machine = TuringMachine(behaviour1)
out = machine.compute(19)
assert len(out) == 19
assert out == '0 1 0 1 0 1 0 1 0 1'

# Machine to compute '001011011101111011111...'
# (This is the 2nd machine described in Turing's paper)
behaviour2 = {
    ('b', ' '): (['Pe', 'R', 'Pe', 'R', 'P0', 'R', 'R', 'P0', 'L', 'L'], 'v'),
    ('v', '1'): (['R', 'Px', 'L', 'L', 'L'], 'v'),
    ('v', '0'): ([], 'q'),
    ('q', 'Any'): (['R', 'R'], 'q'),
    ('q', ' '): (['P1', 'L'], 'p'),
    ('p', 'x'): (['E', 'R'], 'q'),
    ('p', 'e'): (['R'], 'f'),
    ('p', ' '): (['L', 'L'], 'p'),
    ('f', 'Any'): (['R', 'R'], 'f'),
    ('f', ' '): (['P0', 'L', 'L'], 'v')
}
machine = TuringMachine(behaviour2)
out = machine.compute(43)
assert len(out) == 43
assert out == 'ee0 0 1 0 1 1 0 1 1 1 0 1 1 1 1 0 1 1 1 1 1'
