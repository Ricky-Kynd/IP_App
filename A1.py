from IP_address import IP_address
from Table import Table
from Histogram import Histogram

class A1:
    def __init__(self, filename):
        self.file_contents = read_file(filename)
        self.ip_unique_or_not = True
        self.ip_data_list = get_unique_ip_data_list(self.file_contents)
        self.size = max([i[1] for i in self.file_contents])
        self.IP_add = []
        self.store_ip_objects()

    def store_ip_objects(self):
        if self.ip_unique_or_not == True:
            for ip_key, data in self.ip_data_list.items():
                ip_add = IP_address(ip_key, data, self.size)
                self.IP_add.append(ip_add)

    def get_statistics(self):
        get_stats_list = [i.get_statistics() for i in sorted(self.IP_add)]
        return get_stats_list

    def get_freq_table(self, ip_address):
        ip = ip_address.rfind('.')
        ip_trunc = int(ip_address[ip + 1: ])

        freq_ip_list = [i[0] for i in self.file_contents]
        trunc_ip_list = [int(i[ip + 1: ]) for i in freq_ip_list]
        trunc_ip_list = [i for i in trunc_ip_list if i == ip_trunc]
        print([i.get_freq_list() for i in self.IP_add])

        # d = {}
        # count = 0
        # for i in range(len(trunc_ip_list)):
        #     if trunc_ip_list[i] == ip_trunc:
        #         count += 1
        #     if len(trunc_ip_list) == count:
        #         d[i] = count
        #     else:
        #         d[i] = 0
        #
        # return d

    def __str__(self):  # modify this
        self.size = (self.size // 10 + 1)
        self.IP_add.sort()
        stringify = []
        for i in range(len(self.IP_add)):
            stringed_objects = "{}".format(self.IP_add[i])
            stringify.append(stringed_objects)

        return str(stringify)

# Note: helper functions (not in A1)
def process(line):
    line = line.split('\t')
    time_frame = line[1].find('.')
    time_frame = int(line[1][:time_frame])
    return (line[2], time_frame, int(line[7]))


def read_file(filename):
    readfile = open(filename, "r")
    read = readfile.readlines()
    file_list = []
    for line in read:
        lines = process(line)
        file_list.append(lines)
    return file_list


def get_unique_ip_data_list(ip_data):
    ip_dict = {}
    for i in range(len(ip_data)):
        ip = ip_data[i][0]
        if ip not in ip_dict:
            ip_dict[ip] = []
        ip_dict[ip].append((ip_data[i][1], ip_data[i][2]))
    return ip_dict

# def main():
#     my_ip_list = A1('trace33.txt') #return a list of ip address object
#     my_result = my_ip_list.get_statistics()
#     t1 = Table(my_result, headers=['IP address', 'Sum', 'Freq', 'Avg'], width=13)
#     t1.draw_table()
#     print()
#     my_result = my_ip_list.get_freq('192.168.0.24')
#     t1 = Table(my_result, headers=['Time', 'Freq'])
#     t1.draw_table()
#     h1 = Histogram(my_result, x_width=3)
#     h1.draw_horizontal_histogram(unit=1)
#     h1.draw_vertical_histogram(unit=1)
#     print()
#     my_result = my_ip_list.get_sum('192.168.0.24')
#     t1 = Table(my_result, headers=['Time', 'Sum'])
#     t1.draw_table()
#     h1 = Histogram(my_result, x_width=3)
#     h1.draw_horizontal_histogram(unit=100)
#     h1.draw_vertical_histogram(unit=100)
#     print()
#     my_result = my_ip_list.get_avg('192.168.0.24')
#     t1 = Table(my_result, headers=['Time', 'Avg'])
#     t1.draw_table()
#     h1 = Histogram(my_result, x_width=3)
#     h1.draw_horizontal_histogram(unit=10)
#     h1.draw_vertical_histogram(unit=10)
#     print()
# main()

my_ip_list = A1('trace05.txt')
print(my_ip_list.get_freq_table('192.168.0.24'))

my_ip_list = A1('trace33.txt')
print(my_ip_list.get_freq_table('192.168.0.15'))
# [[0, 0], [1, 0], [2, 0], [3, 4]]