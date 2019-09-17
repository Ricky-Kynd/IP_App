from IP_address import IP_address
from Table import Table
from Histogram import Histogram

class A1:
    def __init__(self, filename):
        self.file_contents = read_file(filename)
        self.ip_data_list = get_unique_ip_data_list(self.file_contents)
        self.size = max([i[1] for i in self.file_contents])
        self.IP_add = []
        self.store_ip_objects()

    def store_ip_objects(self):
        # Store ip_objects in constructor
        for ip_key, data in self.ip_data_list.items():
            ip_add = IP_address(ip_key, data, self.size)
            self.IP_add.append(ip_add)

    def get_statistics(self):
        # gets the statistics for all functions
        get_stats_list = [i.get_statistics() for i in sorted(self.IP_add)]
        return get_stats_list

    def general_count(self, data, find_ip, x, y, z):
        # formats ip_data in a dictionary
        general_dict = {}
        for i in data:
          key = (i[y] // 10)
          if (key in range(0, self.size)) and key not in general_dict:
            general_dict[key] = []
          general_dict[key].append(i[x])
        return general_dict

    def sanitize_ip_address(self, ip_address):
        # cleans the list and finds the truncated ip address.
        ip = ip_address.rfind('.')
        find_ip = int(ip_address[ip + 1: ])
        ip_list = [[int(i[0][ip + 1: ]), int(i[1]), int(i[2])] for i in self.file_contents]
        return (ip_list, find_ip)

    def get_freq_table(self, ip_address):
        # gets the frequency of the table
        get_freq_list, find_ip = self.sanitize_ip_address(ip_address)
        get_dict = self.general_count(get_freq_list, find_ip, x=0, y=1, z=2)
        return_freq = self.get_freq_count(get_dict, find_ip)
        return return_freq
      
    def get_freq_count(self, adict, find_ip):
        count = 0
        freq_list = []
        for k, v in adict.items():
          if find_ip in v:
            count = v.count(find_ip)
          freq_list.append([k, count])
        return freq_list
    
    def get_sum_table(self, ip_address):
        get_sum_list, find_ip = self.sanitize_ip_address(ip_address)
        get_dict = self.general_count(get_sum_list, find_ip, x=0, y=1, z=2)
        return_sum = self.get_sum_count(get_sum_list, get_dict, find_ip)
        return return_sum

    def get_sum_count(self, data, adict, find_ip):
        sum_dict = {}
        for i in data:
          key = (i[1] // 10)
          if (key in range(0, self.size)) and key not in sum_dict:
            sum_dict[key] = []
          if i[0] == find_ip: 
            sum_dict[key].append(i[2])

        sum_total = 0
        sum_list = []
        for (k, v), (x, y) in zip(adict.items(), sum_dict.items()):
          for i in v:
            if find_ip == i:
              sum_total = sum(y)
          sum_list.append([x, sum_total])
        return sum_list

    def get_avg_table(self, ip_address):
        get_avg_list, find_ip = self.sanitize_ip_address(ip_address)
        get_dict = self.general_count(get_avg_list, find_ip, x=0, y=1, z=2)
        return_avg = self.get_avg_count(get_avg_list, get_dict, find_ip)
        return return_avg

    def get_avg_count(self, data, adict, find_ip):
        avg_dict = {}
        for i in data:
          key = (i[1] // 10)
          if (key in range(0, self.size)) and key not in avg_dict:
            avg_dict[key] = []
          if i[0] == find_ip: 
            avg_dict[key].append(i[2])

        avg_list = []
        for k, v in avg_dict.items():
            if sum(v) <= 0:
                avg_dict[k] = 0
            else:
                avg_dict[k] = round((sum(v) / len(v)), 1)

        for k, v in sorted(avg_dict.items()):
            avg_list.append([k, v])

        return avg_list

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

def main():
    my_ip_list = A1('trace33.txt') #return a list of ip address object
    my_result = my_ip_list.get_statistics()
    t1 = Table(my_result, headers=['IP address', 'Sum', 'Freq', 'Avg'], width=13)
    t1.draw_table()
    print()
    my_result = my_ip_list.get_freq_table('192.168.0.24')
    t1 = Table(my_result, headers=['Time', 'Freq'])
    t1.draw_table()
    h1 = Histogram(my_result, x_width=3)
    h1.draw_horizontal_histogram(unit=1)
    h1.draw_vertical_histogram(unit=1)
    print()
    my_result = my_ip_list.get_sum_table('192.168.0.24')
    t1 = Table(my_result, headers=['Time', 'Sum'])
    t1.draw_table()
    h1 = Histogram(my_result, x_width=3)
    h1.draw_horizontal_histogram(unit=100)
    h1.draw_vertical_histogram(unit=100)
    print()
    my_result = my_ip_list.get_avg_table('192.168.0.24')
    t1 = Table(my_result, headers=['Time', 'Avg'])
    t1.draw_table()
    h1 = Histogram(my_result, x_width=3)
    h1.draw_horizontal_histogram(unit=10)
    h1.draw_vertical_histogram(unit=10)
    print()
main()