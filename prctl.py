#!/usr/bin/env python

import argparse
from tasks import collect_instances

parser = argparse.ArgumentParser(description='packrat control utility for scheduling collections')
parser.add_argument('--collect', '-c', action='store', dest='name_to_collect', help='schedule a collection')
parser.add_argument('--list', '-l', action='store_true', dest='list_collections', help='list schedulable collections')

args = parser.parse_args()

if __name__ == "__main__":
    if args.name_to_collect == "instances":
        collect_instances()
    elif args.list_collections:
        print "listing collections"
    else:
        print parser.print_help()
