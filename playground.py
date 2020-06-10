#!/usr/bin/env python

# Playground for reading and writing CSV Files in Python


import csv

def txt_to_csv():
    data_files = ['data/data1.txt', 'data/data2.txt']
    for data_file in data_files:
        # read in data from .txt file
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
                csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_NONE) # default: delimeter=','
                csv_writer.writerows(row_list)
                # print(csv_file)
            csv_file.close()
        txt_file.close()


def dinosaurs():
    pass


def main():
    txt_to_csv()
    dinosaurs()


if __name__ == '__main__':
    main()

