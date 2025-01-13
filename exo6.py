import os
import sys

nbArgs = len(sys.argv)
prog = sys.argv[0]
params = sys.argv[1:]

if nbArgs == 1:
  print("No arguments provided")
  sys.exit(0)

path = params[0]

for path, dirs, files in os.walk(path):
  for filename in files:
    print(filename)