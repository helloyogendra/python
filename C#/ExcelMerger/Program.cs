using System;
using System.IO;
using System.Linq;
using Microsoft.Extensions.Configuration;
using NPOI.SS.UserModel;
using NPOI.XSSF.UserModel;

namespace ExcelMerger
{
    class Program
    {
        static void Main(string[] args)
        {
            // Set up configuration
            IConfiguration config = new ConfigurationBuilder()
                .SetBasePath(Directory.GetCurrentDirectory())
                .AddJsonFile("appsettings.json", optional: false, reloadOnChange: true)
                .Build();

            string folderPath = config["FolderPath"];
            string mergedFileName = config["MergedFileName"];
            string processedFolderPath = config["ProcessedFolderPath"];
            int numberOfFilesToMerge = int.Parse(config["NumberOfFilesToMerge"]);
            string fileStartsWith = config["FileStartsWith"];
            string fileEndsWith = config["FileEndsWith"];

            try
            {
                // Get files based on criteria
                var files = Directory.GetFiles(folderPath)
                    // .Where(f => f.StartsWith(fileStartsWith, StringComparison.OrdinalIgnoreCase) &&
                    //             f.EndsWith(fileEndsWith, StringComparison.OrdinalIgnoreCase))
                    .Take(numberOfFilesToMerge)
                    .ToList();

                if (!files.Any())
                {
                    Console.WriteLine("No files matching the criteria found.");
                    return;
                }

               // Create a new workbook for the merged file
                IWorkbook mergedWorkbook = new XSSFWorkbook();
                ISheet mergedSheet = mergedWorkbook.CreateSheet("Merged");

                int currentRow = 0;
                bool isHeaderAdded = false; // Flag to track if the header has been added

                foreach (var file in files)
                {
                    using (var fileStream = new FileStream(file, FileMode.Open, FileAccess.Read))
                    {
                        IWorkbook workbook = new XSSFWorkbook(fileStream);
                        ISheet sheet = workbook.GetSheetAt(0);

                        for (int rowIndex = sheet.FirstRowNum; rowIndex <= sheet.LastRowNum; rowIndex++)
                        {
                            IRow row = sheet.GetRow(rowIndex);
                            if (row == null) continue;

                            // Check if it's the header row and skip if already added
                            if (rowIndex == sheet.FirstRowNum && isHeaderAdded)
                                continue;

                            IRow newRow = mergedSheet.CreateRow(currentRow++);
                            for (int colIndex = row.FirstCellNum; colIndex < row.LastCellNum; colIndex++)
                            {
                                ICell cell = row.GetCell(colIndex);
                                if (cell != null)
                                {
                                    ICell newCell = newRow.CreateCell(colIndex);
                                    newCell.SetCellValue(cell.ToString());
                                }
                            }

                            // Mark header as added after the first row of the first file
                            if (rowIndex == sheet.FirstRowNum)
                                isHeaderAdded = true;
                        }
                    }
                }

                // Save the merged file
                string mergedFilePath = Path.Combine(folderPath, mergedFileName);
                using (var fileStream = new FileStream(mergedFilePath, FileMode.Create, FileAccess.Write))
                {
                    mergedWorkbook.Write(fileStream);
                }

                // Move processed files
                foreach (var file in files)
                {
                    string destPath = Path.Combine(processedFolderPath, Path.GetFileName(file));
                    File.Move(file, destPath);
                }

                Console.WriteLine("Merging complete and files moved.");
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error: {ex.Message}");
            }
        }
    }
}