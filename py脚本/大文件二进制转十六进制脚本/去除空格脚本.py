with open('pocky.txt', 'r') as f_in, open('output.txt', 'w') as f_out:
    for line in f_in:
        new_line = line.replace(' ', '')
        f_out.write(new_line)