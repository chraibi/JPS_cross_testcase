import matplotlib.pyplot as plt

class flow_exit:
    def __init__(self,num):
        self.path = "flow_exit_id_{}_cross.txt".format(num)
        self.data = self.get_data()

    def get_data(self):
        file = open(self.path)
        data = []

        for i in range(4):
            file.readline()

        for line in file:
            if len(line) >= 4:
                line = line.split()
                data.append(float(line[0]))

        file.close()
        return(data)

def plot_me(plotname):
    for i in range(8):
        flow = flow_exit(i)
        plt.plot(flow.data,label="Exit number {}".format(i))

    plt.legend()
    plt.grid()
    plt.xlim(0,100)
    plt.ylim(0,200)
    plt.savefig(plotname)
    #plt.show()

if __name__ == "__main__":
    plot_me("exit_usage.svg")
