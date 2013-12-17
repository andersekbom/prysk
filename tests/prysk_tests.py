from nose.tools import *
import main

def setup():
    print "SETUP!"

map = Map() 


def teardown():
    print "TEAR DOWN!"

def test_basic():
    print "I RAN!"
