# Software installation

- **IDE**: [Pycharm](https://www.jetbrains.com/pycharm/download). Student version or Community Edition. VSCode is not that good for Python development.
- **Git UI**: [Sourcetree](https://www.sourcetreeapp.com/) (for Windows)
- **Diff viewer**: [WinMerge](https://winmerge.org/downloads) (for Windows) or [Meld](https://meldmerge.org/). Or Beyond Compare (pirated version)

# Software setup

### Install python

Install any recent (3.12, 3.13, 3.14, etc.) version of Python on your machine.

### Using Python virtual environments

It is recommended to use a separate Python virtual environment for each project.
We create the virtual environment once and use it whenever working on that project.

Use these commands to create and use it:
```shell
# Create a directory that holds your virtual environments
$ mkdir ~/.envs

$ python3.14 -m venv ~/.envs/bst # Here "bst" is the virtual environment name

$ source ~/.envs/bst/bin/activate # Activate the virtual environment
(bst) $  # Notice that the command line prompt changes with (bst) prefix once you're in the virtual environment
```

Or, for Windows:
```shell
C:\Users\Name> mkdir envs
C:\Users\Name> python3.14 -m venv ~/.envs/bst # Create new virtual environment named "bst"
C:\Users\Name> .\envs\bst\Scripts\activate # Activate the environment
(bst) C:\Users\Name> 
```

> ℹ️ Note<br>
> If you're using an IDE (PyCharm, VSCode, etc.), then for this project you will also need to ask
> the IDE to use this virtual environment.

### Install all required Python packages

Run this command once (in your virtual environment):
```shell
$ cd path/to/git/repository/  # Must be in the directory that contains the requirements.txt file
$ pip install -r requirements.txt
```

# Running the application

Ensure that the repository root directory is added into your Python module search path. 
This can be done by running this command once in every new terminal window. 
Without it, you'll get an `ImportError`. 
```shell
# Add the current directory to Python's module search path. 
# I think that this is not needed for Windows as Windows always includes current directory into Python module search path. 

$ export PYTHONPATH=. # For UNIX  
$ set PYTHONPATH=.    # For Windows
```

Use this command to run the application:
```shell
$ python bst/main.py -j assets/job_2.txt 
```

You should see this output:
```log
INFO     Starting the application...
DEBUG    Parsed 7 lines from input job file
INFO     Processing line  0: insert 5
DEBUG
5

INFO     Processing line  1: insert 2
SUCCESS  Inserted value: 2 into the tree
DEBUG
  5
 /
2

INFO     Processing line  2: insert 10
SUCCESS  Inserted value: 10 into the tree
DEBUG
  5
 / \
2   10

INFO     Processing line  3: insert 3
SUCCESS  Inserted value: 3 into the tree
DEBUG
  __5
 /   \
2     10
 \
  3

INFO     Processing line  4: insert 7
SUCCESS  Inserted value: 7 into the tree
DEBUG
  __5__
 /     \
2       10
 \     /
  3   7

INFO     Processing line  5: insert 15
SUCCESS  Inserted value: 15 into the tree
DEBUG
  __5__
 /     \
2       10
 \     /  \
  3   7    15

INFO     Processing line  6: delete 7
SUCCESS  Deleted value: 7 from the tree
DEBUG
  __5
 /   \
2     10
 \      \
  3      15

INFO     All done!
```
> ℹ️ Note<br>
> To simply things, we do not support duplicate values in this repo. 
> I.e., the tree will have at max one node per node value.


---

# Learning track: Theory

1. Algorithms:
   1. Understand Big-O notations (for **time complexity**). We use it for comparing algorithms.
   2. Which one is a better algorithm: O(2<sup>N</sup>), O(N), O(N<sup>2</sup>), or O(logN)? And why?
   3. **Optional**: Big-O notation for representing an algorithm's **space complexity**.
2. Binary Trees:
   1. Trees vs binary trees (this is straightforward).
   2. Binary Tree vs Complete Binary Tree (this is straightforward).
   3. What is "rank" of a tree node?
3. Binary Search Trees (BST):
   1. Understand BSTs.
   2. BST vs balanced BST.
   3. Why balanced BSTs enable us to have a `log(N)` time complexity for insert, search, and deletion operations.
   4. Once you understand BST, write pseudocode for BST search, insert, and delete functions. 
   5. **Optional**: Understand the three types of traversals for any trees: in-order, pre-order, post-order.
4. AVL Trees (a type of BST):
   1. Understand how AVL trees balance the BST.
   2. Write pseudocode for search, insert, and deletion operations in AVL trees.


# Learning track: Coding

This repository contains a working implementation of BST.
And now, we want to extend it by adding support for balancing. 
There are many types of balanced BSTs. **We will implement the AVL trees in this repository**.  

1. Set up the project on your local machine.
2. You should be able to run the application and see the expected output as documented in this Readme file.
3. Feel free to play around with the `./assets/jobs*.txt` files and run the application.
4. Learn to use debugger in your IDE. You should be able to:
   1. Fire up a debugging session.
   2. Place a breakpoint. Make the execution stop at any desired line of code.
   3. At a breakpoint:
      1. Inspect the value of any variable. 
      2. Run a custom Python statement (say `print(x*10 + 56)`).
      3. Edit a local variable's value and continue the execution.
   4. Place a **conditional** breakpoint somewhere in your code. You can use any variable's value as the condition. Say `x > 3`.
5. Once ready, please implement the TODOs listed in the `./bst/avl.py` file.
6. You should add new files in the `./assets/` directory and test the correctness of your work. Feel free to commit these files into Git repo. 
   Test a variety of corner cases to ensure that your code can indeed handle them.

---

TODO: 
 - x