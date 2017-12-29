import random
import string
from random import randrange
import datetime

startDate = datetime.datetime(2013, 9, 20,13,00,00)
randTimestamp = startDate + datetime.timedelta(minutes=randrange(60))
print(randTimestamp)

randId = (''.join(random.choices(string.ascii_letters + string.digits, k=4)))
print(randId)