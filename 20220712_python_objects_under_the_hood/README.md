Reach out to me on Twitter [@mathsppblog](https://twitter.com/mathsppblog)
and [subscribe to my newsletter](https://mathspp.com/subscribe) to level up your Python knowledge!

# Python objects under the hood

This workshop was given by me [at EuroPython 2022](https://ep2022.europython.eu/session/python-objects-under-the-hood).

This workshop was based off of a series of articles [available on my blog](https://mathspp.com/blog/) and that I will list here:

 - [Dunder methods](https://mathspp.com/blog/pydonts/dunder-methods)
 - [Object initialisation with `__init__`](https://mathspp.com/blog/object-initialisation-with-__init__)

Exercise solutions will be in the articles above.
(If something is missing – sorry! Let me know!)


## Resources

 - Talk slides are available in this repository.
 - My [free Python book](https://gumroad.com/l/pydonts).
 - The [Indie Python Extravaganza bundle](https://leanpub.com/b/theindiepythonextravaganza/c/europython2022), free during the EuroPython 2022 conference.
 - The [data model Python 3 documentation page](https://docs.python.org/3/reference/datamodel).


## Abstract

Have you ever heard of Python's **magic** methods?
I am sorry, but they are not that “magic”!
I agree they are really cool, but dunder methods (the name they usually go by) are just regular Python methods that you implement!
And it is my job to help **you** learn about them.

**Dunder methods** are the methods that you need to implement when you want your objects to interact with the syntax of Python.
Do you want `len` to be callable on your objects? Implement `__len__`.
Do you want your objects to be iterables? Implement `__iter__`.
Do you want arithmetics to work on your objects? Implement `__add__` (and a bunch of others!).
Just to name a few things your objects could be doing.

In this training, we will go over a series of small use cases for many of the existing dunder methods: we will learn about the way in which each dunder method is supposed to work and then we implement it.
This will make you a more well-rounded Python developer because you will have a greater appreciation for how things work in Python.
I will also show you the approaches I follow when I am learning about a new dunder method and trying to understand how it works, which will help you explore the remainder dunder methods by yourself.

For this training, you need Python 3.8+ and your code editor of choice. This is a welcoming training and you will not be discriminated because of your choice of editor.
