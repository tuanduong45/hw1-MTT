from matplotlib import pyplot 
fabricSize = [1,2,4,8,16,32,64]
throughput = [100,76.15, 66.375,62.55,60.025,59.6219,59.09375] 
pyplot.plot(fabricSize,throughput,marker='.',markersize = 12)
pyplot.xlabel("Fabric Size")
pyplot.ylabel("Throughput")
pyplot.show()