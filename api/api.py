from flask import Flask, jsonify, request

import sys
import os
# Tell syspath where to import modules from other folders in root direcotry
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from model.issCrewModel import issCrew


# Initialize Flask application
app= Flask(__name__)
app.config["DEBUG"] = True

def __init__(self):
    self

@app.route('/', methods=['GET'])
def home():
    """ Tets method to check api """
    return jsonify('Hellow world!')

@app.route("/iss-crew-bio", methods=["GET"])
def issCrewBio():
    """ Get iss crew members with their bio """
    crewBio = issCrew()
    issBio = crewBio.matchCrewWithAstros()  
    return jsonify('Current ISS crew: ', issBio)

app.run()