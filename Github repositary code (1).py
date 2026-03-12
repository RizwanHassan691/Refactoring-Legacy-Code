import statistics

class ComputeStatistics:
    """
    Class to read integers from a file and calculate statistics.
    """
    def __init__(self, file):
        """
        Constructor to initialize the file path.
        :param file: path to the file containing integers
        """
        self.file = file

    def read_ints(self):
        """
        Reads integer values from the file and returns a list.
        :return: List of integers
        """
        data = []
        try:
            with open(self.file, 'r') as f:
                for line in f:
                    num = int(line.strip())
                    data.append(num)
        except Exception as e:
            print("Error reading file:", e)
        return data

    def count(self):
        return len(self.read_ints())

    def summation(self):
        return sum(self.read_ints())

    def average(self):
        data = self.read_ints()
        return sum(data)/len(data) if data else 0

    def minimum(self):
        data = self.read_ints()
        return min(data) if data else None

    def maximum(self):
        data = self.read_ints()
        return max(data) if data else None

if __name__ == "__main__":
    file_path = "random_nums.txt"
    stats = ComputeStatistics(file_path)

    data = stats.read_ints()
    print("The values are:", data)
    print("Total values in file:", stats.count())
    print("Summation of data:", stats.summation())
    print("Average of data:", stats.average())
    print("Minimum value:", stats.minimum())
    print("Maximum value:", stats.maximum())