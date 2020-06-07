#!/usr/bin/env python
# coding: utf8
#
#
'''
    This file is part of "2ME fan control".

    "2ME fan control" is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    "2ME fan control" is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Foobar.  If not, see <http://www.gnu.org/licenses/>.

    Diese Datei ist Teil von "2ME fan control".

    "2ME fan control" ist Freie Software: Sie können es unter den Bedingungen
    der GNU General Public License, wie von der Free Software Foundation,
    Version 3 der Lizenz oder (nach Ihrer Wahl) jeder neueren
    veröffentlichten Version, weiter verteilen und/oder modifizieren.

    Fubar wird in der Hoffnung, dass es nützlich sein wird, aber
    OHNE JEDE GEWÄHRLEISTUNG, bereitgestellt; sogar ohne die implizite
    Gewährleistung der MARKTFÄHIGKEIT oder EIGNUNG FÜR EINEN BESTIMMTEN ZWECK.
    Siehe die GNU General Public License für weitere Details.

    Sie sollten eine Kopie der GNU General Public License zusammen mit diesem
    Programm erhalten haben. Wenn nicht, siehe <https://www.gnu.org/licenses/>.
'''

import time
import RPi.GPIO as GPIO

fan_port = 25
cpu_max = 30

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(fan_port, GPIO.OUT)

def get_fan_status(fan_port):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(fan_port, GPIO.OUT)
    state = GPIO.input(fan_port)
    print(state)
    return state

def get_cpu_temp():
    tempFile = open("/sys/class/thermal/thermal_zone0/temp")
    cpu_temp = tempFile.read()
    return float(cpu_temp) / 1000

def fan_control():
    c = get_cpu_temp()
    s = "temperatur ist " + repr(c)
    print(s)
    fanState = get_fan_status(fan_port)
    if fanState == 1:
        print("fan is active")
    else:
        print("fan is off")

    if c > cpu_max:
        print("more than " + repr(cpu_max))
        GPIO.output(fan_port, GPIO.HIGH)
    elif c <= cpu_max:
        print("less than " + repr(cpu_max))
        GPIO.output(fan_port, GPIO.LOW)
        GPIO.cleanup()

while 1:
    fan_control()
    time.sleep(10)