# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/03_neuron.ipynb.

# %% auto 0
__all__ = ['Neuron', 'Layer', 'MLP']

# %% ../../nbs/03_neuron.ipynb 2
# from nanograd.core.value import Value
import random, math
from . import Value, draw_dot
from typing import List, Iterable, Union

# %% ../../nbs/03_neuron.ipynb 3
class Neuron:

    def __init__(self, nin) -> None:
        self.w = [Value(random.uniform(-1, 1), label=f"w{i}") for i in range(nin)]
        self.b = Value(random.uniform(-1, 1), label="b")
    
    def __call__(self, x):
        assert len(x) == len(self.w)
        x = [Value(_x) if not isinstance(_x, Value) else _x for _x in x]
        return (sum([_x*_w for _x, _w in zip(x, self.w)]) + self.b).tanh()

# %% ../../nbs/03_neuron.ipynb 4
class Layer:

    def __init__(self, nin, nout) -> None:
        self.neurons = [Neuron(nin) for _ in range(nout)]

    def __call__(self, x):
        return [neuron(x) for neuron in self.neurons]

# %% ../../nbs/03_neuron.ipynb 5
class MLP:

    def __init__(self, nin: int, nouts:List[int]) -> None:
        sz = [nin] + nouts
        self.layers = [Layer(sz[i], sz[i+1]) for i in range(nouts)]
    
    def __call__(self, x):
        for layer in self.layers:
            x = layer(x)
        return x
