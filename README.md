tmux-chooser
============

Session chooser for busy people with lots of tmux sessions everywhere

Screenshot
----------

TODO

Dependencies
------------

tmux-chooser is written in Python (tested on Python 2.7) and depends the
Paramiko module for the ssh communication.

Installation
------------

TODO: update this once PyPI support is there.

For now, just make sure you have python and paramiko installed and then put
tmux-chooser in your path.

Using it
--------

### Running ###

In a terminal, outside a tmux session, start `tmux-chooser`.

It will show the existing tmux sessions on localhost by default.

You can use the following keys:
 * Arrows to navigate left - right between servers
 * Arrows to navigate up - down in session lists
 * `Enter` connects to the selected session
 * `c` creates a new session on the selected server
 * `k` kills a session. Watch out, There is no confirmation dialog!
 * `q` quits tmux-chooser without attaching to a session

### Problems? ###

The most likely source of problems are ssh connection issues. Make sure that:
 1. The serves you are connected to are in your `~/.ssh/known_hosts` file
 2. You can access the servers without a password, using ssh keys (this avoids
    the need for `tmux-chooser` to prompt or remember passwords and all related
    potential security problems)

Check the paramiko logs in `/tmp/paramiko.<PID>.log` to get a clue of what
might be the problem.

### Configuration ###

TODO: more words

 * `servers`: list
 * `ssh_log`: bool
 * `user`: string

Found bugs?
-----------

File report in the [issue tracker](https://github.com/peter-d/tmux-chooser/issues).
