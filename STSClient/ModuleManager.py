#!/usr/bin/env python3

# License: AGPL 3
# Author: Lorenzo Santina (BigNerd95)

import libs.Structures
import pkgutil
import importlib

def listModules(package):
	modules = []
	for importer, modname, ispkg in pkgutil.iter_modules(package.__path__):
		modules.append(modname)
		#print("Found submodule " + modname)
	return modules

def importModuleFromPackage(package, moduleName):
	return importlib.import_module(package.__name__ + '.' + moduleName)

def listStructures():
    return listModules(libs.Structures)

def importStructure(name):
    return importModuleFromPackage(libs.Structures, name)

##################################################################

def parse_cli():
    parser = ArgumentParser(description='** Module Tester **')
    subparser = parser.add_subparsers(dest='subparser_name')

    listParser = subparser.add_parser('list', help='List available module')

    testParser = subparser.add_parser('test', help='Test a module')
    testParser.add_argument('-m', '--module', required=True, help='Module name')
    testParser.add_argument('-f', '--file_path', required=True, help='File(s) path')
    testParser.add_argument('-v', '--verbose', action='store_true', help='Show all parsed receipts')

    args = parser.parse_args()
    if args.subparser_name:
        return args
    else:
        parser.print_help()
        return None

# main for testing purpose.
# You can write your own Structure module inside libs/Structures
# and test it with this program.
if __name__ == '__main__':
    from argparse import ArgumentParser

    args = parse_cli()
    if args:
        if args.subparser_name == 'list':
            for s in listStructures():
                print(s)

        elif args.subparser_name == 'test':
            module = importStructure(args.module)
            receipts = module.parse(args.path)
            print('Count: ' + str(len(receipts)))
            if args.verbose:
                for r in receipts:
                    print(r)
