Getting Started
================

The simplest Citus file could look like this:

.. code:: python

  import citus

  app = citus.App()


  @app.get("/")
  async def root():
      return "Hello World"


Copy that to a file `main.py`.

Run the live server:

.. code:: console
  
   $ citus main:app --reload

.. code:: html

  INFO:     Citus is running on http://127.0.0.1:8000 (Press CTRL+C to quit)
  INFO:     Started reloader process [28720]
  INFO:     Started server process [28722]
  INFO:     Waiting for application startup.
  INFO:     Application startup complete.



.. note::

    The command `citus main:app` refers to:

    * `main`: the file `main.py` (the Python "module").
    * `app`: the object created inside of `main.py` with the line `app = quo.App()`.
    * `--reload` or `-r`: make the server restart after code changes. Only use for development.

In the output, there's a line with something like:

.. code:: console

INFO:     Citus is running on http://127.0.0.1:8000 (Press CTRL+C to quit)

That line shows the URL where your app is being served, in your local machine.

Check it
--------

Open your browser at http://127.0.0.1:8000

You will see the JSON response as:

.. code:: console

  "Hello World"

Interactive API docs
---------------------

Now go to <a href="http://127.0.0.1:8000/docs" class="external-link" target="_blank">http://127.0.0.1:8000/docs</a>.

You will see the automatic interactive API documentation (provided by <a href="https://github.com/swagger-api/swagger-ui" class="external-link" target="_blank">Swagger UI</a>):

![Swagger UI](https://fastapi.tiangolo.com/img/index/index-01-swagger-ui-simple.png)

Alternative API docs
----------------------

And now, go to <a href="http://127.0.0.1:8000/redoc" class="external-link" target="_blank">http://127.0.0.1:8000/redoc</a>.

You will see the alternative automatic documentation (provided by <a href="https://github.com/Rebilly/ReDoc" class="external-link" target="_blank">ReDoc</a>):

![ReDoc](https://fastapi.tiangolo.com/img/index/index-02-redoc-simple.png)

OpenAPI
--------

**Citus** generates a "schema" with all your API using the **OpenAPI** standard for defining APIs.

Schema
-------

A "schema" is a definition or description of something. Not the code that implements it, but just an abstract description.

API "schema"
------------

In this case, https://github.com/OAI/OpenAPI-Specification is a specification that dictates how to define a schema of your API.

This schema definition includes your API paths, the possible parameters they take, etc.

Data "schema"
--------------

The term "schema" might also refer to the shape of some data, like a JSON content.

In that case, it would mean the JSON attributes, and data types they have, etc.

OpenAPI and JSON Schema
--------------------------

OpenAPI defines an API schema for your API. And that schema includes definitions (or "schemas") of the data sent and received by your API using **JSON Schema**, the standard for JSON data schemas.

Check the `openapi.yml`
------------------------------

If you are curious about how the raw OpenAPI schema looks like, Citus automatically generates a yaml (schema) with the descriptions of all your API.

You can see it directly at: http://127.0.0.1:8000/openapi.yml

It will show a JSON starting with something like:

.. code:: yml
{
    "openapi": "3.0.2",
    "info": {
        "title": "FastAPI",
        "version": "0.1.0"
    },
    "paths": {
        "/items/": {
            "get": {
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {






What is OpenAPI for? 
---------------------

The OpenAPI schema is what powers the two interactive documentation systems included.

And there are dozens of alternatives, all based on OpenAPI. You could easily add any of those alternatives to your application built with **FastAPI**.

You could also use it to generate code automatically, for clients that communicate with your API. For example, frontend, mobile or IoT applications.

## Recap, step by step

Step 1: import `Citus`
----------------------

```Python hl_lines="1"
{!../../../docs_src/first_steps/tutorial001.py!}
```

### Step 2: create a `FastAPI` "instance"

```Python hl_lines="3"
{!../../../docs_src/first_steps/tutorial001.py!}
```

Here the `app` variable will be an "instance" of the class `FastAPI`.

This will be the main point of interaction to create all your API.

This `app` is the same one referred by `uvicorn` in the command:

<div class="termy">

```console
$ uvicorn main:app --reload

<span style="color: green;">INFO</span>:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

</div>

If you create your app like:

```Python hl_lines="3"
{!../../../docs_src/first_steps/tutorial002.py!}
```

And put it in a file `main.py`, then you would call `uvicorn` like:

<div class="termy">

```console
$ uvicorn main:my_awesome_api --reload

<span style="color: green;">INFO</span>:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

</div>

### Step 3: create a *path operation*

Path
------

The path resides after the hostname and is separated by “/” (forward slash).
A path can comprise of any asset file extension, like `.jpg`, `.pdf` etc

So, in a URL like:

.. code:: console

  https://example.com/items/foo

...the path would be:

.. code:: console

  /items/foo

.. note::

    A "path" is also commonly called an "endpoint" or a "route".

While building an API, the "path" is the main way to separate "concerns" and "resources".

HTTP Methods
------------
The primary HTTP methods are `POST`, `GET`, `PUT`, `PATCH`, and `DELETE`. These correspond to create, read, update, and delete (or CRUD) operations, 

.. note::

  CRUD is an acronym that refers to the four functions that are considered necessary to implement a persistent storage application: create, read, update and delete.

There are a number of other methods, but are utilized less frequently.

*  `OPTIONS`
*  `HEAD`
*  `TRACE`


Defining a *path HTTP method decorator*
---------------------------------------

The :func:`@app.GET("/")` tells **Citus** that the function right below is in charge of handling requests that go to:

* the path `/`

You can also use the other operations:

* `@app.POST()`
* `@app.PUT()`
* `@app.DELETE()`

And the more exotic ones:

* `@app.OPTIONS()`
* `@app.HEAD()`
* `@app.P()`
* `@app.trace()`


Define the **path operation function**
---------------------------------------

This is our "**path operation function**":

* **path**: is `/`.
* **operation**: is `get`.
* **function**: is the function below the "decorator" (below `@app.get("/")`).

```Python hl_lines="7"
{!../../../docs_src/first_steps/tutorial001.py!}
```

This is a Python function.

It will be called by **FastAPI** whenever it receives a request to the URL "`/`" using a `GET` operation.

In this case, it is an `async` function.

---

You could also define it as a normal function instead of `async def`:

```Python hl_lines="7"
{!../../../docs_src/first_steps/tutorial003.py!}
```

!!! note
    If you don't know the difference, check the [Async: *"In a hurry?"*](../async.md#in-a-hurry){.internal-link target=_blank}.

### Step 5: return the content

```Python hl_lines="8"
{!../../../docs_src/first_steps/tutorial001.py!}
```

You can return a `dict`, `list`, singular values as `str`, `int`, etc.

You can also return Pydantic models (you'll see more about that later).

There are many other objects and models that will be automatically converted to JSON (including ORMs, etc). Try using your favorite ones, it's highly probable that they are already supported.

