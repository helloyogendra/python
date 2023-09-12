/ Comment - This is a full working example of .q script: 10/Nov/2020.
/ How to run this script- 
/ 1.) If Q is configured, go to cmd prompt and type- q print.q, 
/ 2.) first run Q in cmd prompt by just typing the q, once q prompt is available simply type and press enter - q) \l print.q

a:101; b:a+10;
show "Staring Q Script"
show `World
0N!3+2        
show b
t: 1 2 3
m: 4
x: t * m
x
show x


0N!`yogi
0N! x

f:{
  [i;j;k]
  c:i+j+k;
  d:c*10;
  d
   }
f[1;2;3]
show .z.x         		/ Accessing command line argument here, like a key:value pair. 
                       / To pass argument to this script run it like - C:\q print.q -xyz 1001
.Q.opt[.z.x][`xyz]		/ This line will print: 1001

show "Q Script execution completed"
/ 
This is a example of
multiline comment, last line of this script will close the q prompt automatically.




