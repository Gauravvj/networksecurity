import os
import sys
import json
import certifi

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL=os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

ca=certifi.where()

import pandas as pd
import numpy as np
import pymongo
from networksecurity.exception import NetworkSecurityException

from networksecurity.logging import logging


