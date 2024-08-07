# 0x02. Python - Async Comprehension

## Project Overview

In this project, you will learn about asynchronous comprehensions and generators in Python. You will create a coroutine that generates random numbers asynchronously, use async comprehensions to collect these numbers, and measure the runtime of multiple parallel comprehensions.

## Learning Objectives

At the end of this project, you are expected to be able to:

- Explain how to write an asynchronous generator.
- Use async comprehensions to collect asynchronous values.
- Type-annotate generators.

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `pycodestyle` style (version 2.5.x)
- The length of your files will be tested using `wc`
- All your modules should have a documentation (python3 -c 'print(**import**("my_module").**doc**)')
- All your functions should have a documentation (python3 -c 'print(**import**("my_module").my_function.**doc**)')
- A documentation is not a simple word, it’s a real sentence explaining what's the purpose of the module, class or method (the length of it will be verified)
- All your functions and coroutines must be type-annotated.

## Tasks

### 0. Async Generator

Write a coroutine called `async_generator` that takes no arguments. The coroutine will loop 10 times, each time asynchronously wait 1 second, then yield a random number between 0 and 10. Use the `random` module.

```bash
bob@dylan:~$ cat 0-main.py
#!/usr/bin/env python3

import asyncio

async_generator = __import__('0-async_generator').async_generator

async def print_yielded_values():
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)

asyncio.run(print_yielded_values())

bob@dylan:~$ ./0-main.py
[4.403136952967102, 6.9092712604587465, 6.293445466782645, 4.549663490048418, 4.1326571686139015, 9.99058525304903, 6.726734105473811, 9.84331704602206, 1.0067279479988345, 1.3783306401737838]
```

### 1. Async Comprehensions

Import `async_generator` from the previous task and then write a coroutine called `async_comprehension` that takes no arguments. The coroutine will collect 10 random numbers using an async comprehensing over `async_generator`, then return the 10 random numbers.

```bash
bob@dylan:~$ cat 1-main.py
#!/usr/bin/env python3

import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension

async def main():
    print(await async_comprehension())

asyncio.run(main())

bob@dylan:~$ ./1-main.py
[9.861842105071727, 8.572355293354995, 1.7467182056248265, 4.0724372912858575, 0.5524750922145316, 8.084266576021555, 8.387128918690468, 1.5486451376520916, 7.713335177885325, 7.673533267041574]
```

### 2. Run time for four parallel comprehensions

Import `async_comprehension` from the previous file and write a `measure_runtime` coroutine that will execute `async_comprehension` four times in parallel using `asyncio.gather`. `measure_runtime` should measure the total runtime and return it.

Notice that the total runtime is roughly 10 seconds, explain it to yourself.

```bash
bob@dylan:~$ cat 2-main.py
#!/usr/bin/env python3

import asyncio

measure_runtime = __import__('2-measure_runtime').measure_runtime

async def main():
    return await measure_runtime()

print(
    asyncio.run(main())
)

bob@dylan:~$ ./2-main.py
10.021936893463135
```

## Professional README

### Project Title: 0x02. Python - Async Comprehension

### Description

This project is an introduction to asynchronous comprehensions and generators in Python. It covers writing an asynchronous generator, using async comprehensions to collect asynchronous values, and measuring the runtime of multiple parallel comprehensions.

### Table of Contents

