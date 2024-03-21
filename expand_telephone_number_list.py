##########
#
#  read a file with a list and / or range of telephone numbers
#  return a file with all the individual numbers
# 
#  input format:
#
#  7165551000
#  7165551005 - 1010
#  7165551111
#  
#  output format:
#
#  7165551000
#  7165551005
#  7165551006
#  7165551007
#  7165551008
#  7165551009
#  7165551010
#  7165551111
#
#########


def expand_range(input_range):
    # strip and then split string to handle trailing blanks
    # assume blank dash blank is consistent delimiter
    start, end = input_range.strip().split(" - ")
    # format real end number by replacing the last, length of end digits in start with the end digits
    modified_end = start[0:len(start)-len(end)] + end
    # create a list of numbers out of the range of numbers between and including start and end
    mylist = list(range(int(start), int(modified_end)+1))
    return mylist

def main(input_file, output_file):
    with open(input_file, 'r') as my_input_file:
        lines = my_input_file.readlines()

    formatted_numbers = []
    for line in lines:
        if '-' in line:
            # expand ranges here
            expanded_numbers = expand_range(line)
            formatted_numbers.extend(expanded_numbers)
        else:
            # single number here
            formatted_numbers.append(line.strip())

    with open(output_file, 'w') as my_output_file:
        for number in formatted_numbers:
            my_output_file.write(f"{number}\n")

if __name__ == "__main__":
    input_filename = "telephone_numbers_range_input.txt"
    output_filename = "telephone_numbers_list_output.txt"
    main(input_filename, output_filename)
    print(f"Formatted telephone number list saved to {output_filename}")
