import sys
import datetime
import pip
import pkg_resources
built_in_mod = sys.modules
#print(built_in_mod.keys())
'''if "sys" in built_in_mod:
    print("true")'''
#a=[datetime]
#res=set(a)-set(built_in_mod)
#print(list(res))
#print(built_in_mod)
pkgs = []
pkgs1=[]
#print([pip.main(['list'])])
installed = [pkg.key for pkg in pkg_resources.working_set]
#print(installed)
with open('app.py') as f:
    for lines in f:
        if "import" in lines:
            tmp = lines.split("import")
            #print(tmp[-1])
            if tmp[-1].strip() not in built_in_mod and tmp[-1].strip() not in installed:
            #if tmp[-1].strip() not in built_in_mod:
                    pkgs.append((tmp[-1].strip()))
#print(pkgs)
#pkgs = set(pkgs)-set(installed)
#print(list(pkgs))
for package in pkgs:
    if package in installed or package.lower() in installed:
            pkgs.remove(package)
            print(pkgs)
pip.main(['install'] + pkgs)
