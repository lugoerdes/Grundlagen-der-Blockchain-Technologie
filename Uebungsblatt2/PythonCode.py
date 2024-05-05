import hashlib
puzzleID = 'BBSE_E01'
d = '0000'
x = 0

while(True):
    print(x)
    r=puzzleID+str(x)
    r=r.encode()
    r=hashlib.sha256(r).hexdigest()
    print(r)
    if (r[:4]==d):
        break
    x+=1
print('x: '+str(x)+' Hash: ' +str(r))