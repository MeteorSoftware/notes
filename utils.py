from flask import Flask,jsonify,make_response,request

def success(res):
    return make_response(res, 200)

def fail400(res):
    return make_response(res, 400)