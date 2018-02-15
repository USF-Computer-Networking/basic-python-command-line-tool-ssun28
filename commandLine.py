#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
import sys

@click.group()
def cli():
	'''This is a Python command-line program that supports 8 different options'''
	pass

@click.command()
@click.option('--name', '-n',  default='xxx xxx', prompt='Type your name:', help='The person to greet.')
def name(name):
	click.echo('Hello %s!' % name)

@click.command()
@click.option('--item', '-i', 'item', type=(str, int), default=(None, 0), help='This is multi value options.')
def item(item):
	click.echo('nickname=%s id=%d' % item)

@click.command()
@click.option('--message', '-m', 'message', multiple=True, help='multiple option')
def message(message):
	click.echo('\n'.join(message))

@click.command()
@click.option('--verbose', '-v', 'verbose', count=True, help='counting')
def verbose(verbose):
	click.echo('Verbosity: %s' % verbose)

@click.command()
@click.option('--upper', '-u', 'transformation', flag_value='upper', default=True,help='Feature Switches')
def transformation(transformation):
	click.echo(getattr(sys.platform, transformation)())

@click.command()
@click.option('--password', '-p', 'password', prompt=True, hide_input=True, confirmation_prompt=True, help='Password Prompts')
def password(password):
	click.echo('Encrypting password to %s' % password.encode('rot13'))

@click.command()
@click.option('--count', type=click.IntRange(0, 20, clamp=True), help='Range Options')
@click.option('--digit', type=click.IntRange(0, 10), help='Range Options')
def repeat(count, digit):
	click.echo(str(digit) * count)

@click.command()
@click.argument('output', type=click.File('wb'))
def output(output):
	text = "this is a sample!"
	output.write(text)

cli.add_command(name)
cli.add_command(item)
cli.add_command(message)
cli.add_command(verbose)
cli.add_command(transformation)
cli.add_command(password)
cli.add_command(repeat)
cli.add_command(output)


if __name__ == '__main__':
	cli()