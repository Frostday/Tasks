from classes import A, B, C
import pickle
import os
import click

file_name = 'classes/data.pkl'

if os.path.exists(file_name):
    open_file = open(file_name, "rb")
    classes_list = pickle.load(open_file)
    open_file.close()
else:
    classes_list = []
print(classes_list)


@click.group()
def messages():
    pass


@click.command(short_help='Add a new class object')
@click.option(
    '--name',
    '-n',
    help='Enter name of object.',
    required=True,
)
@click.option(
    '--type',
    '-t',
    help='Enter type of class - A, B or C.',
    required=True,
)
def add(name, type):
    if type == 'A':
        new_class = A(name)
    elif type == 'B':
        new_class = B(name)
    elif type == 'C':
        new_class = C(name)
    classes_list.append(new_class)
    print(classes_list)
    open_file = open(file_name, "wb")
    pickle.dump(classes_list, open_file)
    open_file.close()


@click.command(short_help='Delete a class object')
@click.option(
    '--name',
    '-n',
    help='Enter name of object.',
    required=True,
)
def delete(name):
    for i in range(len(classes_list)):
        if classes_list[i].name == name:
            del classes_list[i]
            break
    print(classes_list)
    open_file = open(file_name, "wb")
    pickle.dump(classes_list, open_file)
    open_file.close()


@click.command(short_help='Execute a class object')
@click.option(
    '--name',
    '-n',
    help='Enter name of object.',
    required=True,
)
@click.option(
    '--args',
    '-a',
    help='Enter comma separated arguments inside [] with no spaces.',
    required=False,
    multiple=True
)
def execute(name, args):
    data = {}
    if args:
        args = args[0][1:-1].split(',')
        for i in range(len(args)):
            data[i+1] = args[i]
    for i in range(len(classes_list)):
        if classes_list[i].name == name:
            classes_list[i].execute(data)
            break
    print(classes_list)
    open_file = open(file_name, "wb")
    pickle.dump(classes_list, open_file)
    open_file.close()


messages.add_command(add)
messages.add_command(delete)
messages.add_command(execute)
messages()
