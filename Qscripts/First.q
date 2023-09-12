/ File Name = First.q
/ Hello, I am a comment.

a:101; b:a+100;
show "Starting..."
show b
lists: 11 22 33 44 55
lists
lists * 1000
f:{x+y}
f[100;200]

myFunction: {
  [i;j;k]
  c: i + j + k;
  d: c * 10;
  d
  }
myFunction[10;20;30]

show .z.x

.Q.opt[.z.x][`xyz]

show "Completed..."


/
This is an example of
multiline comment
\
