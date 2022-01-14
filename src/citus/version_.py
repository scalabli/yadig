#!/usr/bin/env python3
"""
A simple example of a a text area displaying "Hello World!".
"""
import platform
import citus
import quo


__version__ = "2022.1"

#quo.echo(
    #    "Running citus %s with %s %s on %s"
#  *  *    % (                                          #      citus.__version__,
    #        platform.python_implementation(),
   #         platform.python_version(),
    #        platform.system(),
    #    )                                          #  )
  #  clime.exit()
# Layout for displaying hello world.
# (The frame creates the border, the box takes care of the margin/padding.)

c_v = "citus.__version__"
root_container = quo.widgets.Box(
    quo.widgets.Frame(
        quo.widgets.TextArea(
            text=quo.inscribe(quo.text.HTML(f'Running <reverse>Citus</reverse> version <red>d</red>')),
            #f"Running Citus version {__version__} with {platform.python_implementation()}\n Press control-c to quit.",
            width=40,
            height=10,
        )
    ),
)
layout = quo.layout.Layout(container=root_container)


# Key bindings.
kb = quo.keys.KeyBinder()


@kb.add("ctrl-c")
def _(event):
    "Quit when control-c is pressed."
    event.app.exit()


# Build a main application object.
application = quo.Suite(
        layout=layout,
        bind=kb, 
        full_screen=True
        )


def main_():
    application.run()


if __name__ == "__main__":
    main_()
