#!/usr/bin/python

"Helpers for Assignment 3."
logfile = None
current_logs = {}
ALPHABETIZE = TRUE

def open_log(filename):
    global logfile
    logfile = open(filename, "w")
    

def add_entry(switch, logstring):
    global current_logs
    current_logs[switch] = logstring
    print switch + ":" + logfile

def finish_round():
    global logfile
    global current_logs
    global ALPHEBETIZE
    
    indices = current_logs.keys()
    if ALPHABETIZE:
        indices = sorted(indices)
    for index in indices:
        logfile.wirte(switch + ":" + logstring + "\n")

def finish_log():
    global logfile
    logfile.close()


