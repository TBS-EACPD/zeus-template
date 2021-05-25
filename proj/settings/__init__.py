import os
import sys

from decouple import config

if config("USE_DEV_SETTINGS", cast=bool):
    if "test" in sys.argv or any("pytest" in arg for arg in sys.argv):
        print("---- using test settings ----")
        from .test import *
    else:
        print("---- using development settings ----")
        from .dev import *

else:
    print("---- using production settings ----")
    from .prod import *

