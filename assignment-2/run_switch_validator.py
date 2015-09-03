# Assignment 2 output validator for CS 6250 (OMS).
# auth Angela Smiley (based on Assignment 3 output validator by Michael Brown.)

# This output validator is designed to check the student's result log files for errors.
# Errors detected (both):
# Missing or extra columns in log entries.

# Errors detected (static):
# Invalid switch names (not in the sample topology).
# Invalid ports (not in the sample topology).
# Invalid MAC addresses (not in the sample topology).

# Errors detected (learning):
# Missing call to next_entry()

import sys
import re

line_number = 1

def validateStudentOutput(filename, validSwitches=None, validPorts=None, validMacs=None):
    with open(filename) as f:
        for line in f:
            if line != "\n":
                line = line[0:len(line)-1]
                validateLine(line, validSwitches, validPorts, validMacs)
            global line_number
            line_number = line_number + 1


def validateLine(line, validSwitches=None, validPorts=None, validMacs=None):
    vals = line.split(' ')
    if len(vals) != 3:
        print "Invalid Output[L" + str(line_number) + "]: log entry should have three values but " + len(vals) + " are given."
        return
    switch = int(vals[0])
    port = int(vals[1])
    mac = str(vals[2])

    if (validSwitches != None) and not (switch in validSwitches):
        print "Invalid Output[L" + str(line_number) + "]: switches in this problem are numbered (" + str(validSwitches) + ") but " + switch + " is given."
    if (validPorts != None) and not (port in validPorts):
        print "Invalid Output[L" + str(line_number) + "]: switches in this problem have ports (" + str(validPorts) + ") but " + port + " is given."
    if (validMacs != None) and not (mac in validMacs):
        print "Invalid Output[L" + str(line_number) + "]: hosts in this problem have mac addresses (" + str(validMacs) + ") but " + mac + " is given."

def iterationCheck(filename):
    totalSteps=0
    with open(filename) as f:
        for line in f:
            if line == "\n":
                totalSteps += 1

    if totalSteps < 1:
        print("Invalid Output: Missing next_entry() in " + filename)


if len(sys.argv) != 3 or not (sys.argv[2] in ['static-forwarding', 'learning-switch']):
    print "Syntax:"
    print "    python "+sys.argv[0]+" <log_file> <mode>"
    print "    <mode>: one of {static-forwarding, learning-switch}"
    exit()

print "Output validation initiated on " + sys.argv[1] + " (" + sys.argv[2] + "):"

if sys.argv[2] == 'static-forwarding':
    validateStudentOutput(sys.argv[1],
                          validSwitches=[1, 2],
                          validPorts=[1, 2, 3],
                          validMacs=['00:00:00:00:00:01','00:00:00:00:00:02','00:00:00:00:00:03','00:00:00:00:00:04'])
else:
    iterationCheck(sys.argv[1])
    validateStudentOutput(sys.argv[1])
print "Output validation complete."

