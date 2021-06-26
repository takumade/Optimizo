"""Optimize Grapper"""
import argparse

import os
import sys

# Create the parser
my_parser = argparse.ArgumentParser(prog="optimizo", 
                                    description='Optimize Laravel project and push it to Github',
                                    epilog='Happy Optimizing!')

# Add the arguments
my_parser.add_argument('Project',
                       metavar='project_type',
                       type=str,
                       help='type of project e.g larave, rn, flutter')


my_parser.add_argument('-t',
                       '--html',
                       action='store_true',
                       help='Optimize HTML')

my_parser.add_argument('-c',
                       '--css',
                       action='store_true',
                       help='Optimize CSS')

my_parser.add_argument('-j',
                       '--js',
                       action='store_true',
                       help='Optimize JS')

my_parser.add_argument('-s',
                       '--shared-hosting',
                       action='store_true',
                       help='Modifies laravel so its shared hosting ready. Works only with Laravel')

my_parser.add_argument('-g',
                       '--github',
                       action='store_true',
                       help='Push project to github.')

my_parser.add_argument('-u',
                       '--unoptimize',
                       action='store_true',
                       help='Unoptimize project back to the way it was.')


# Execute the parse_args() method
args = my_parser.parse_args()

print(args.js)

