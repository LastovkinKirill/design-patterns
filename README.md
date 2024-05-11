# design-patterns

```mermaid
graph TD
;
    principles[Principles]
    principles --> KIS[KIS];
    principles --> DRY[DRY];
    principles --> SOLID[SOLID];
    principles --> smelly_code[Smelly code];
%%%%    
    design_patterns[Design patterns];
    design_patterns --> creational[Creational patterns];
    design_patterns --> structural[Structural patterns];
    design_patterns --> behavioral[Behavioral patterns];
    design_patterns --> concurrency[Concurrency patterns];
%%%%
    creational --> builder[Builder];
    creational --> abstract_factory[Abstract Factory]
    creational --> factory_method[Factory method]
    creational --> singleton[Singleton]
    creational --> prototype[Prototype]
%%%%
    structural --> adapter[Adapter]
    structural --> bridge[Bridge]
    structural --> facade[Facade]
    structural --> decorator[Decorator]
    structural --> proxy[Proxy]
    structural --> mvc[MVC]
    structural --> composite[Composite]
    structural --> flyweight[Flyweight]
%%%%    
    behavioral --> template_method[Template method]
    behavioral --> strategy[Strategy]
    behavioral --> observer[Observer]
    behavioral --> visitor[Visitor]
    behavioral --> chain_of_responsibility[Chain of responsibility]
    behavioral --> iterator[Iterator]
    behavioral --> mediator[Mediator]
    behavioral --> state[State]
    behavioral --> command[Command]
    behavioral --> interpreter[Interpreter]
    behavioral --> memento[Memento]
%%%%
    architectural_patterns[Architectural patterns]
    architectural_patterns --> mvc[MVC];
    architectural_patterns --> layered_architecture[Layered Architecture];
    architectural_patterns --> ports_and_adapters[Ports and Adapters 'Hexagonal' architecture];
    architectural_patterns --> onion_architecture[Onion architecture];
    architectural_patterns --> clean_architecture[Clean architecture];
    architectural_patterns --> microservice_architecture[Microservice architecture];
%%%%    
    other_patterns[Other patterns and principles];
    other_patterns --> dto[DTO];
    other_patterns --> microservices_and_monolith[Microservices and monolith];
    other_patterns --> dependency_inversion_principle[Dependency inversion principle];
    other_patterns --> monkey_patch[Monkey patch];
    other_patterns --> tdd_fdd_ddd_bdd[TDD FDD BDD DDD];
    other_patterns --> onion_architecture[Onion architecture];
    other_patterns --> active_record_architecture[Active record];
    other_patterns --> distributed_architecture[Distributed architecture];
    architectural_patterns[Architectural patterns]
    other_patterns --> dao[DAO];
    other_patterns --> Repository[Repository];

```

# Node links

[Template method](https://github.com/LastovkinKirill/design-patterns/tree/main/template_method)
[Iterator](https://github.com/LastovkinKirill/design-patterns/tree/main/iterator_pattern)

# Priority

1. Design Patterns
    1. Creational:
        1. Builder
        2. Abstract Factory
        3. Factory method
        4. Singleton
        5. Prototype
    2. Structural
        1. Adapter
        2. Bridge
        3. Facade
        4. Decorator
        5. Proxy
        6. MVC
            1. Design pattern or architectural pattern ?
        7. Composite
            1. ?
        8. Flyweight
            1. ?
    3. Behavioral
        1. Template method
        2. Strategy
        3. Observer
        4. Visitor
        5. Chain of responsibility
        6. Iterator
        7. Mediator
        8. State
        9. Command
        10. Interpreter
            1. ?
        11. Memento
            1. ?

# Questions

1. What is anti-patterns?

# Requirements for the cheat sheet

1. Скорость.
    1. Она должна быть быстро написана, без перфекционизма и лишних подробностей и углублений.
2. Практика.
    1. Обязательно практически написанный тобой код. Но только необходимый, чтобы прощупать предмет изучения. Без лишних
       примеров.
3. Понять предмет изучения.
4. Вся структура шпаргалки строиться на вопросах.
5. Шпаргалка должна быть короткой.
6. Ссылки на ресурсы и источники, которые тебе помогали понять и ты использовал при написании шпаргалки.
7. Шпаргалка нужно, чтобы все усвоить, запомнить и быстро вспомнить.
