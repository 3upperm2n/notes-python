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

## lambda function
http://www.secnetix.de/olli/Python/lambda_functions.hawk

<img src="figs/lamba_demo.png" height="300">

## global scope of a variable inside a function
```python
def update_input_layer(review):
    
    global layer_0
    
    # clear out previous state, reset the layer to be all 0s
    layer_0 *= 0
    for word in review.split(" "):
        layer_0[0][word2index[word]] += 1

update_input_layer(reviews[0])
```

