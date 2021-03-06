[![Downloads](https://pepy.tech/badge/citus)](https://pepy.tech/project/citus)
[![PyPI version](https://badge.fury.io/py/citus.svg)](https://badge.fury.io/py/citus)
[![Wheel](https://img.shields.io/pypi/wheel/citus.svg)](https://pypi.com/project/citus)
[![Windows Build Status](https://img.shields.io/appveyor/build/gerrishons/citus/main?logo=appveyor&cacheSeconds=600)](https://ci.appveyor.com/project/gerrishons/citus)
[![pyimp](https://img.shields.io/pypi/implementation/citus.svg)](https://pypi.com/project/citus)
[![RTD](https://readthedocs.org/projects/citus/badge/)](https://citus.readthedocs.io)
[![licence](https://img.shields.io/pypi/l/citus.svg)](https://opensource.org/licenses/MIT)
[![Twitter Follow](https://img.shields.io/twitter/follow/gerrishon_s.svg?style=social)](https://twitter.com/gerrishon_s)


[![Logo](https://raw.githubusercontent.com/secretum-inc/citus/main/docs/images/citus.png)](https://github.com/secretum-inc/citus)


`Forever Scalable`

**𝙲𝚒𝚝𝚞𝚜** is a python based, ultrafast web framework  focusing on composing Web APIs all the more rapidly and with needless baggage. 

Citus requires Python `3.8` or later. 


## Features
The key features are:

- [x] **Fast**: Very high performance, on par with **NodeJS** and **Go** (thanks to Starlette and Pydantic). [One of the fastest Python frameworks available](#performance).

- [x] **Fast to code**: Increase the speed to develop features by about 200% to 300%. *
- [x] **Fewer bugs**: Reduce about 40% of human (developer) induced errors. *
- [x] **Intuitive**: Great editor support. <abbr title="also known as auto-complete, autocompletion, IntelliSense">Completion</abbr> everywhere. Less time debugging.
- [x] **Easy**: Designed to be easy to use and learn. Less time reading docs.
- [x] **Short**: Minimize code duplication. Multiple features from each parameter declaration. Fewer bugs.
- [x] **Robust**: Get production-ready code. With automatic interactive documentation.
- [x] **Standards-based**: Based on (and fully compatible with) the open standards for APIs: <a href="https://github.com/OAI/OpenAPI-Specification" class="external-link" target="_blank">OpenAPI</a> (previously known as Swagger) and <a href="https://json-schema.org/" class="external-link" target="_blank">JSON Schema</a>.

<small>* estimation based on tests on an internal development team, building production applications.</small>
- [x] Support for Ansi, RGB and HTML color models
- [x] Support for tabular presentation of data
- [x] Interactive progressbars
- [x] Code completions
- [x] Nesting of commands
- [x] Automatic help page generation
- [x] Syntax highlighting
- [x] Autosuggestions
- [x] Key Binders

## Getting Started
### Installation
You can install citus via the Python Package Index (PyPI)

```
pip install -U citus
```

## Example

### Create it

* Create a file `main.py` with:

```Python
from typing import Optional

import citus

app = citus.App()


@app.GET("/")
def read_root():
    return "Hello World"


@app.GET("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
```

<details markdown="1">
<summary>Or use <code>async def</code>...</summary>

If your code uses `async` / `await`, use `async def`:

```Python hl_lines="9  14"
from typing import Optional
import quo

app = citus.App()


@app.GET("/")
async def read_root():
    return "Hello World"


@app.GET("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
```


**Note**:

If you don't know, check the _"In a hurry?"_ section about <a href="https://fastapi.tiangolo.com/async/#in-a-hurry" target="_blank">`async` and `await` in the docs</a>.

</details>

### Run it

Run the server with:

<div class="termy">

```console
$ citus main:app --reload

INFO:     Citus running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [28720]
INFO:     Started server process [28722]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

</div>

<details markdown="1">
<summary>About the command <code>uvicorn main:app --reload</code>...</summary>

The command `citus main:app` refers to:

* `main`: the file `main.py` (the Python "module").
* `app`: the object created inside of `main.py` with the line `app = citus.App()`.
* `--reload` or `-r`: make the server restart after code changes. Only do this for development.

</details>

## Example upgrade

Now modify the file `main.py` to receive a body from a `PUT` request.

Declare the body using standard Python types, thanks to Pydantic.

```Python hl_lines="4  9-12  25-27"
from typing import Optional

import citus

app = citus.App()


class Item(citus.Base):
    name: str
    price: float
    is_offer: Optional[bool] = None


@app.GET("/")
def read_root():
    return "Hello World"


@app.GET("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.GET("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
```

The server should reload automatically (because you added `--reload` to the command above).

### Check it

Open your browser at <a href="http://127.0.0.1:8000/items/33?q=checkuser" class="external-link" target="_blank">http://127.0.0.1:8000/items/33?q=checkuser</a>.

You will see the JSON response as:

```JSON
{"item_id": 33, "q": "checkuser"}
```

You already created an API that:

* Receives HTTP requests in the _paths_ `/` and `/items/{item_id}`.
* Both _paths_ take `GET` <em>operations</em> (also known as HTTP _methods_).
* The _path_ `/items/{item_id}` has a _path parameter_ `item_id` that should be an `int`.
* The _path_ `/items/{item_id}` has an optional `str` _que

## Getting Help

### Community

For discussions about the usage, development, and the future of quo, please join our Google community

* [Community👨‍👩‍👦‍👦](https://groups.google.com/forum/#!forum/secretum)

## Resources

### Bug tracker

If you have any suggestions, bug reports, or annoyances please report them
to our issue tracker at 
[Bug tracker](https://github.com/secretum-inc/citus/issues/) or send an email to:

 📥 secretum@googlegroups.com


## License📑

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)  
This software is licensed under the `MIT License`. See the [License](https://github.com/secretum-inc/citus/blob/main/LICENSE) file in the top distribution directory for the full license text.


## Code of Conduct
Code of Conduct is adapted from the Contributor Covenant,
version 1.2.0 available at
[Code of Conduct](http://contributor-covenant.org/version/1/2/0/)

