'''
create a new file with the content of another file reversed
'abc' --> 'bca'
'''

def reverse_line(infilename, outfilename):
    with open(infilename) as infile, open(outfilename, 'w') as outfile:
        for one_line in infile:
            outfile.write(f'{one_line.rstrip()[::-1]}\n')

reverse_line('test.txt', 'reversed_test.txt')
