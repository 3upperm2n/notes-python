## tuple
immutable, like read-only cache

## sorting
use sorted() will return a list of tuple

if you need the dict(), use OrderedDict
```python
from collections import OrderedDict
od = OrderedDict(sorted_streams_start)
```
## class
create a class [example](https://en.wikibooks.org/wiki/A_Beginner's_Python_Tutorial/Classes)

## counter from collections
https://docs.python.org/2/library/collections.html#collections.Counter

```python
from collections import Counter
total_counts = Counter()

for idx,rows in reviews.iterrows():
    total_counts.update(rows[0].split(' '))
```


## xrange(N)
it creates a sequence from 0 to N-1


## vstack
Stack arrays in sequence vertically (row wise)

https://docs.scipy.org/doc/numpy/reference/generated/numpy.vstack.html

```python
self.weights[self.num_layers] = np.vstack((2 * np.random.random(shape) - 1, 2 * np.random.random((1, shape[1])) - 1))
```

[nn in python] (https://github.com/jiexunsee/Neural-Network-with-Python)
