import time

def getTime( func ):
    startTime = time.time()
    def innerFunc(param):
        func(param)
    endTime = time.time()
    return endTime - startTime

def testFunc(x):
    print "testerinoing"
    time.sleep(5000)
    return 5 * x

timetest =  getTime( testFunc )
print timetest(5)
    
