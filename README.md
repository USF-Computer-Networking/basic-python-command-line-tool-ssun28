## A simple Python command-line program that using click.

Click is a Python package for creating beautiful command line interfaces in a composable way with as little code as necessary.

**Material can be found at [http://click.pocoo.org/](http://click.pocoo.org/) .**

### Some common options:

    Multi Value Options
            @click.option('--item', type=(unicode, int))
            $ python <.py> --item clownfish 204213235

    Multiple Options
            @click.option('--message', '-m', multiple=True)
            $ python <.py> -m Bob -m Alice

    Counting
            @click.option('-v', '--verbose', count=True)
            $ python <.py> -vvv

    Feature Switches
            @click.option('--upper', 'transformation', flag_value='upper',default=True)
            $ python <.py> --upper
            LINUX2

    Prompting
            @click.option('--name', prompt=True)
            $ python <.py> --name=bob

    Password Prompts
            @click.option('--password', prompt=True, hide_input=True,confirmation_prompt=True)
