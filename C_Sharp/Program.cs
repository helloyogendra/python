using System;
using System.Collections.Generic;
					
public class Program
{
	public static void Main()
	{
		Console.WriteLine("Hello World");
		
		Base obj1 = new Child();
		obj1.a = 11;

		Console.WriteLine(obj1.a);
		
		Child c = (Child) obj1;
		c.a = 21;
		c.b = 31;
		
		Console.WriteLine(c.a);
		Console.WriteLine(c.b);
		
		List<Base> lst1 = new List<Base>();
		//List<Child> lst2 = new List<Base>();
        lst1.Add(c);

        List<Child> lst2 = new List<Child>();
        lst1.AddRange(lst2);
		Console.WriteLine("Hello");
	}
}

class Base
{
	public int a;
}

class Child : Base
{
	public int b;
}