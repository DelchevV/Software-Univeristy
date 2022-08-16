def substring(f_line, s_line):
    while f_line in s_line:
        s_line = s_line.replace(f_line, "")
    return s_line


print(substring(input(), input()))
