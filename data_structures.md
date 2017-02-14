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



