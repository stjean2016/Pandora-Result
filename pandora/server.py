# -*- coding: utf-8 -*-
import __init__
import json
from flask import Flask

test_dict = {"b64_url":"img.txt"}

a = json.dumps(test_dict)
print (a,type(a))

#app = __init__.create_app()
#app.run(debug=True)


