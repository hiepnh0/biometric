#!/usr/bin/python

import sys
import os
import csv
from os import listdir
from os.path import isfile, join

dictSearch = {
 				"Failed_sign_1": "<Error>: getEnabledForUnlock",
 				"Failed_sign_2": "<Error>: getSKSLockState:forUser",
 				"Failed_sign_3": "<Error>: getBioLockoutState:forUser:withClient",
 				"Failed_sign_4": "<Error>: startDetectFingerWithOptions:withClient:",
 				"Failed_sign_5": "<Error>: startBioOperation",
 				"Failed_sign_6": "<Error>: detectFingerWithOptions:withClient",
 				"Failed_sign_7": "<Error>: processBioOperation:withPriority:withParams:withClient",
 				"Failed_sign_8": "ERROR: AppleBiometricSEP::sepMessageHandler",

 				"Passed_sign_1": "<Notice>: statusMessage:withData:timestamp:",
 				"Passed_sign_2": "<Notice>: sending status message"
				"Passed_sign_ignore_1": "<Error>: forceBioLockoutForUser:withClien"
				"Passed_sign_ignore_2": "<Notice>: sending status message"
			}
def MY_CONSTANT():
	dictTmp = {
 				"Failed_sign_1": "",
 				"Failed_sign_2": "",
 				"Failed_sign_3": "",
 				"Failed_sign_4": "",
 				"Failed_sign_5": "",
 				"Failed_sign_6": "",
 				"Failed_sign_7": "",
 				"Failed_sign_8": "",

 				"Passed_sign_1": "",
 				"Passed_sign_2": "",
				"Passed_sign_ignore_1": "",
				"Passed_sign_ignore_2": "",
				"DeviceSerial": ""
			}
	return dictTmp

resArr = []

args = sys.argv

mypath = args[1]
if mypath == "":
	mypath = os.getcwd()
searchfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for x in searchfiles:
	if x != "search.py":
		dictRec = MY_CONSTANT()
		dictRec.update({"DeviceSerial": x})

		fileName = mypath+"/"+x
		file1 = open(fileName, 'r')
		for line in file1:
			for item in dictSearch:
				if dictSearch[item] in line:
					dictRec.update({item: "x"})
		resArr.append(dictRec)
		file1.close()

keys = sorted(resArr[0].keys())
f = open("tid_output.csv", "w")
writer = csv.DictWriter(
    f, keys)
writer.writeheader()
writer.writerows(resArr)
f.close()

