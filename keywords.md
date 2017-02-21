### raise
```python
if something:
    raise Exception('My error!')
```

### arbitrary argument list
https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists
```bash
>>> def concat(*args, sep="/"):
...     return sep.join(args)
...
>>> concat("earth", "mars", "venus")
'earth/mars/venus'
>>> concat("earth", "mars", "venus", sep=".")
'earth.mars.venus'
```

### assert
```python
assert batch_size is not None, 'You must set the batch size'
```
