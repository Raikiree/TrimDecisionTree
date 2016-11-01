#################
#
# Tree Format Ex.: {A1:{B1:{},B2:{}}, A2:{C1:{},C2:{},C3:{}}, A3:{D1:{},D2:{}}}
# 'Tree' is Decision Tree!!!
#
#################

def isBottome(d):
	flag = True
	keys = d.keys()
	for key in keys:
		if type(d[key]) == dict:
			flag = False
			break
	return flag

def sameVals(d):
	flag = True 
	vals = d.values()
	v = list(d.values())[0]
	for val in vals:
		if val != v:
			flag = False
			break
	return flag


def run(d):
	if not isBottome(d):
		keys = d.keys()
		for key in keys:
			if type(d[key]) == dict:
				d[key] = simTree(d[key])

	if isBottome(d) and sameVals(d):
		return list(d.values())[0]
	else:
		return d

	