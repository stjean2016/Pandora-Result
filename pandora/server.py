# -*- coding: utf-8 -*-
import __init__
import json
from flask import Flask



app = __init__.create_app()
app.run(debug=True)


