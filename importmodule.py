import sys
import datetime
import pip
import pkg_resources
built_in_mod = sys.modules


pkgs = []
pkgs1=[]

installed = [pkg.key for pkg in pkg_resources.working_set]

with open('app.py') as f:
    for lines in f:
        if "import" in lines:
            tmp = lines.split("import")
           
            if tmp[-1].strip() not in built_in_mod and (tmp[-1].strip()).lower() not in installed:
                pkgs.append((tmp[-1].strip()))
if len(pkgs) is not 0:
    print(pkgs)
    pip.main(['install'] + pkgs)
    print("******************")
else:
    print("All the Packages are installed...You are Good to go...")

