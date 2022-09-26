import os

# Фикс при использовании PySide2 designer
path = os.path.dirname(__file__)
for uiFileName in os.listdir(path):
    if not uiFileName.endswith(".py") or uiFileName == "__init__.py":
        continue

    uiPath = os.path.join(path, uiFileName)

    with open(uiPath, "r") as uiFile:
        uiContent = uiFile.read()

    uiContent = uiContent.replace("PySide2", "PyQt5")

    with open(uiPath, "w") as uiFile:
        uiFile.write(uiContent)
