# Todo-CLI
A simple todo manager CLI program using python.

1. Install python3
2. Open Shell or Command prompt
3. Type 
     python3 ./todo.py #argument#

Examples:
 1. Get help:

    ```
    $ python3 todo.py help
    Usage :-
    $ ./todo add "todo item"  # Add a new todo
    $ ./todo ls               # Show remaining todos
    $ ./todo del NUMBER       # Delete a todo
    $ ./todo done NUMBER      # Complete a todo
    $ ./todo help             # Show usage
    $ ./todo report           # Statistics
    ```

 2. Adding todo item:

    ```
    $ python3 todo.py add "Lock the gate"
    Added todo: Lock the gate
    ```

 3. List all todo items:

    ```
    $ python3 todo.py ls
    [3] Switch off the lights
    [2] Wash cloths
    [1] Lock the gate
    ```

 4. Mark an item as done:

    ```
    $ python3 todo.py done 2
    Marked todo #2 as done
    ```

 5. Delete an todo item

    ```
    $ python3 todo.py del 1
    Deleted todo #1
    ```

6. Get report 

    ```
    $ python3 todo.py report
    2020-12-26 Pending : 1 Completed : 1
    ```
