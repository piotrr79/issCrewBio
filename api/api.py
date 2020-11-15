from flask import Flask, jsonify, request

import sys
import os
# Tell syspath where to import modules from other folders in root direcotry
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from model.issCrewModel import issCrew


# initialize our Flask application
app= Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return jsonify('Hellow world!')

@app.route("/iss-crew-bio", methods=["GET"])
def issCrewBio():
    issBio = issCrew.matchCrewWithAstros()
    
    print(issBio)
    
    return jsonify(issBio)

#x = issCrew()
#match = x.matchCrewWithAstros()
#print(match)

app.run()