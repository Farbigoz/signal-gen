import os
import sys
import importlib

from ui.BaseGenerator import BaseGenerator, GENERATOR_LIST

# Автоматический импорт всех генераторов

generatorsPath = os.path.join(os.path.split(__file__)[0], "generators")

sys.path.append(generatorsPath)

for generatorFile in os.listdir(generatorsPath):
    if generatorFile == "__init__.py": continue

    if os.path.isfile(os.path.join(generatorsPath, generatorFile)):
        generatorModule = importlib.import_module(os.path.splitext(generatorFile)[0])

        for objName in dir(generatorModule):
            obj = getattr(generatorModule, objName)
            if hasattr(obj, "__bases__"):
                if BaseGenerator in obj.__bases__:
                    GENERATOR_LIST.append(obj)


