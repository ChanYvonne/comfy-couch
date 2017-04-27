import time

def getTime( func ):
    def innerFunc(param):
        startTime = time.time()
        result = func(param)
        endTime = time.time()
        
        print "Time: " + str(endTime - startTime) + " s"
        return result
        
    return innerFunc

def testFunc(x):
    print "running test functIONE"
    time.sleep(1)
    return 5 * x

timetest = getTime( testFunc )
print timetest(5)
    
