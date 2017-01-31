### timing

If you want to time how long it takes for a whole cell to run, you’d use %%timeit at the beginning of the cell.
![](figs/magic-timeit2.png)


Timing how quickly your code runs is essential for this optimization. You can use the %timeit magic command to time how long it takes for a function to run.
![](figs/magic-timeit.png)

### visualizations

* To render figures directly in the notebook, you should use the inline backend with the command %matplotlib inline.
* On higher resolution screens such as Retina displays, the default images in notebooks can look blurry. Use %config InlineBackend.figure_format = 'retina' after %matplotlib inline to render higher resolution images.







There are a whole bunch of other magic commands, I just touched on a few of the ones you'll use the most often. To learn more about them, here's the list of all available [magic commands](http://ipython.readthedocs.io/en/stable/interactive/magics.html).
