# Creational Design Patterns

Creational patterns are used while **creating objects**, increasing flexibility and code reusability.  
They help define **how objects are created, composed, and represented**.

There are two main goals of these patterns:
- They **hide information** about the specific classes used in the system.
- They **hide the details** of how instances of these classes are created and assembled.

---

## 1. Abstract Factory Pattern

**Abstract Factory** is a creational design pattern that lets you produce **families of related objects** without specifying their concrete classes.

**Example:**  
Consider a **Honda factory**.  
Now, they have two types of Hondas in different regions:  
- **Indian Honda**  
- **US Honda**

Their main objective is to create two kinds of vehicles:
- **Bike**
- **Car**

So:
- Indian Honda will create **Indian Car** and **Indian Bike**.
- US Honda will create **US Car** and **US Bike**.

Technically, **US Car** and **Indian Car** can be derived from a base **Car** class. Similarly, **US Bike** and **Indian Bike** can be derived from a base **Bike** class.  
These derived classes may have the same or different functionalities and specifications.

This shows how the **Abstract Factory** works — it produces related objects grouped under a single family without knowing their exact concrete classes.

---

## 2. Builder Pattern

**Builder** is a creational design pattern that lets you construct **complex objects step by step**. The pattern allows you to produce **different types and representations** of an object using the same construction code.

**Example:**  
Suppose we have a base class called **Transformer**.  
There are two types of Transformers:  
1. **Autobot**  
2. **Decepticon**

Both inherit from **Transformer**.  
The building process, which is generally complex, can be broken down step by step:
- You don’t have to call a function and catch the return every time.
- Instead, you keep calling methods step by step.
- Finally, you call a `build()` function that returns the complete **Transformer** object.

---

## 3. Factory Pattern

**Factory Method** is a creational design pattern that provides an **interface for creating objects** in a superclass, but allows subclasses to **alter the type of objects** that will be created.

This is one of the **most commonly used patterns** in everyday development.

**Example:**  
Consider a **Burger** class.  
Now, we have a **Burger Factory** class.  
The factory class can create different types of burgers and return their objects, like:
- **Cheese Burger**
- **Fish Burger**
- **Chicken Burger**

The client code just calls the factory and gets the specific burger it needs.

---

## 4. Prototype Pattern

**Prototype** is a creational design pattern that lets you **copy existing objects** without making your code dependent on their concrete classes.

It is a simple pattern that lets you **clone an object** to create a new one, which saves time and resources.

**Example:**  
Consider an **alien invasion** — the aliens have the name, weight, and height of **John Doe**.  
Now, they want to clone or copy John Doe to create **Johnny English** with a different weight.  
They can directly copy the DNA as well — so instead of creating a new being from scratch, they **clone** and adjust details.

---

## 5. Singleton Pattern

**Singleton** is a creational design pattern that lets you ensure that a class **has only one instance**, while providing a **global access point** to that instance.

It solves two main problems:
1. Ensures that a class has only **one instance**.
2. Provides a **global access point** to that instance.

> Note: There is no **implicit keyword** to define a class as a Singleton in Python — you need explicit logic for it.  
> Every developer might use a slightly different approach.

**Example:**  
Consider an **AppState** — you are only allowed to create **one instance** of it.

Basic Singleton logic:
1. Create a class with a constructor.
2. Add a **class variable** (e.g., `_instance`) and set it to `None` initially.
3. In the constructor, check if `_instance` is `None`:
   - If `_instance` is not `None`, raise an exception (only one instance allowed).
   - If `_instance` is `None`, set `_instance` to `self`.
4. Provide a **static method** (e.g., `get_instance`) to check:
   - If `_instance` is `None`, create it and return it.
   - If `_instance` is not `None`, just return the existing instance.

This ensures the user **cannot create a new object**, but can **always get the same instance**.

---

✅ **These creational patterns** help you manage object creation smartly and make your code **more maintainable, flexible, and reusable.**
