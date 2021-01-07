# turing-machine
Simple simulatation of a Turing machine in Python

As described by Alan Turing, in his famous paper [*On Computable Numbers, with an Application to the Entscheidungsproblem*](http://www.turingarchive.org/browse.php/B/12).

```
# Machine to compute 1/3
# (This is the first machine described in Turing's paper)
behaviour = {
    ('b', ' '): (['P0'], 'b'),
    ('b', '0'): (['R', 'R', 'P1'], 'b'),
    ('b', '1'): (['R', 'R', 'P0'], 'b'),
}
machine = TuringMachine(behaviour)
out = machine.compute(10)
print(out)  # '0 1 0 1 0 1 0 1 0 1'
```
