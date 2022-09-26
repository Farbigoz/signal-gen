import os
import sys

generatorsPath = os.path.split(__file__)[0]

sys.path.append(generatorsPath)

for generator in os.listdir(generatorsPath):
    if os.path.isfile(os.path.join(generatorsPath, generator)):
        __import__(os.path.splitext(generator)[0])
