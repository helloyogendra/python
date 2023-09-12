mydbdir: hsym `$"c:/data/db","/mydb";
{
  `trd set select from trades where time=x;
  .Q.dpft[mydbdir;x;`sym;`trd];
  delete trd from `.;
} 
each distinct trades[`time]

.Q.dpft[mydbdir; 2016.04.07; `sym; `trd1];
.Q.dpft[mydbdir; 2016.04.08; `sym; `trd2];
.Q.dpft[mydbdir; 2016.04.11; `sym; `trd3];


2021.03.19D08:00:00.108000000