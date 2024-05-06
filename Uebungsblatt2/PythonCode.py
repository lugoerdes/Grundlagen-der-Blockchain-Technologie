import hashlib
import time
startTime = time.time()
puzzleID = 'BBSE_E01'
d = '0000'
iteration = 0

while(True):
    hash=puzzleID+str(iteration)
    hash=hash.encode()
    hash=hashlib.sha256(hash).hexdigest()
    if (hash[:4]==d):
        break
    iteration+=1
print('Iterationen: '+str(iteration)+' Hash: ' +str(hash)+' Time: '+ str(time.time()-startTime))