#!/usr/bin/env python
import os
import sys

import dotenv

from django.core.management import execute_from_command_line

if __name__ == '__main__':
    # Use dotenv to load env variables from a .env file
    dotenv.load_dotenv('{}/.env'.format(Path(__file__).ancestor(1)))
    execute_from_command_line(sys.argv)
