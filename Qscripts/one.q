file_info_list: enlist "";
csv_files: exec filename from ([] filename: key `:C:/Users/hello) where like[;"*.csv"] each key `:C:/Users/hello;

{[filename]

  full_filename: `$":C:/Users/hello/", string filename;
  data: ("SII"; enlist ",") 0: full_filename;

  cmd: "certutil -hashfile ", (1_ string full_filename), " MD5";

  checksum_output: system cmd;
  checksum: checksum_output[1];

  num_rows: count data;
  line: "|" sv (string full_filename, (`$checksum), `$string num_rows);
  file_info_list:: file_info_list, enlist line

 } each csv_files

fcount1: count csv_files
combined_info: "|" sv (raze enlist each file_info_list)
output_content: string fcount1, combined_info

`:C:/Users/hello/date.txt 0: enlist (raze output_content)

show `Completed!!;