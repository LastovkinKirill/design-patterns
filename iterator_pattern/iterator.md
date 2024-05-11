# Terms and definitions

**The Iterator Pattern** is a behavioral design pattern that provides a way to access the elements of an aggregate
object
sequentially without exposing its underlying representation. It defines a mechanism to traverse elements of a
collection, such as lists, arrays, trees, etc., without needing to know the specific implementation details of the
collection.

According to GangOfFour, Iterator Pattern is used ” to access the elements of an aggregate object sequentially without
exposing its underlying implementation”.

In programming, an **antipattern** refers to a common approach or solution to a problem that initially appears to be
beneficial, but ultimately leads to poor code quality, inefficiency, or other negative consequences. These patterns can
arise due to various reasons, such as lack of experience, misunderstanding of requirements, or simply following outdated
practices.

An **iterable** refers to any data structure or object that can be iterated over, meaning it supports a way to traverse
its
elements sequentially. In python Iterable objects can be used in a for loop, and they typically implement the __iter__()
method, which returns
an iterator.

An **iterator** is an object that facilitates the traversal of elements within a container, data structure,
or collection. It provides a way to access elements sequentially without exposing the underlying structure of the
container.

# Comments and questions

1. In Iterator pattern we stick with Single Responsibility Principle. You can clean up the client code and the
   collections by extracting bulky traversal algorithms into separate classes.
2. In Iterator pattern we stick with Open/Closed Principle. You can implement new types of collections and iterators and
   pass them to existing code without breaking anything.
3. В других языках реализация требует два метода has_next() и next(). Но в питоне убрали требование has_next() и
   применили принцип питона The "ask for forgiveness, not permission" (EAFP) principle in Python
   "EAFP" stands for "Easier to Ask for Forgiveness than Permission." so you must raise StopIteration so __next__ handle
   it (under the hood) and to stop iteration.
4. __iter__ - возвращает итератор. т е iter() или когда for ... in ...
5. Iteration Protocol or Interface: Iterators often implement a standard protocol or interface that defines methods for
   advancing to the next element (next() in Python) and checking for the presence of more elements (hasNext() in Java).

# Resources

1. https://refactoring.guru/design-patterns/iterator
2. https://sourcemaking.com/design_patterns/iterator
3. https://github.com/faif/python-patterns/blob/master/patterns/behavioral/iterator_alt.py
3. https://www.geeksforgeeks.org/iterator-method-python-design-patterns/
