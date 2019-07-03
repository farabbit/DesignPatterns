# 设计模式 Design Patterns

> Also See: [Design Patterns Intro](https://www.oodesign.com/)

> code: [PatternName].py

resuable solutions to commonly occruing problems, started as best practice applied to similar problems encountered in different contexts.

## Creation Design Patterns

### Singleton

---

> Ensure only **one instance** of a class created, provide **GLOBAL ACCESS POINT** to the object

### 工厂 Factory

#### 简单工厂模式 Factory

---

> 1. Creates object **without exposing instantiation logic** to the client.
> 2. **Refers** to newly created object **through a common interface**
> 3. 工厂一般用于根据传入的String类名创建不同的类

![Factory](https://www.oodesign.com/images/creational/factory-pattern.gif)

Be used when:

* when we need flexibility in adding new types of objects that must be created by the class

structure

* 接口 Product << Interface >> -> abstract XX getXX()
* 实现类 Concrete Product -> XX getXX() -> return XX
* 工厂 Factory = 用于产生不同的类 => 集中了所有实例的**创建逻辑**，不利于责任分配

#### 工厂方法 Factory Method

---

> 1. Defines an interface for creating objects, but **let subclasses to decide** which class to instantiate
> 2. Refers to the newly created object **through a common interface**.
> 3. 定义一个用户创建对象的接口，让子类决定实例化哪一个类，工厂方法模式使类的实例化延迟到其子类

![FactoryMethod](https://www.oodesign.com/images/creational/factory-method-pattern.gif)

Be used when:

* Base factory doesn't know what concrete classes will be required to create
* Base factory delegates the creation to its subclasses
* Subclasses know which class need to be instantiated

structure

* product << interface >>
* Concrate Product
* Concrete Factory
* Factory

#### 抽象工厂

pass

### 建造者模式 Builder

![Builder](https://www.oodesign.com/images/creational/builder-pattern.png)

* structure
  * Product
  * ConcreteBuilder
  * Builder
  * ConcreteBuilder
  * Director

## 行为型模式 Behavior Patterns

### 责任链模式 Chain of responsibility

> Objects become part of the chain, **request is sent from one object to another** until one object handle it

![Chain of Responsbility](https://www.oodesign.com/images/stories/chain%20of%20responsability%20implementation%20-%20uml%20class%20diagram.gif)

structure

* Request
* Handler << abstract >>
* Concrete Handler

Be used when:

> More than one object can handle a request, and the hanlder is unknow
