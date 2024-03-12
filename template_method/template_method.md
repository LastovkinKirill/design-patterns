# Template Method pattern

# What is it? Definition?

> My definition:
> Поведенческий паттерн, который определяет функцию-алгоритм, но шаги реализации будут определены извне.

> Behavioral pattern which defines the skeleton of a base algorithm, deferring definition of exact steps to subclasses.
> [link](https://github.com/faif/python-patterns/blob/master/patterns/behavioral/template.py)

> Template Method is a behavioral design pattern that allows you to define a skeleton of an algorithm in a base class
> and let subclasses override the steps without changing the overall algorithm’s structure.
> [link](https://refactoring.guru/design-patterns/template-method/python/example)

> Behavioral Design Pattern that defines the skeleton of the operation and leaves the details to be implemented by the
> child class
> [link](https://www.geeksforgeeks.org/template-method-python-design-patterns/)

> Поведенческий шаблон проектирования, определяющий основу алгоритма и
> позволяющий наследникам переопределять некоторые шаги алгоритма, не изменяя его структуру в целом.
> [link](https://ru.wikipedia.org/wiki/%D0%A8%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D0%BD%D1%8B%D0%B9_%D0%BC%D0%B5%D1%82%D0%BE%D0%B4_(%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD_%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F))

# Description

## My description

# Classic implementation

Создаешь класс в котором определяешь метод-шаблон. В этом методе вызываешь другие методы класса, которые определяют
алгоритм этого метода-шаблона. Сами реализации методов, которые определяют алгоритм, реализуешь в дочерних классах.

### Python implementation

Создаешь функцию в котором определяешь функцию-шаблон. В этой функции-шаблоне вызываешь другие функции, которые ты
можешь
передать в качестве аргументов в функцию-шаблон. Эти функции-аргументы реализуют алгоритм функции-шаблона.

## How should it be used?

1. Analyze the target algorithm to see whether you can break it into steps. Consider which steps are common to all
   subclasses and which ones will always be unique.
2. Create the abstract base class and declare the template method and a set of abstract methods representing the
   algorithm’s steps. Outline the algorithm’s structure in the template method by executing corresponding steps.
   Consider making the template method final to prevent subclasses from overriding it.
3. It’s okay if all the steps end up being abstract. However, some steps might benefit from having a default
   implementation. Subclasses don’t have to implement those methods.
4. Think of adding hooks between the crucial steps of the algorithm.
5. For each variation of the algorithm, create a new concrete subclass. It must implement all of the abstract steps, but
   may also override some of the optional ones.

*[source](https://refactoring.guru/design-patterns/template-method)

# What for it? Why should it be used? What problems does it solve?

## Common problem

Паттерн помогает решить проблемы, где можно выделить общий алгоритм действий для похожих задач по структуре, но разных
по реализации.

Two different components have significant similarities, but demonstrate no reuse of common interface or implementation.
If a change common to both components becomes necessary, duplicate effort must be
expended. [link](https://sourcemaking.com/design_patterns/template_method)

## Potential SOLID problem

cм. problem/

1. Можно нарушить принцип DRY, если написать похожие классы с разными реализациями частей одного и того же алгоритма.
2. Одно из решений проблемы вариативности действий в зависимости от принимаемых параметров в алгоритме является
   использование конструкции if/else. Если возможно большое количество различных реализаций, то это решение может
   привести к нарушению принципа OCP. Потому что после первой реализации решения в production, возможно, понадобиться
   добавить другие реализации и мы будем вынуждены исправлять класс, в котором используется реализация с конструкцией
   if/else, тем самым подвергая риску сломать уже работающую, текущую реализацию.
3. Также есть возможность нарушить принцип SRP (cм. пример в problem/).

# Examples where it could be used? In what scenarios?

1. Оформление заказа в интернет магазине.
2. Формирование документа по шаблону.

# Where is it used in real projects, python libraries?

## Django

[Code line](https://github.com/django/django/blob/stable/3.2.x/django/views/generic/base.py#L62)

Template method pattern is used in view function. (but it is not method, so we can call it template function instead).
В это функции используются request проходит весь цикл от приема запроса, обработки его методами,
которые определяются наследниками класса (get, post, patch, put, delete, ...) до возврата ответа клиенту.

В этой функции можно переопределить методы для использования в шаблоне: setup, dispatch. Но самые главные методы,
которые используются это методы get, post, patch, put, delete.

Example of http methods overriding:

```python
class MyView(View):
    # этот метод вызовется в dispatch() если пришел запрос (request) HTTP-method GET
    def get(self):
        return "Hello World!"

    # этот метод вызовется в dispatch() если пришел запрос (request) HTTP-method POST
    def post(self):
        return "Hello World!"
```

# How have you used it in your real projects?

1. Для отправки жалоб в маркетплейс wildberries необходимы соответсвующее документы. Бот формировал структуру документа
   формата pdf в зависимости от типа жалобы (Жалоба по Авторскому праву, Жалоба по товарному знаку). Структура документа
   собирается с использованием библиотеки [python-docx](https://github.com/python-openxml/python-docx). Также пример
   есть в Design Patterns In Python. Copyright © 2019-2021 Sean Bradley.

# How does it differ from other tools (patterns)?

1. Factory Method is a specialization of Template Method. At the same time, a Factory Method may serve as a step in a
   large
   Template Method.

2. Template Method is based on inheritance: it lets you alter parts of an algorithm by extending those parts in
   subclasses.
   Strategy is based on composition: you can alter parts of the object’s behavior by supplying it with different
   strategies
   that correspond to that behavior. Template Method works at the class level, so it’s static. Strategy works on the
   object
   level, letting you switch behaviors at runtime.

*[source](https://refactoring.guru/design-patterns/template-method)

# What pros and cons of it?

## Pros

1. You can let clients override only certain parts of a large algorithm, making them less affected by changes that
   happen to other parts of the algorithm.
2. You can pull the duplicate code into a superclass.

## Cons

1. Some clients may be limited by the provided skeleton of an algorithm.
2. You might violate the Liskov Substitution Principle by suppressing a default step implementation via a subclass.
3. Template methods tend to be harder to maintain the more steps they have.
4. Based on inheritance.

*[source](https://refactoring.guru/design-patterns/template-method)

# A modern view of this tool? is it relevant today?

1. В python, возможно, будет использоваться чаще всего реализация на
   основе [first-class objects](https://en.wikipedia.org/wiki/First-class_citizen) ([ru](https://ru.wikipedia.org/wiki/%D0%9E%D0%B1%D1%8A%D0%B5%D0%BA%D1%82_%D0%BF%D0%B5%D1%80%D0%B2%D0%BE%D0%B3%D0%BE_%D0%BA%D0%BB%D0%B0%D1%81%D1%81%D0%B0)) (
   cм. python_implementation/).

# Nuances

1. Классическая реализация паттерна используется в языках, в которых отсутствуют объекты первого класса. В python с
   помощью объектов первого класса, возможна реализация отличная от классической. Поэтому
2. Но Brandon Rhodes отмечает, что сам же книга (Gangs of Four (GoF)) говорит использовать композицию вместо
   наследования и предлагает свой [вариант](https://youtu.be/pGq7Cr2ekVM?si=ufUPj8MS47kaDwoE&t=552) через композицию.

# How you work with it?

...

# Interview questions

## Links

1. https://climbtheladder.com/python-design-patterns-interview-questions/
2. https://www.tutorialspoint.com/design_pattern/design_pattern_interview_questions.htm
3. https://www.fullstack.cafe/blog/design-patterns-interview-questions
4. https://www.geeksforgeeks.org/top-design-patterns-interview-questions/
5. https://www.interviewbit.com/design-patterns-interview-questions/
6. https://medium.com/@ind/30-design-patterns-interview-questions-and-answers-29205ab01df6
7. https://www.indeed.com/career-advice/interviewing/design-patterns-interview-questions

## My interview questions

...

# My questions

...

# Sources

## Links

1. https://refactoring.guru/design-patterns/template-method
2. https://refactoring.guru/design-patterns/template-method/python/example
3. https://github.com/faif/python-patterns/blob/master/patterns/behavioral/template.py
4. https://sourcemaking.com/design_patterns/template_method
5. https://sourcemaking.com/design_patterns/template_method/python/1
6. https://www.geeksforgeeks.org/template-method-python-design-patterns/
7. https://github.com/ArjanCodes/betterpython/blob/main/6%20-%20template%20method%20%26%20bridge/trading-after.py

## Books

1. Design Patterns In Python. Copyright © 2019-2021 Sean Bradley.
2. Python: Master the Art of Design Patterns. Copyright © 2016 Packt Publishing. Dusty Phillips Chetan Giridhar Sakis
   Kasampalis.

## Videos

1. https://www.youtube.com/watch?v=t0mCrXHsLbI
    1. пример с trade-bot.