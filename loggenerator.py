import time
import random
import faker
from datetime import datetime
from datetime import date
import random
from random import randint, choice
import sys
import time
import faker
from datetime import datetime
import os


fak = faker.Faker("tr_TR")
os.environ["TZ"] = "Europe/Istanbul"


def str_time_prop(start, end, format, prop):
    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))
    ptime = stime + prop * (etime - stime)
    return time.strftime(format, time.localtime(ptime))


def random_date(start, end):
    return str_time_prop(start, end, "%d/%b/%Y:%I:%M:%S %z", random.random())


dictionary = {
    "request": ["GET", "POST", "PUT", "DELETE"],
    "endpoint": [
        "/usr",
        "/usr/admin",
        "/usr/admin/developer",
        "/usr/login",
        "/usr/register",
    ],
    "statuscode": ["303", "404", "500", "403", "502", "304", "200"],
    "ua": [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36",
        # Diğer User-Agent'lar
    ],
    "referrer": ["-", "https://www.secrcomp.com/"],
}

statuscode_weights = [0.7, 0.1, 0.1, 0.05, 0.02, 0.02, 0.01]

with open("secrcomp.log", "w") as f:
    for _ in range(1, 50001):
        f.write(
            '{} - - [{}] "{} {} HTTP/1.0" {} {} "{}" "{}" {}\n'.format(
                fak.ipv4(),
                random_date("01/Jan/2023:12:00:00 +0300", "01/Jan/2024:12:00:00 +0300"),
                choice(dictionary["request"]),
                choice(dictionary["endpoint"]),
                random.choices(
                    dictionary["statuscode"], weights=statuscode_weights, k=1
                )[0],
                max(0, int(random.gauss(5000, 50))),
                choice(dictionary["referrer"]),
                choice(dictionary["ua"]),
                random.randint(1, 5000),
            )
        )
