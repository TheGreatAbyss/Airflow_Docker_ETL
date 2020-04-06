import argparse
import datetime
import sys

from importlib import import_module


"""
Main entry point for all jobs
example usage:  python ./etl_src/entry_point.py --job_and_func=ETLs.IEEE.transactions_etl.transactions_etl --start_date=2017-04-25 --end_date=2017-05-15
example usage:  python ./etl_src/entry_point.py --job_and_func=ETLs.IEEE.identities_etl.identities_etl --start_date=2017-04-25 --end_date=2017-05-15
"""
parser = argparse.ArgumentParser()
parser.add_argument('-p', '--job_and_func', required=True)
parser.add_argument('-s', '--start_date', required=False)
parser.add_argument('-e', '--end_date', required=False)
args = parser.parse_args()
print(args)

if args.start_date:
    start_date = datetime.datetime.strptime(args.start_date, "%Y-%m-%d")
else:
    start_date = None

if args.end_date:
    end_date = datetime.datetime.strptime(args.end_date, "%Y-%m-%d")
else:
    end_date = None

mod_name, func_name = args.job_and_func.rsplit('.', 1)

try:
    job_module = import_module(mod_name)
    job_func = getattr(job_module, func_name)
except (ImportError, ValueError) as e:
    print("Unable to run job: {0}".format(e), sys.stderr)
    sys.exit(1)
except AttributeError as e:
    print("Invalid module or function name: {0}".format(e), sys.stderr)
    print("Double-check the package and module path to the function.", sys.stderr)
    sys.exit(1)

job_func(start_date, end_date)