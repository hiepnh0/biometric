#!/usr/bin/python

import sys
import os
import csv
from os import listdir
from os.path import isfile, join
from shutil import copyfile

dictSearch = {
 				"E1": "Error",
 				"E2": "error",
 				"F1": "<Error>: getEnabledForUnlock",
 				"F2": "<Error>: getSKSLockState:forUser",
 				"F3": "<Error>: getBioLockoutState:forUser:withClient",
 				"F4": "<Error>: startDetectFingerWithOptions:withClient:",
 				"F5": "<Error>: startBioOperation",
 				"F6": "<Error>: detectFingerWithOptions:withClient",
 				"F7": "<Error>: processBioOperation:withPriority:withParams:withClient",
 				"F8": "ERROR: AppleBiometricSEP::sepMessageHandler",

 				"P1": "<Notice>: statusMessage:withData:timestamp:",
 				"P2": "<Notice>: sending status message",
 				"P3": "<Notice>: BKOperation::statusMessage",
 				"P4": "<Notice>: BKDevice::bioLockoutState:forUser",

				"I1": "<Error>: forceBioLockoutForUser:withClient",
    			"I2": "<Error>: BKDevicePearl::deviceAvailable -> 0 (null)",
    			"I3": "<Error>: AssertMacros",
			    "I4": "<Error>: BKDevice::deviceWithDescriptor"
			}

arrFaileds = [
 				"F1",
 				"F2",
 				"F3",
 				"F4",
 				"F5",
 				"F6",
 				"F7",
 				"F8"
			]

arrPassed = [
 				"P1",
 				"P2",
 				"P3",
 				"P4"
			]

arrIrgnore = [
				"<Error>: forceBioLockoutForUser:withClient",
    			"<Error>: BKDevicePearl::deviceAvailable -> 0 (null)",
    			"<Error>: AssertMacros",
			    "<Error>: BKDevice::deviceWithDescriptor"
			]
arrError = [
				"E1",
 				"E2"
			]
def MY_CONSTANT():
	dictTmp = {
 				"E1": "",
 				"E2": "",
 				"F1": "",
 				"F2": "",
 				"F3": "",
 				"F4": "",
 				"F5": "",
 				"F6": "",
 				"F7": "",
 				"F8": "",

 				"P1": "",
 				"P2": "",
 				"P3": "",
 				"P4": "",

				"I1": "",
				"I2": "",
				"I3": "",
				"I4": "",

				"result": "",
				"DeviceSerial": "",
			}
	return dictTmp

resArr = []

args = sys.argv

mypath = args[1]
if mypath == "":
	mypath = os.getcwd()
searchfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

try: 
    os.makedirs("blank")
except OSError:
    if not os.path.isdir("blank"):
        raise

try: 
    os.makedirs("passed")
except OSError:
    if not os.path.isdir("passed"):
        raise

try: 
    os.makedirs("failed")
except OSError:
    if not os.path.isdir("failed"):
        raise

for x in searchfiles:
	if (x != "search.py" and x != "tid_output.csv"):
		dictRec = MY_CONSTANT()
		dictRec.update({"DeviceSerial": x[4:-4]})

		fileName = mypath+"/"+x
		file1 = open(fileName, 'r')
		for line in file1:
			for item in dictSearch:
				if dictSearch[item] in line:
					dictRec.update({item: "x"})
					if "F" in item:
						dictRec.update({"result": "failed"})
					if "E" in item:
						for igr in arrIrgnore:
							if igr in line:
								dictRec.update({item: ""})
		if dictRec["result"] == "":
			for itemP in arrPassed:
				if dictRec[itemP] == "x":
					for err in arrError:
						if dictRec[err] == "": 
							dictRec.update({"result": "passed"})
						else:
							dictRec.update({"result": ""})

		if dictRec["result"] == "":
			copyfile(fileName, "blank/" + dictRec["DeviceSerial"] + ".txt")
		if dictRec["result"] == "passed":
			copyfile(fileName, "passed/" + dictRec["DeviceSerial"] + ".txt")
		if dictRec["result"] == "failed":
			copyfile(fileName, "failed/" + dictRec["DeviceSerial"] + ".txt")
		resArr.append(dictRec)
		file1.close()
keys = sorted(resArr[0].keys())
f = open("tid_output.csv", "w")
writer = csv.DictWriter(
    f, keys)
writer.writeheader()
writer.writerows(resArr)
f.close()
		











