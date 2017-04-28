import time

def getInfo(func):
    def innerFunc(param):
        print func.__name__ + ": " + "(" + str(param) + ")" + "\n"
        if param == 0: return 0
        elif param == 1: return 1
        else: return innerFunc(param-1)+innerFunc(param-2)
    return innerFunc

def getTime( func ):
    def innerFunc(param):
        startTime = time.time()
        result = func(param)
        endTime = time.time()
        
        print "Execution Time: " + str(endTime - startTime) + " s\n"
        return result
        
    return innerFunc

def fibonacci(param):
    if param == 0: return 0
    elif param == 1: return 1
    else: return fibonacci(param-1)+fibonacci(param-2)

def testFunc(x):
    time.sleep(1)
    return 5 * x

timetest = getTime( testFunc )
#print timetest(5)

infograb = getInfo(testFunc)
#print infograb(4)

timeee= getTime(fibonacci)
print timeee(30)

inform = getInfo(fibonacci)
inform(30)
