from matplotlib import pyplot

fabricSize = [1, 2, 4, 8, 16, 32, 64]
throughput = [100, 75.65, 65.475, 62.2645, 59.975, 59.3781, 59.0171]
pyplot.plot(fabricSize, throughput, marker=".", markersize=12)
pyplot.xlabel("Fabric Size")
pyplot.ylabel("Throughput")
pyplot.show()
