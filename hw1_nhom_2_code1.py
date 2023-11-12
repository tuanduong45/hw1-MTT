import random

# Initialize the simulation parameters
num_input_ports = 64
num_output_ports = 64
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
            #print(input_queues[input_port])
            if input_queues[input_port][0] not in l_empty:
                # theo thu tu
                packet_destination = input_queues[input_port].pop(0)
            l_empty.append(packet_destination)
            #print(packet_destination)
            #print("----")
    #print(l_empty)
    l_empty = []

number_of_packkets_not_forwarded = 0

for i in input_queues:
    #print(i)
    number_of_packkets_not_forwarded = len(i) + number_of_packkets_not_forwarded


print(100 - (number_of_packkets_not_forwarded / (num_input_ports*num_packets_per_input)*100))