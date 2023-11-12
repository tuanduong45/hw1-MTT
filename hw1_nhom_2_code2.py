import random

# Initialize the simulation parameters
num_input_ports = 128
num_output_ports =128
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

def get_pop_list(num_input_ports, input_queues, output_queues):
    # print(input_queues)
    for port in range(num_input_ports):
        if input_queues[port]:
            input_port = input_queues[port][0]
            output_queues[input_port].append(port)
    # print(output_queues)
    random_pop_list = []
    for output_port in output_queues:
        if output_port:
            random_pop_list.append(random.choice(output_port))
    for output_port in output_queues:
        output_port.clear()
    # print(random_pop_list)
    # print("----------------------------------------------------------------------------")
    return random_pop_list



# Start the simulation
for time_slot in range(num_time_slots):
    random_pop_list = get_pop_list(num_input_ports, input_queues, output_queues)
    for index in random_pop_list:
        if input_queues[index]:
            input_queues[index].pop(0)

    # reset random pop list
    random_pop_list = []


number_of_packkets_not_forwarded = 0

for i in input_queues:
    #print(i)
    number_of_packkets_not_forwarded = len(i) + number_of_packkets_not_forwarded


print(100 - (number_of_packkets_not_forwarded / (num_input_ports*num_packets_per_input)*100))