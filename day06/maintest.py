import RPi.GPIO as GPIO
import time
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from flask import Flask, request, render_template

form_class = uic.loadUiType("./main01.ui") [0]

