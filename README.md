# LangGraph Tutorial

A repository dedidcate to learning LangGraph.

## What is LanngGraph?

LangGraph is a framework for building **stateful, multi-agent AI workflow** using **graphs** - where each node represents an LLM, tool, or logic step, and edges define how information flows between them. It extends [**LangChain**](https://github.com/boghas/langgraph-tutorial.git) to make complex, conversation, or reactive AI systems easier to manage.

## Overview

### Type Annotations

`Type annotations` let you specify the expected **data types** of variables, functions parameters, and return values to improve **code clarity, linting*, and type checking**

* ***linting:*** automatically checking your code for **errors, style issues, or potential bugs** - helping you keep it clean, consistent and reliable.
 
#### Dictionaries

##### **`Normal Dictionary`:**
  
```movie = {"name": "Avengers Endgame", "year": 2019}```

* * Allows for *efficient data retrieval* based on unique keys
* * *Flexible* and easy to implement.
* * Leads to **challenges** in ensuring that the data is a **particular structure** especially for larger projects.
* * Doesn't check if the data is the correct type or structure.

##### **`TypedDict`:**

`TypedDict` in Python lets you define a **dictionary type** where you can **specify the expected keys and their value types**, improving type checking and code clarity.


```
from typing import TypedDict

class Movie(TypedDict):
    name: str
    year: int

movie = Movie(name="Avengers Endgame", year=2019)
```

* * **Type Safety** - we defined explicitly what the data structures are, reducing runtime errors.
* * **Enhanced Readability** - Makes debugging easier and makes code more understandable.
  
##### **`Union`:**

A `Union` in Python's typing system means a value can be **one of several types**.

```
from typing import Union

def square(x: Union[int, float]) -> float:
    return x * x

# x = 5 -> this is fine because it's an integer
# x = 1.32 -> this is also fine because it's a float
# x = "5" -> this will fail because it's not an int or a float 
```

* * Union lets you say that a value can be more than one type.
* * **Flexible** and easy to code.
* * **Type Safety** as it can provide hints to help catch incorrect usage.

##### **`Optional`:**

`Optional` in Python means a value can be **either a specific type or *None***.

It's a shorthand for: `Union[type, None]`

```
from typing import Optional

def greet(name: Optional[str]) -> None:
    if name:
        print(f"Hello {name}!")
    else:
        print("Hello, stranger!")
```

* * In this case *name* can either **be** a **str** or a **None**.
* * It **cannot be anything else.**

##### **`Any`:**

`Any` in Python's typing system means a value be **of any type**, and type checkers **won't enforce** any restrictions on it.

```
from typing import Any

def process(data: Any) -> None:
    print(data)
```

* * Anything and everything is allowed!

##### **`Lambda: lambda`:**

In Python, a `lambda` is just an **anonymous (inline) function**, and in **type annotations**, you can descrbe its type using `Callable`.

```
from typing import Callable

f: Callable[[int], str] = lambda x: str(x)
```

```
square = lambda x: x * x
square(10)
```

```
nums = [1, 2, 3, 4]
squares = list(map(lambda x: x * x, nums))
```

* In Python `map()` is a built-in function that **applies a function to each item in an iterable** (like a list) and returns a **map object** (an iterator). *It's also efficient.*

* * Lambda is just a **shortcut** to writing small functions!
* * It's efficient.

### LangGraph Elements

#### `State`:

* The `State` is a shared data structure that holds the current information or context of the entire application.
* In simple terms, it is like the application's **memory**, keeping track of the variables and data that *nodes* can access and modify as they execute.
* **Analogy:** **whiteboard in a Meeting room**: Participants *(nodes)* write and read information on the whiteboard *(state)* to stay updated and coordinate actions.

#### `Nodes`:

* `Nodes` are individual *functions or operations* that perform *specific tasks* within the graph.
* Each node receives *input (often the current state)*, **process** it, and **produces** an **output** or an **updated state.**
* **Analogy**: **Assembly Line Stations:** Each station does one job - attach a part, paint it, inspect quality, etc.

#### `Graph`:

* A `Graph` in `LangGraph` is the overarching structure that maps out how different *tasks (nodes)* are connected and executed.
* It visually represents the *workflow*, showing the sequence and conditional paths between various operations.
* **Analogy:** **Road map:** A road map displaying the different routes connecting cities, with intersections offering choices on which path to take next.
 
#### `Edges`:

* `Edges` are the connections between **nodes** that determine the flow of execution.
* They tell us which node should be executed next after the current one completes its task.
* **Analogy:** **Train Tracks:** Each *track (edge)* connects the *stations (nodes)* togheter in a specific direction.

#### `Conditional Edges`:

* `Conditional Edges` are specialized connections that decide the next node to execute based on specific conditions or logic applied to the current state.
* **Analogy:** **Traffic Lights:** Green means go one way, red means stop, yellow means slow down. The condition (light color) decides the next step.

#### `START Node`:

* The `START node` is a **virtual entry point** in **LangGraph**, marking where the workflow begins.
* It doesn't ***perform any operations itself***, but serves as the ***designated starting position*** for the graph's execution.
* **Analogy:** **Race Starting Line:** The place where a race officially begins.

#### `END Node`:

* The `END Node` signifies the ***conclusion of the workflow in LangGraph***.
* Upon reaching this node, the graph's execution stops, indicating that all intended processes have been completed.
* **Analogy:** **Finish Line in a Race:** The race is over when you cross it.

#### `Tools`:

* `Tools` are specialized ***functions*** or ***utilities*** that nodes can utilize to perform specific tasks such as ***fetching data from an API.***
* They enhance the capabilities of nodes by providing ***additional functionalities.***
* ***Nodes*** are ***part of the graph structure***, while ***tools are functionalities used within nodes.***
* **Analogy:** **Tools in a Toolbox:** A hammer for nails, a screwdriver for screws, each tool has a distinct purpose.

#### `ToolNode`:

* A `ToolNode` is just a ***special kind of node*** whose main job is **to run a tool.**
* It connects the tool's output back into the `State`, so other nodes can use that information.
* **Analogy:** **Operator Using a Machine:** The *operator
(ToolNode)* controls the *machine (Tool)*, then takes the results back to the assembly line.

#### `StateGraph`:

* A `StateGraph` is a class in `LangGraph` used to ***build and compile*** the graph structure.
* it ***manages nodes, edges, and the overall state***, ensuring that the workflow operates in a unified way and that data flows correctly between components.
* **Analogy:** **Blueprint of a Building:** Just as a blueprint outlines the design and connections within a building, a `StateGraph` defines the structure and flow of the workflow.

#### `Runnable`:

* A `Runnable` in `LangGraph` is a ***standardized, executable component*** that performs a specific task within an AI workflow.
* It serves as a fundamental building block, allowing for us to create modular systems.
* `Runnable` vs `Node`: A `Runnable` can represent various operations, whereas the `Node` typically receives a `State`, performs an action on it, and then updates the `State`.
* **Analogy:** **LEGO Bricks:** Just as LEGO bricks can snapped togheter to build complex structures, `Runnables` can be combined to create sophisticated AI workflows.

#### `Messages`:

* `HumanMessage`: Represents input from a user.
* `SystemMessage`: Used to provide instructions or context to the model.
* `Function Message`: Represents the result of a function call
* `AIMessage`: Represents responses generated by AI models.
* `ToolsMessage`: Similar to `FunctionMessage`, but specific to **tool** usage.