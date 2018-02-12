# dsl1.py

import sys
import importlib

# The source file is the first argument to the script
if len(sys.argv) != 2:
	print('usage: %s <src.dsl>' % sys.argv[0])
	sys.exit(1)

sys.path.insert(0, '/Users/jeje/Documents/dsl-python/modules')
with open(sys.argv[1], 'r') as file:
	for line in file:
		line = line.strip()
		if not line or line[0] == '#':
			continue
		parts = line.split()
		print(parts)

		mod = importlib.import_module(parts[0])
		print(mod)
		getattr(mod, parts[1])(parts[2], parts[3])