import argparse


class MSPFile(object):

    def __init__(self, file_name):
        self._file_name = file_name
        self._data = {}

        self.read()

    def read(self):
        print("reading file name: %s" % self._file_name)

        line_count = 0
        f = open(self._file_name, 'r')
        for line in f:
            line = line.strip()
            # print("LINE: '%s'" % line.strip())
            line_count +=1

            # if line_count >= 20: break

            code= line[0:4].strip()
            fee = line[5:13].strip()

            if code in self._data:
                raise ValueError("already have code: %s" % code)

            self._data[code] = fee
            #print("%d LINE: >%s< CODE: >%s< FEE: >%s<" % (line_count, line, code, fee))

        f.close()

    def get_file_name(self):
        return self._file_name

    def diff(self, other):
        print("Comparing %s to %s" % (self.get_file_name(), other.get_file_name() ))

        for code, fee in other._data.items():
            other_fee = self._data.get(code)
            if other_fee is None:
                print("Code %s (%s) is only in file: %s" % (code, fee, other.get_file_name()))
                continue

        for code, fee in self._data.items():
            other_fee = other._data.get(code)
            if other_fee is None:
                print("Code %s (%s) is only in file: %s" % (code, fee, self.get_file_name()))
                continue

            if fee != other_fee:
                print("FEES DIFFER: CODE: %s FEE: %s --> %s" % (code, fee, other_fee))


class Application(object):

    def __init__(self, args):
        print(args)

        self._file_a = MSPFile(args.file_a)
        self._file_b = MSPFile(args.file_b)
        self._file_a.diff(self._file_b)

    def run(self):
        print("running")

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Compare MSP Fee Code Files')
    parser.add_argument('-a', '--file-a', help='File A', required=True)
    parser.add_argument('-b', '--file-b', help='File B', required=True)

    args = parser.parse_args()

    app = Application(args)
    app.run()