list1: 10 20 30 40;
list1[1]: 11;
show list1;

list1[1 3]                                      / get items at index 1 and 3

list2: (10 20 30; 50 60 70; 80 90 40);
show list2;
show list2[1;1];                                / get item at row 1, column 1

mix_list: (22; 33.55; `abc; "hello")
type mix_list

mix_list[0]: 55.75;
show mix_list;

now: 2023.09.09D08:08:03;
show now;
show type now;                                  / -12h, means timestamp

tt: "t"$now;                                    / extract time part and store in a variable
show tt;

show "d"$now;                                    /  extract date part and print.
show "m"$now;                                    /  extract year:month part and print.
show "v"$now;                                    /  extract time part and print.
show "u"$now;                                    /  extract hour:minute part and print.

show now.year;
show now.month;
show now.date;
show now.time;
show now.minute;

/ show `$"other format to extract date-time part", now.mm, now.dd, now.hh, now.uu, now.ss;


show `mango`cherry`banana;                       /  print list of symbols
show (3 * 2 + 3 - 1);                            /  evaluate expression (right to left) and print the result, #12

0N!3*3*3                                            /   evaluate expression (right to left) and print the result, and return the result
0N!(2*3*5)                                          /   same like above

aa: 0N!3*3*3                                        /   evaluate expression (right to left) and print the result, and store the returned result
show aa;

bb: 5*0N!3*3                                        / it will print - 9 and it will return 45, so value of variable 'bb' will be 45
show bb;


{[x]; 
    show x;
    show `func;
    x*x
 }[3]

ls: 2 3 4 5;

{[x]
    show x;
    x*x
 } each ls






/ Project POC
/ data: ("SII"; enlist ",") 0: `data1.csv                             / load csv-file in a variable
/ count data                                                          / count number of rows from above variable, this means 'number of rows from csv-file'

/ csv_string: ",\"" sv/: string each flip data                        / flip this data-variable
/ raze csv_string                                                     / raze to a single value
/ md5 raze csv_string                                                 / get md5 hash/checksum value

/ system "certutil -hashfile data1.csv MD5"                           / calculate hash/checksum value in Windows and get it back in KDB, along with extra output
/ (system "certutil -hashfile data1.csv MD5")[1]                      / calculate hash/checksum value in Windows and get only checksum value in KDB
/ (system "certutil -hashfile c:\\users\\hello\\data1.csv MD5")[1]    / observe file path here, fully qualified path mentioned


/ Below code execute in Python to get md5 hash/checksum value
/ import hashlib
/ hashlib.md5(open('data1.csv', 'rb').read()).hexdigest() 
/ 
/ Below command execute in Linux to get md5 hash/checksum value
/ md5sum data1.csv
\


file_info: hopen `:C:/Users/hello/file_info.txt;
csv_files: exec filename from ([] filename: key `:C:/Users/hello) where like[;"*.csv"] each key `:C:/Users/hello;
file_info_list: enlist "";


show csv_files;

lst: 10 20 30
tmp: ()

{[x]

  show x
} each lst

show file_info_list;



