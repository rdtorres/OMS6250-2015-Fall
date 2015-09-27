# Assignment 3 for OMS6250
#
# This defines a DistanceVector Node that can fun the Bellman-Ford
# algorithm. The TODOs are all related to implementing BF. Students should
# modify this file as necessary, guided by the TODO comments and the
# assignment instructions. This is the only file that needs to be modified
# to complete the project.
#
# Copyright 2015 Dave Lillethun & Sean Donovan

from Node import *
from helpers import *

class DistanceVector(Node):
    #TODO: You need to have a structure that contains current distances

    def __init__(self, name, topolink, neighbors):
        super(DistanceVector, self).__init__(name, topolink, neighbors)
        #TODO: You may need to initialize your distance data structure


    #TODO: You may want to override __str__ to print your distance info.
    #def __str__(self):
    #    ''' Returns a string representation of the node. '''

    def send_initial_messages(self):
        for neighbor in self.links:
            # TODO - Build message
            msg = None

            # Send message to neighbor
            self.send_msg(msg, neighbor)


    def process_BF(self):
        # TODO: The Bellman-Ford algorithm needs to be implemented here.
        # 1. Process queued messages
        # 2. Send neighbors updated distances

        # Process queue:
        for msg in self.messages:
            # TODO: Do something
            pass
        # Empty queue
        self.messages = []

        # Send neighbors udpated distances:
        pass


    def log_distances(self):
        ''' Prints distances in the following format (no whitespace either end):
        A:A0,B1,C2
        A is the node were on,
        B is the neighbor, 1 is it's distance
        A0 shows that the distance to self is 0
        Taken from topo1.py
        '''
        # TODO: The string in the format above (no newlines, no whitepsace) must
        # be defined. THen log with write_entry, example below. You'll need to 
        # make a loop over all the switches and call add_entry() (see helpers.py)
        # for each switch.
        switch = "A"
        logstring = "A0,B1,C2"
        add_entry(switch, logstring)
        pass