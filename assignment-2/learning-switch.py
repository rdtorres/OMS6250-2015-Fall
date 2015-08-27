#!/usr/bin/python

"Assignment 4 - This is the controller code that students will have to \
    implement sections of. It is Pyretic based, but this is somewhat\
    unimportant at the moment, as we only care about the learning\
    behaviors."

from pyretic.lib.corelib import *
from pyretic.lib.std import *
from pyretic.lib.query import packets
from helpers import *


class LearningSwitch(DynamicPolicy):
    def __init__(self):
        """ Initialization of the Learning Switch. The important piece
            is the definition of the switch mapping. This is a nested
            dictionary. """

        # Initialize the parent class
        super(LearningSwitch, self).__init__()

        # Initialize logfile
        init_log("learning-switch.log")
        
        # TODO: Initialize your forwarding tables. Create this however you wish.
        # Couple of suggestions: Dictionary of dictionaries, Dictionary of 
        # tuples. 


        # only use one flood instance - this is the default policy when there 
        # isn't a known path.
        self.flood = flood()

        # Get the first packet from each new MAC address on a switch. This
        # is how we are able to learn new routes.
        new_pkts = packets(1, ['srcmac', 'switch'])
        new_pkts.register_callback(self.learn_route)
        self.query = new_pkts

        # Initialize the policy
        self.build_policy() 


    def print_switch_tables(self):
        # TODO - This is different than how logging in static-switch.py works.
        # Here, you have to do a bit more. First, you need to print out each 
        # entry in the forwarding tables, as was done in static-switch.py.
        # Finally (which is already done for you), next_entry() needs to be
        # called, creating a break between each set of forwarding tables.
        # next_entry() need only be called at the very end - not after each
        # entry.
        
        
        # After looping through the forwarding table(s), finish up with a break
        # in the log file.
        next_entry()

    def learn_route(self, pkt):
        """  This function adds new routes into the fowarding table. """

        # TODO - create a new entry in the fowarding table. Use the functions 
        # in the second half of helpers to simplify all your work.
        

        # print out the switch tables:
        self.print_switch_tables()

        # Call build_policy to update the fowarding tables of the switches.
        self.build_policy()
        pass




    def build_policy(self):
        """ 
        This is similar to the build_policy() function in StaticSwitch. 
        There is a major difference: If there isn't a rule, you need to flood
        the packets. The example code should help.
        """
        new_policy = None
        not_flood_pkts = None
        

        # TODO: Example code. You will need to edit this based on how you're 
        # storing your policies. You should only have to replace the details in
        # rule entries.
        rule1 = 1, "00:00:00:00:00:01", 3
        rule2 = 1, "00:00:00:00:00:02", 2
        for rule in (rule1, rule2):
            if new_policy == None:
                # First entry, prime the pump
                new_policy = (match(switch=int(rule[0]), dstmac=(rule[1])) >>
                              fwd(rule[2]))
            else:
                new_policy += (match(switch=int(rule[0]), dstmac=(rule[1])) >>
                               fwd(rule[2]))
            if not_flood_pkts == None:
                not_flood_pkts = (match(switch=int(rule[0]), dstmac=(rule[1])))
            else:
                not_flood_pkts |= (match(switch=int(rule[0]), dstmac=(rule[1])))
                        
                

        # If you follow the pattern above, you won't have to change this below. 
        # We don't know of any rules yet, so flood everything.
        if not_flood_pkts == None:
            self.policy = self.flood + self.query
        else:
            self.policy = if_(not_flood_pkts, new_policy, self.flood) + self.query
        
        # The following line can be uncommented to see your policy being
        # built up, say during a flood period. 
        # print self.policy


def main():
    return LearningSwitch()
