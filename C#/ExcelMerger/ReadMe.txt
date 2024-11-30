###################################################
Steps to Run this C# Program:
###################################################

Requirement: 
.Net Core Framework - 8.0 and NPOI Package.


Open a terminal in VS Code and create a new C# Console project:
dotnet new console -n ExcelMerger
cd ExcelMerger
dotnet add package NPOI
dotnet add package Microsoft.Extensions.Configuration
dotnet add package Microsoft.Extensions.Configuration.Json



Verify the dependency in the ExcelMerger.csproj file:
In ExcelMerger.csproj search for "NPOI"


We need a config file to keep the configurable items:
Refer to appsettings.json file
Make sure to adjust the paths in this file - appsettings.json


3 Excel file are available for testing inside Data Folder


Run the program directly using the terminal:
dotnet run



###################################################
Publish the Application:
###################################################
dotnet publish -c Release -r win-x64 --self-contained true

Compiled\Published Code Location - bin\Release\net6.0\win-x64\publish\

Deploy the Application by copying this folder to the target server.

Better to place it in a dedicated directory, C:\Apps\ExcelMerger.

Our Application is this - ExcelMerger.exe


###################################################
Steps to Schedule with Tidal Software:
###################################################

Create a New Job in Tidal:

Configure the job type to Script or Executable.
Specify the path to the compiled .exe file of your program.
Set Parameters:

Pass folder path, number of files, and other parameters dynamically to the program (if needed).
Schedule the Job:

Use Tidal's scheduling options to run this program at desired intervals.
Monitor Logs:

Implement logging in your program to log processing details to a text file for easier debugging.




