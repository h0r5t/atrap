import os


def getParentDir(dira):
    return os.path.abspath(os.path.join(dira, '..'))


class CoverageData():

    def __init__(self, coverage_instance):
        core_dir = os.path.join(getParentDir(getParentDir(__file__)), "core")

        self.coverage_data_list = []

        for f in os.listdir(core_dir):
            if f.endswith(".py") and f != "__init__.py":
                module_name = f.replace(".py", "")
                analysis = coverage_instance.analysis2(os.path.join(core_dir, f))
                covered = analysis[1]
                not_covered = self.filterNotCovered(os.path.join(core_dir, f), analysis[3])
                line_amount = len(covered) + len(not_covered)
                if line_amount > 0:
                    coverage_percent = int((len(covered) / line_amount) * 100)
                else:
                    coverage_percent = 100
                # not_covered_as_string = self.notCoveredAsString(not_covered)
                non_covered_methods = self.getMethodsWithNonTestedCodeString(os.path.join(core_dir, f),  analysis[3])
                result = str(coverage_percent) + " % (" + str(len(covered)) + "/" + str(line_amount) + ") : "
                result += str(module_name) + " : " + non_covered_methods
                self.coverage_data_list.append(result)

    def getMethodsWithNonTestedCodeString(self, _file, not_covered_list):
        f = open(_file)
        lines = f.readlines()

        lines_to_method = {}

        c = 0
        currentdef = "no_def"
        while c < len(lines):
            cur_line = lines[c].strip()
            if (cur_line.startswith("def ")):
                currentdef = cur_line.split("def")[1].strip().split("(")[0] + "()"
            if (cur_line.startswith("if __name__ == '__main__':") or cur_line.startswith('if __name__ == "__main__"')):
                currentdef = "no_def"
            lines_to_method[c] = currentdef
            c += 1

        non_covered_methods = []
        for not_covered_line in not_covered_list:
            method = lines_to_method[int(not_covered_line)-1]
            if method not in non_covered_methods:
                non_covered_methods.append(method)

        result_string = ""
        for method in non_covered_methods:
            result_string += method + " "
        return result_string.strip()

    def filterNotCovered(self, _file, not_covered_list):
        f = open(_file)
        lines = f.readlines()

        filter_list = ['def', 'class', "if __name__ == \"__main__:\"", "import", "#", "from"]

        to_delete = []
        for not_covered_line in not_covered_list:
            line = lines[int(not_covered_line)-1].strip()
            for expression in filter_list:
                if line.startswith(expression) or line == "":
                    to_delete.append(not_covered_line)
                    break

        for a in to_delete:
            not_covered_list.remove(a)

        return not_covered_list

    def notCoveredAsString(self, not_covered_list):
        string = ""

        for a in not_covered_list:
            string += str(a) + " "

        return string.strip()

    def getCoverageData(self):
        return self.coverage_data_list
