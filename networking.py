import appgamekit as agk


class Network:
    def __init__(self, name, ip, port):
        self.target_ip = ip
        self.port = port
        self.last_msg_id = 0
        self.name = name
        self.state = 0
        self.type = 0
        self.network_id = 0


    def host(self):
        network_id = agk.host_network("AGK Test Game", self.name, 45000)
        self.type = 0
        self.state = 1
        return network_id

    def client(self):
        network_id = agk.join_network_ip(self.target_ip, 45000, self.name)
        self.type = 0
        self.state = 1
        return network_id

    def update(self):
        pass