- [0. Async Generator](#0-async-generator)
- [1. Async # 0x02. Python - Async Comprehension

## Project Overview

In this project, you will learn about asynchronous comprehensions and generators in Python. You will create a coroutine that generates random numbers asynchronously, use async comprehensions to collect these numbers, and measure the runtime of multiple parallel comprehensions.

## Learning Objectives

At the end of this project, you are expected to be able to:

- Explain how to write an asynchronous generator.
- Use async comprehensions to collect asynchronous values.
- Type-annotate generators.

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `pycodestyle` style (version 2.5.x)
- The length of your files will be tested using `wc`
- All your modules should have a documentation (python3 -c 'print(**import**("my_module").**doc**)')
- All your functions should have a documentation (python3 -c 'print(**import**("my_module").my_function.**doc**)')
- A documentation is not a simple word, it’s a real sentence explaining what's the purpose of the module, class or method (the length of it will be verified)
- All your functions and coroutines must be type-annotated.

## Tasks

### 0. Async Generator

Write a coroutine called `async_generator` that takes no arguments. The coroutine will loop 10 times, each time asynchronously wait 1 second, then yield a random number between 0 and 10. Use the `random` module.

```bash
bob@dylan:~$ cat 0-main.py
#!/usr/bin/env python3

import asyncio

async_generator = __import__('0-async_generator').async_generator

async def print_yielded_values():
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)

asyncio.run(print_yielded_values())

bob@dylan:~$ ./0-main.py
[4.403136952967102, 6.9092712604587465, 6.293445466782645, 4.549663490048418, 4.1326571686139015, 9.99058525304903, 6.726734105473811, 9.84331704602206, 1.0067279479988345, 1.3783306401737838]
```

### 1. Async Comprehensions

Import `async_generator` from the previous task and then write a coroutine called `async_comprehension` that takes no arguments. The coroutine will collect 10 random numbers using an async comprehensing over `async_generator`, then return the 10 random numbers.

```bash
bob@dylan:~$ cat 1-main.py
#!/usr/bin/env python3

import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension

async def main():
    print(await async_comprehension())

asyncio.run(main())

bob@dylan:~$ ./1-main.py
[9.861842105071727, 8.572355293354995, 1.7467182056248265, 4.0724372912858575, 0.5524750922145316, 8.084266576021555, 8.387128918690468, 1.5486451376520916, 7.713335177885325, 7.673533267041574]
```

### 2. Run time for four parallel comprehensions

Import `async_comprehension` from the previous file and write a `measure_runtime` coroutine that will execute `async_comprehension` four times in parallel using `asyncio.gather`. `measure_runtime` should measure the total runtime and return it.

Notice that the total runtime is roughly 10 seconds, explain it to yourself.

```bash
bob@dylan:~$ cat 2-main.py
#!/usr/bin/env python3

import asyncio

measure_runtime = __import__('2-measure_runtime').measure_runtime

async def main():
    return await measure_runtime()

print(
    asyncio.run(main())
)

bob@dylan:~$ ./2-main.py
10.021936893463135
```

## Professional README

### Project Title: 0x02. Python - Async Comprehension

### Description

This project is an introduction to asynchronous comprehensions and generators in Python. It covers writing an asynchronous generator, using async comprehensions to collect asynchronous values, and measuring the runtime of multiple parallel comprehensions.

### Table of Contents

- [0. Async Generator](#0-async-generator)
- [1. Async Comprehensions](#1-async-comprehensions)
- [2. Run time for four parallel comprehensions](#2-run-time-for-four-parallel-comprehensions)

### 0. Async Generator

The `async_generator` coroutine is a generator that yields random numbers asynchronously. It uses the `random` module to generate random numbers between 0 and 10. The coroutine waits for 1 second between each yield to simulate asynchronous behavior.

### 1. Async Comprehensions

The `async_comprehension` coroutine uses an async comprehension to collect 10 random numbers from the `async_generator` coroutine. This demonstrates the power of async comprehensions in Python, allowing for concise and efficient asynchronous code.

### 2. Run time for four parallel comprehensions

The `measure_runtime` coroutine measures the total runtime of executing the `async_comprehension` coroutine four times in parallel using `asyncio.gather`. The total runtime is roughly 10 seconds. This is because the `async_comprehension` coroutine is waiting for 1 second between each yield, and there are four coroutines running in parallel. Since each coroutine takes 10 seconds to complete, the total runtime is 40 seconds. However, due to the asynchronous nature of the coroutines, the actual runtime is much shorter, around 10 seconds.

### Usage

To run the provided examples, simply execute the corresponding Python files (`0-main.py`, `1-main.py`, or `2-main.py`). The output will be displayed in the terminal.

### Requirements

- Python 3.7 or higher
- `asyncio` library
- `random` library

### Author

[Emmanuel Paul](https://github.com/emmanuelist) - [emmanuel.paul75@yahoo.com](mailto:emmanuel.paul75@yahoo.com)

### License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

### Acknowledgments

- [Python Documentation](https://docs.python.org/3/)
- [PEP 530 - Asynchronous Comprehensions](https://www.python.org/dev/peps/pep-0530/)
- [What's New in Python: Asynchronous Comprehensions / Generators](https://docs.python.org/3/whatsnew/3.6.html#whatsnew36-pep525)
- [Type-hints for generators](https://docs.python.org/3/library/typing.html#typing.Generator)
-
