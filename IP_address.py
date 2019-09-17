class IP_address:
    def __init__(self, ip_key, data_list, size):
        self.ip_key = ip_key
        self.data = data_list
        self.size = size

    def get_ip_address(self):
        return self.ip_key

    def get_freq_list(self):
        freq_dict = {}
        for i in self.data:
            key = (i[0] // 10)
            if (key in range(0, self.size)) and key not in freq_dict:
                freq_dict[key] = []
            freq_dict[key].append(i[0])

        for i in range(0, self.size):
            if i not in freq_dict:
                freq_dict[i] = []

        freq_list = []
        for k, v in freq_dict.items():
            freq_dict[k] = len(v)
        for k, v in sorted(freq_dict.items()):
            freq_list.append([k, v])

        return freq_list

    def get_sum_list(self):
        sum_dict = {}
        for i in self.data:
            key = (i[0] // 10)
            if (key in range(0, self.size)) and key not in sum_dict:
                sum_dict[key] = []
            sum_dict[key].append(i[1])

        for i in range(0, self.size):
            if i not in sum_dict:
                sum_dict[i] = []

        sum_list = []
        for k, v in sum_dict.items():
            sum_dict[k] = sum(v)

        for k, v in sorted(sum_dict.items()):
            sum_list.append([k, v])
        return sum_list

    def get_avg_list(self):
        avg_dict = {}

        for i in self.data:
            key = (i[0] // 10)
            if (key in range(0, self.size)) and key not in avg_dict:
                avg_dict[key] = []
            avg_dict[key].append(i[1])

        for i in range(0, self.size):
            if i not in avg_dict:
                avg_dict[i] = []

        avg_list = []

        for k, v in avg_dict.items():
            if sum(v) <= 0:
                avg_dict[k] = 0
            else:
                avg_dict[k] = round((sum(v) / len(v)), 1)

        for k, v in sorted(avg_dict.items()):
            avg_list.append([k, v])

        return avg_list

    def get_statistics(self):
        get_stats_list = []
        packet_sum           = sum([i[1] for i in self.get_sum_list()])
        sum_freq             = sum([i[1] for i in self.get_freq_list()])
        ip_address           = get_stats_list.append(self.get_ip_address())
        total_pack_sum       = get_stats_list.append(packet_sum)
        total_sum_freq       = get_stats_list.append(sum_freq)
        avg_packet_size_list = get_stats_list.append(round(packet_sum / sum_freq))
        return get_stats_list

    def __eq__(self, other):
        if not isinstance(other, IP_address):
            return False
        else:
            return self.ip_key == other.ip_key

    def __lt__(self, other):
        self_indx, other_indx         = self.ip_key.rfind('.'), other.ip_key.rfind('.')
        self_ip_slice, other_ip_slice = self.ip_key[self_indx + 1:], other.ip_key[other_indx + 1:]
        return True if int(self_ip_slice) < int(other_ip_slice) else False

    def __str__(self):
        ip_address,freq, pack_sum, avg_pack = \
            self.ip_key, \
            [i[1] for i in self.get_freq_list()], \
            [i[1] for i in self.get_sum_list()], \
            [i[1] for i in self.get_avg_list()]
        return "{}:freq={},sum={},avg={}".format(ip_address, freq, pack_sum, avg_pack)