from logging import basicConfig, DEBUG
from easysnmp import Session

basicConfig(level=DEBUG)

s = Session(hostname="192.168.1.173:1161", version=2, use_modules=True)

for var in s.bulkwalk(oids="1.3"):
    print(var)
