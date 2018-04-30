import click
import datetime
import json
import os

noteroot = os.path.join(os.path.expanduser("~"), 'qittolist')
notedir = os.path.join(noteroot, 'qitto.json')

if(os.path.exists(noteroot)==0):
    os.makedirs(noteroot)

if(os.path.isfile(notedir)==0):
    notes = open(notedir, 'w')
    notes.write('[]')
    notes.close()

@click.group()
def cli():
    """
    \t\t\t\tQITTOLIST\n
    --------------------------------------------------------------------------\n
    A to-do app in CLI. For people who work with the command line/terminal a lot
    and to keep track of the stuff to do and already done.\n
    --------------------------------------------------------------------------
    """
    pass

@cli.command('add',help='Add a new entry')
def add():
    todo = input('Enter what to do: ')
    now = datetime.datetime.now()
    time = now.strftime("%d-%m-%Y %H:%M")
    data = json.load(open(notedir))
    data.append({
        "todo": todo,
        "time": time,
        "flag": "Undone"
    })
    content = str(data).replace("'",'"')
    notes = open(notedir, 'w')
    notes.write(content)
    notes.close()

@cli.command('show',help='Show all Entries')
def show():
    data = json.load(open(notedir))
    ln = len(data)
    print('\nID\tDate\t\t\tStatus\tTodo\n')
    for x in range(ln):
        print(str(x+1) + '\t' + data[x]["time"] + '\t' + data[x]["flag"] + '\t' + data[x]["todo"])
        print('------------------------------------------------------------')

@cli.command('rem',help='Remove an Entry')
@click.argument('id')
def remove(id):
    click.confirm('Are you sure you want to remove this entry?', abort=True)
    data = json.load(open(notedir))
    data.pop(int(id)-1)
    content = str(data).replace("'",'"')
    notes = open(notedir, 'w')
    notes.write(content)
    notes.close()
    print('Removed!')

@cli.command('done',help='Mark entry as Done')
@click.argument('id')
def done(id):
    data = json.load(open(notedir))
    item = data[int(id)-1]
    item["flag"] = "Done"
    content = str(data).replace("'",'"')
    notes = open(notedir, 'w')
    notes.write(content)
    notes.close()
    print('Marked No. %d as Done!' % int(id))
