import pip
from pip._internal import main
def install_and_import(package):
    #import importlib
    #try:
       #importlib.import_module(package)
   #except ImportError:
        main(['install', package])
    #finally:
       # globals()[package] = importlib.import_module(package)


with open('app.py') as f:
    for lines in f:
        if "import" in lines:
            tmp = lines.split("import")
            pack=tmp[-1].strip()
            install_and_import(pack)  
