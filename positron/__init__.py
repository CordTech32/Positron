

import json
import os
import shutil
import sys
from typing import Union
from .gui import Chromium
from .converter import Flask

class AltJSON:
    def __init__(self, **kwds):
        for k in kwds.keys():
            self.__setattr__(k, kwds[k])

    def as_json(self):
        return vars(self)

def create_debug_app(config: Union[dict, AltJSON]):
    if isinstance(config, AltJSON):
        config = config.as_json()
    f = Flask(config)
    f.run_server()
    c = Chromium(f)
    c.run()

def freeze(input_file, output, config:dict):
    print("Freezing your app...")
    print("Creating App Container...")
    f = Flask(config)
    shutil.copytree(os.path.dirname(os.path.abspath(__name__+".py")), output)
    print("Collecting Positron Distutils...")
    if sys.platform != "win32":
        os.system("python3 -m pip install git+https://cordtech32/positron --target=floss_modules")
    else:
        os.system("pip install git+https://github.com/cordtech32/positron --target=posi_modules")
    print("Reading Metadata...")
    with open("package.json") as js:
        pack = json.load(js)

    with open(input_file) as f:
        app = f.read()
    
    print("Creating Project...")
    
    with open(output+f"/{pack['entrypoint']}.py","w") as f:
        f.write(app)

    if sys.platform != "win32":
        with open(output+"/positron.sh", "w") as f:
            f.write(f"""
            #!/bin/bash
            python3 positron.py
            """)

        with open(output+"/positron.py","w") as f:
            f.write(f"""
from {pack['entrypoint']} import app
from posi_modules.positron import create_debug_app, AltJSON

struct = AltJSON(flask_app=app, flask_address="{pack['flask_host']}", name="{pack['name']}")

create_debug_app(struct)
            """)
    else:
        with open(output+"/positron.cmd", "w") as f:
            f.write(f"""
            py positron.py
            """)


        with open(output+"/positron.py","w") as f:
            f.write(f"""
from {pack['entrypoint']} import app
from posi_modules.positron import create_debug_app, AltJSON

struct = AltJSON(flask_app=app, flask_address="{pack['flask_host']}", name="{pack['name']}")

create_debug_app(struct)
            """)

    print("Positron Distributable is now created!")
    print("Happy Hacking :)")

    