import sys
import os

path = os.path.abspath('..')
sys.path.append(path)
import FDgen

print(FDgen.create_person())
print(FDgen.get_name())
print(FDgen.get_last_name())
print(FDgen.get_location())
print(FDgen.get_address())
print(FDgen.get_mail("arzybek", "kazikulov"))
print(FDgen.get_number("+228"))
