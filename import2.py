import pip
import importlib
import pkg_resources
def install_and_import(package):
    
    try:
       importlib.import_module(package)
    except ImportError:
        pip.main(['install', package])
    #finally:
       # globals()[package] = importlib.import_module(package)
installed = [pkg.key for pkg in pkg_resources.working_set]
builtin_modules = sys.modules
with open('app.py') as f:
    for lines in f:
        if "import" in lines:
            tmp = lines.split("import")
            pack=tmp[-1].strip()
            if pack not in built_in_mod and pack.lower() not in installed:
                install_and_import(pack)  
            else:
                print("installed lib")
