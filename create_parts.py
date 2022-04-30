TABLE = "parts"
PASS = "123"
USER = "postgres"
from secrets import choice
import string

for i in range(100):
    s = '-'.join([''.join([choice(string.ascii_uppercase + string.digits) for _ in range(3)]) for _ in range(3)])
    print(s)