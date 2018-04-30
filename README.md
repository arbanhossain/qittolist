# qittolist
#### a to-do app for command line interface

Qitto helps developers and people to keep track of the stuff they have to do, right in the terminal. This comes in handy if you are the type who spends a lot of time using the command line. Qitto uses 'Click', this is installed while running ```setup.py```. The script works on both Windows and Linux (I don't own a Mac, so can't guarantee that)

### What you need to do
- Download the repository or clone it
- Open your terminal and browse to the folder that contains the two scripts. Like this: 
    ```
    ./
    |- qittolist.py
    |- setup.py
    ```
- Then simply install it by running either
    ```
    $ python setup.py install
    ```
    or
    ```
    $ pip install --editable .
    ```
    You might need to have Python 3 installed (which you probably have, or else you wouldn't use an app which uses CLI)
    If you're on Linux and have both versions of Python installed you maybe need to use ```python3``` or ```pip3```
- Then you can use the app by typing in ```qitto```

### How to use it
Qitto uses four commands:
- ```add```- This is used to add a new entry to your list
    ```
    $ qitto add
      Enter what to do: push project to github
    ```
- ```show```- This is used for showing your current to-do list
    ```
    $ qitto show

      ID      Date                    Status  Todo

      1       29-04-2018 16:04        Undone  push project to github
      -------------------------------------------------------------
      
    ```
- ```done```- This is used for marking an entry as 'Done'
    ```
    $ qitto done 1
      Marked No. 1 as Done!
    $ qitto show

      ID      Date                    Status  Todo

      1       29-04-2018 16:04        Done    push project to github
      -------------------------------------------------------------
    ```
- ```rem```- This is used to remove an entry
    ```
    $ qitto rem 1
      Are you sure you want to remove this entry? [y/N]: y
      Removed!
    $ qitto show

      ID      Date                    Status  Todo
    ```

### Why not Argparser?
I am a consistent user of Argparser myself and will stick to using it. The reason I used Click instead of Argparser is that this project was a quick challenge with my friend so I chose click as it allows building the interface faster and at a simpler way.

### Contribute
At this moment, I can't think of anything else that increases productivity without breaking the core concept, ease of use of the app. I'd welcome any feature that sticks to this rule (I even changed the name of the app a few time so that the user doesn't have any trouble typing ```qitto```). Either way, you are free to make a pull request