import pyalps

fileheader = 'heisenberg'
data = pyalps.loadEigenstateMeasurements(pyalps.getResultFiles(prefix=fileheader),'Energy')

#print data,len(data)

J_En = pyalps.collectXY(data, x='J', y='Energy')
print data 

for x, y in zip(J_En[0].x, J_En[0].y):
    print x, y 
