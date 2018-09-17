import re
file = open("C:\PythonProjects\GA High Schools Dashboard\GA Schools by County.txt")

all_counties_list = []

county_match = re.compile(r'==\w+\s+County==')
school_match = re.compile(r'(\*)(\[*)(\w)')
dict = {}
counter = 0
# county_re = re.compile()
for line in file:
    current_county = ""
    llen = len(line)
    if llen == 1:
        continue
    # if line.count('=') == 4:
    #     print(line)
    if county_match.search(line):
        print(line)

    print("line {linenum}(len-{linelength}): {linetext}".format(linenum = counter, linelength=llen,linetext=line))
    counter += 1