# Behavioral Design Patterns

Behavioral design patterns focus on the interactions and communication between objects. They help define how objects collaborate and distribute responsibility among them, making it easier to manage complex control flow and communication in a system.

---

## Types of Behavioral Patterns

### 1. Chain of Responsibility Pattern
**Intent:** Pass a request along a chain of handlers. Each handler either processes the request or passes it to the next handler in the chain.

Think of it like a linked list where each node (handler) decides whether to act or pass the request along.

**Example:**  
A support team with low-level, mid-level, and high-level ticket resolvers. If a ticket arrives, it starts with the low-level resolver. If it can't handle it, it escalates to mid-level, and so on. If no handler can resolve it, the ticket remains unresolved.

---

### 2. Command Pattern
**Intent:** Encapsulate a request as an object, allowing you to parameterize clients, queue or log requests, and support undoable operations.

Think of a king giving commands to different workers. Each worker is an independent entity executing the king’s orders.

---

### 3. Iterator Pattern
**Intent:** Provide a way to access elements of a collection sequentially without exposing its underlying structure.

**Example:**  
A linked list or a tree structure. You define `__iter__()` and `__next__()` methods to iterate without knowing the internal representation.

---

### 4. Mediator Pattern
**Intent:** Reduce direct communication between objects and enforce interactions only via a mediator.

**Analogy:**  
Think of an API Gateway—you send a request, and the gateway handles routing, validation, and dispatching to the correct endpoint. The services don't communicate directly but via the gateway (mediator).

---

### 5. Memento Pattern
**Intent:** Capture and restore an object’s internal state without violating encapsulation. Commonly used in undo/redo functionality.

**Example:**  
In a text editor, you save your work frequently. If your PC crashes, you can restore the last checkpoint because it was saved in a memento.

---

### 6. Observer Pattern
**Intent:** Define a subscription mechanism to notify multiple objects about changes in another object.

**Example:**  
YouTube subscriptions: Users subscribe to a channel, and whenever a new video is uploaded, all subscribers receive a notification—just like a pub/sub system (e.g., RabbitMQ, Kafka).

---

### 7. State Pattern
**Intent:** Allow an object to alter its behavior when its internal state changes.

**Example:**  
A human object starts with a default state: walking. When it decides to run, its state changes to running. Switch it back to walking, and the behavior adapts accordingly.

---

### 8. Strategy Pattern
**Intent:** Define a family of algorithms, encapsulate each one, and make them interchangeable at runtime.

**Example:**  
A payment gateway supports UPI, Credit Card, PayPal, etc. At runtime, the user chooses which payment method (strategy) to use.

---

### 9. Template Method Pattern
**Intent:** Define the skeleton of an algorithm in a superclass, but let subclasses override specific steps.

**Example:**  
Every car has a basic structure: 4 wheels, interiors, and a mandatory engine (with variations). Optional features like NoS can be added. Ferrari and Supra are subclasses that define their own engine types and optional features.

---

### 10. Visitor Pattern
**Intent:** Add new operations to existing class structures without modifying them.

**Example:**  
A `ShapeVisitor` class visits multiple shapes like Circle, Square, etc. Each shape allows the visitor to perform operations without changing the shape’s original implementation.

---

## Conclusion

Behavioral patterns enhance object communication while maintaining loose coupling and separation of concerns. They are essential for building scalable and maintainable systems by clearly defining the roles and interactions of components.
