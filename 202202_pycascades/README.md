Reach out to me on Twitter [@mathsppblog](https://twitter.com/mathsppblog)
and [subscribe to my newsletter](https://mathspp.com/subscribe) to level up your Python knowledge!

# Fifty shades of `sign`

This talk was presented at PyCascades 2022.

![](./poster.png)


## Abstract

The Zen of Python says “there should be one -- and preferably only one -- obvious way to do it”, but what if there's a dozen obvious ways to do it?

In this talk we take a look at over a dozen implementations of a very simple function: the sign function.
The sign function should return -1 for negative numbers, 1 for positive numbers, and 0 if the input is 0. Simple, right?
And it is, but there are multiple implementations that we can look at.

As we do so, we try to decide which alternative is the best and we even explore a couple of more intricate Python subtleties!
As an example of some of those subtleties, we'll look at Boolean arithmetic, Boolean to integer conversion, and (chained) conditional expressions.

As we look at different implementations, we try to decide which one is the best. We will do some profiling, but we'll also realise that that's hardly the most important metric to use!

Which implementation will be the best?


[twitter]: https://twitter.com/mathsppblog
