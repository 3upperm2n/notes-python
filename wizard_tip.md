### zip
use zip and compaction to compute dot product of two vectors
```python
wx = sum(a * b for a , b in zip(x,w))
```

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
