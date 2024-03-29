#!/usr/bin/env python

# Playground for reading and writing CSV files in Python


import csv
import math


# convert (comma delimited) text file to csv
def txt_to_csv():
    data_files = ['data/data1.txt', 'data/data2.txt']
    for data_file in data_files:
        # read in data from txt file
        with open(data_file, mode='r') as txt_file:
            csv_name = txt_file.readline().rstrip('\n')
            headers = txt_file.readline().rstrip('\n').split(',')
            row_list = []
            row_list.append(headers)
            for line in txt_file:
                data = line.strip('\n').rsplit(',')
                row_list.append(data)

            # write data to csv file
            with open('data/' + csv_name, mode='w', newline='') as csv_file:
                csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_NONE)
                csv_writer.writerows(row_list)


# uses csv.reader(csvfile), assumes complete csv data with particular column order
def dinosaurs1():
    bipedal_dict = {}
    with open('data/dinosaur2.csv', mode='r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader) # skips headers
        for row in csv_reader:
            if row[2] == 'bipedal':
                bipedal_dict[row[0]] = row[1:]

    speed_list = []
    with open('data/dinosaur1.csv', mode='r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader) # skips headers
        bipedal_names = bipedal_dict.keys()
        for row in csv_reader:
            if row[0] in bipedal_names:
                stride_length = float(bipedal_dict.get(row[0])[0])
                leg_length = float(row[1])
                speed = ((stride_length / leg_length) - 1) * math.sqrt(leg_length * 9.8)
                speed_list.append((row[0], speed))
    speed_list.sort(key=lambda tup: tup[1], reverse=True)
    print('Fastest. . .')
    for tup in speed_list:
        print(f'{tup[0]} (speed={tup[1]})')
    print('. . .Slowest')


# uses csv.DictReader(csvfile), makes less assumptions about csv data, better readability
def dinosaurs2():
    bipedal_dict = {}
    with open('data/dinosaur2.csv', mode='r', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            if row.get('STANCE') == 'bipedal':
                bipedal_dict[row.get('NAME')] = [row.get('STRIDE_LENGTH'), row.get('STANCE')]
        
    speed_list = []
    with open('data/dinosaur1.csv', mode='r', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        bipedal_names = bipedal_dict.keys()
        for row in csv_reader:
            name = row.get('NAME')
            if name in bipedal_names:
                stride_length = float(bipedal_dict.get(name)[0])
                leg_length = float(row.get('LEG_LENGTH'))
                speed = ((stride_length / leg_length) - 1) * math.sqrt(leg_length * 9.8)
                speed_list.append((name, speed))
    speed_list.sort(key=lambda tup: tup[1], reverse=True)
    print('Fastest. . .')
    for tup in speed_list:
        print(f'{tup[0]} (speed={tup[1]})')
    print('. . .Slowest')


# add a new row (employee) to employees.csv
def add_employee(first_name='FIRSTNAME', last_name='LASTNAME', age='AGE', street='STREET', zip='ZIP'):
    with open('employees.csv', mode='r+', newline='') as csv_file: # read and write mode
        csv_reader = csv.DictReader(csv_file)
        # skip over to the last row in csv_reader
        for row in csv_reader:
            pass
        # get the next available id for the employee being added
        next_id = int(row.get('id')) + 1

        csv_writer = csv.DictWriter(csv_file, fieldnames=csv_reader.fieldnames)
        csv_writer.writerow({
            'id': next_id,
            'first_name': first_name,
            'last_name': last_name,
            'age': age,
            'street': street,
            'zip': zip
        })
    print(f'added employee: {first_name} {last_name} (id={next_id})')


# playground
def main():
    print('convert (comma delimited) text file to csv')
    txt_to_csv()
    print('testing dinosaurs1()')
    dinosaurs1()
    print()
    print('testing dinosaurs2()')
    dinosaurs2()
    print()
    print('add a new row (employee) to employees.csv')
    add_employee('Foobar', 'Baz', '21', 'Hacker Way', '94025')


if __name__ == '__main__':
    main()
