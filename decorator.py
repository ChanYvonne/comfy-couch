import time

def getInfo(func):
    def innerFunc(param):
        print func.__name__ + ": " + "(" + str(param) + ")" + "\n"
        return func(param)

    return innerFunc

def getTime( func ):
    def innerFunc(param):
        startTime = time.time()
        result = func(param)
        endTime = time.time()
        
        print "Execution Time: " + str(endTime - startTime) + " s\n"
        return result
        
    return innerFunc

def fibonacci(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return F(n-1)+F(n-2)

def testFunc(x):
    time.sleep(1)
    return 5 * x

timetest = getTime( testFunc )
#print timetest(5)

infograb = getInfo(testFunc)
#print infograb(4)

informationaoinwdoiwan = getTime(fibonacci)
informationaoinwdoiwan(700)
