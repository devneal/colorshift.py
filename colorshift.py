#!/usr/bin/python
import argparse
import os
import signal
import sys

DEFAULT_XRESOURCES = os.path.expanduser('~/.Xresources')

parser = argparse.ArgumentParser()
parser.add_argument("colorscheme", help="the .Xresources colorscheme to use")
parser.add_argument("-a", "--all",
                    help="change colors on all urvxt instances",
                    action="store_true")
parser.add_argument("-x", "--xresources",
                    help="path to the .Xresources file",
                    default=DEFAULT_XRESOURCES)
args = parser.parse_args()

def get_process_name(pid):
    return os.popen("ps -o comm= -p {}".format(pid)).read().strip()

def get_parent_pid(pid):
    return int(os.popen("ps -o ppid= -p {}".format(pid)).read().strip())

# get absolute path to colorscheme
if os.path.isabs(args.colorscheme):
    colorscheme_path = args.colorscheme
elif args.colorscheme.startswith('~'):
    colorscheme_path = os.path.expanduser(args.colorscheme)
else:
    colorscheme_path = os.getcwd() + os.sep + args.colorscheme
colorscheme_path = os.path.realpath(colorscheme_path)

# verify that the colorscheme exists
new_file_contents = ""
if os.path.isfile(colorscheme_path):
    new_file_contents = '#include ' + '\"' + colorscheme_path + '\"\n'
else:
    print "Could not find colorscheme {}".format(colorscheme_path)
    exit(1)

# overwrite .Xresources file
with open(args.xresources, 'r') as fin:
    fin.readline() # ignore old colorscheme
    new_file_contents += fin.read()

with open(args.xresources, 'w') as fout:
    fout.write(new_file_contents);

# update urxvt
os.system('xrdb ' + args.xresources)
if args.all:
    urxvt_pids = map(int, os.popen("pidof urxvt").read().split())
    for pid in urxvt_pids:
        os.kill(pid, signal.SIGHUP)
else:
    urxvt_pid = os.getppid()
    while get_process_name(urxvt_pid) != "urxvt":
        urxvt_pid = get_parent_pid(urxvt_pid)

    os.kill(urxvt_pid, signal.SIGHUP)
