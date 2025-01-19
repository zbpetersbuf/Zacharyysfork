import csv

#open the text file in read mode

#OR

custom_headers = ['wavelength(nm)', 'intensity(au)']

with open('spectrum.csv', mode ='r') as file:
    csvFile = csv.reader(file)

    #open the csv file in wite mode
    #with open('spectrum_output.csv', mode = 'w') as csv_file:
    with open('spectrum_output.txt', mode = 'w') as txt_file:
        txt_file.write(','.join(custom_headers) + '\n')
        #csv_file.write(','.join(custom_headers) + '\n')
        
        for row in csvFile:
            txt_file.write(','.join(row) + '\n')
            #csv_file.write(','.join(row) + '\n')

print('CSV content has been saved to spectrum_output.txt')
#print('CSV content has been saved to spectrum_output.csv')

    


