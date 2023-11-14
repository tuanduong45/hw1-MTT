import random
from matplotlib import pyplot


def calculate_hol_throughput(fabric_size):
    # Initialize the simulation parameters
    num_input_ports = fabric_size
    num_output_ports = fabric_size
    num_packets_per_input = 1000
    num_time_slots = 1000

    # Create a list of input queues
    input_queues = []
    for i in range(num_input_ports):
        input_queues.append([])

    # Create a list of output queues
    output_queues = []
    for i in range(num_output_ports):
        output_queues.append([])

    # Fill the input queues with packets
    for i in range(num_input_ports):
        for j in range(num_packets_per_input):
            input_queues[i].append(random.randint(0, num_output_ports - 1))

    l_empty = []
    # Start the simulation
    for time_slot in range(num_time_slots):
        # For each input port, try to forward a packet
        for input_port in range(num_input_ports):
            if len(input_queues[input_port]) > 0:
                # print(input_queues[input_port])
                if input_queues[input_port][0] not in l_empty:
                    # theo thu tu
                    packet_destination = input_queues[input_port].pop(0)
                l_empty.append(packet_destination)
                # print(packet_destination)
                # print("----")
        # print(l_empty)
        l_empty = []

    number_of_packkets_not_forwarded = 0

    for i in input_queues:
        # print(i)
        number_of_packkets_not_forwarded = len(i) + number_of_packkets_not_forwarded

    # Caculate throughput
    thoughput = 100 - (
        number_of_packkets_not_forwarded
        / (num_input_ports * num_packets_per_input)
        * 100
    )
    return thoughput

# Plot a line chart throughput varying by fabric_sizes
def plot_chart_througput_fs(fabric_sizes, throughputs):
    fig = pyplot.gcf()
    fig.canvas.set_window_title("HW1 - Nhom 2")
    pyplot.plot(fabric_sizes, throughputs, marker=".", markersize=12)
    pyplot.title("HOL Blocking Throughput Chart")
    pyplot.xlabel("Fabric Size")
    pyplot.ylabel("Throughput")
    for idx, value in zip(fabric_sizes, throughputs):
        pyplot.text(idx + 5, value + 1.5, f"{str(round(value, 4))}%", ha = "center")
    pyplot.show()

# main prog
if __name__ == "__main__":
    fabric_sizes = [1, 2, 4, 8, 16, 32, 64]
    num_loops = input("Enter number of loops for calculating: ")
    for i in range(int(num_loops)):
        fabric_size_throughput = []
        for fs in fabric_sizes:
            fabric_size_throughput.append(calculate_hol_throughput(fs)) 
        print(fabric_size_throughput)
        plot_chart_througput_fs(fabric_sizes, fabric_size_throughput)
