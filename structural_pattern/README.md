# Structural Design Patterns

Structural Design Patterns are solutions in software design that focus on how classes and objects are organized to form larger, functional structures. These patterns help developers simplify relationships between objects, making code more efficient, flexible, and easy to maintain. By using structural patterns, you can better manage complex class hierarchies, reuse existing code, and create scalable architectures.

There are two recurring themes in these patterns:

* Making independently developed class libraries work together.
* Composing objects to realize new functionality.

The added flexibility of object composition comes from the ability to change the composition at run-time, which is impossible with static class composition.

---

## 1. Adapter Pattern

**Alias:** Wrapper

It converts the interface of a class into another interface that clients expect. The Adapter lets classes work together that couldn't otherwise because of incompatible interfaces.

**Example:**
Today's GenZ generation might not enjoy retro songs. So, we wrap old songs in rock music. Tada! GenZ now listens to old songs. The adapter here bridges the gap between retro and modern music preferences.

---

## 2. Bridge Pattern

This pattern splits a large class or a set of closely related classes into two separate hierarchies: **abstraction** and **implementation**—which can be developed independently.

**Example:**
You have multiple shapes and multiple colors. Instead of creating a class for every combination (e.g., RedCircle, GreenSquare), you separate shapes and colors into different interfaces and implementations. Now, adding a new shape or color doesn't lead to an explosion of classes.

---

## 3. Composite Pattern

This pattern lets you compose objects into tree structures and work with them as if they were individual objects.

**Example:**
An organizational hierarchy: Managers have leads under them, and leads have software engineers under them. Each entity can be treated as a node. We create a tree-like structure where every manager can contain other employees.

---

## 4. Decorator Pattern

This pattern lets you attach new behaviors to objects by wrapping them inside special wrapper objects (decorators) that contain the behavior.

**Clarification:**

* `@decorator` in Python wraps **functions**.
* Decorator design pattern wraps **classes** (objects).

**Example:**
You have a basic coffee with a base cost and description. You now want to add milk or sugar. You wrap the coffee with a MilkDecorator or SugarDecorator. Each wrapper adds its own cost and modifies the description.

---

## 5. Facade Pattern

This pattern provides a simplified interface to a complex subsystem of classes, frameworks, or libraries.

**Example:**
You want to watch a movie. You press one button on your Home Theatre, and internally it turns on the DVD, dims the lights, powers the projector and sound system. After the movie ends, everything resets. The user interacts with a single entry point, unaware of the complexity behind it.

---

## 6. Flyweight Pattern

This pattern reduces memory consumption by sharing common parts of object state between multiple objects, rather than storing everything in each object.

**Example:**
All humans share the same basic traits: 206 bones, 32 teeth, and binary gender. Instead of storing these common values in every human object, we create a shared object for this common state. A factory ensures we reuse the shared state unless something changes. Then, we can create a planet object with thousands of lightweight human objects.

---

## 7. Proxy Pattern

This pattern provides a substitute or placeholder for another object. It controls access, allowing actions before or after the real object's method is invoked.

**Example:**
A student checks the timetable. If the subject is Maths, English, or History, he attends class. Otherwise, he asks a proxy to mark his attendance. The proxy acts as a gatekeeper to determine whether to forward the request to the real object or handle it itself.

---

> These patterns are essential tools in a developer's toolkit for building maintainable and scalable software systems. Use them wisely based on the problem context.
