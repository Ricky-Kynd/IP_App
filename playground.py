class IP_address:
    def __init__(self, ip_key, data_list, size):
        self.ip_key = ip_key
        self.data = data_list
        self.size = size

    def get_ip_address(self):
        return self.ip_key

    def get_freq_list(self):
        freq_dict = {}

        #loop through the list
        for i in self.data:
            key = (i[0] // 10)
            if (key in range(0, self.size)) and key not in freq_dict:
                freq_dict[key] = []
            freq_dict[key].append(i[0])

        #loop through and append to a dictionary if in range
        for i in range(0, self.size):
            if i not in freq_dict:
                freq_dict[i] = []

        freq_list = []

        for k, v in freq_dict.items():
            freq_dict[k] = len(v)

        for k, v in sorted(freq_dict.items()):
            freq_list.append([k, v])

        return freq_list

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


data_list = read_file('trace33.txt')
data_list = [(i[1], i[2]) for i in data_list]
ip_key = '192.168.0.24'
size = 5
ip = IP_address(ip_key, data_list, size)
print(ip.get_freq_list())

# ip_key = '192.168.0.2'
# data_list = [(33, 60), (34, 64), (34, 1500), (34, 712), (35, 52), (35, 60), (36, 52), (36, 287), (37, 52), (37, 52), (37, 52), (39, 60), (40, 643), (40, 52)]
# size = 5
# ip = IP_address(ip_key, data_list, size)
# print(ip.get_freq_list())
# [[0, 0], [1, 0], [2, 0], [3, 12], [4, 2]]