import random
from tabulate import tabulate
import sys
from bs4 import BeautifulSoup
import datetime


if len(sys.argv) > 1:
	row_count = int(sys.argv[1])
	col_count = int(sys.argv[2])

	if ((row_count>=3) and (row_count<=9)) and ((col_count>=3) and (col_count<=9)):


            # Create a list to store the grid cells
                grid = []

                 
                for i in range(row_count):
                    row = []
                    for j in range(col_count):
                        
                        if random.random() < 0.9:
                            row.append(str(random.randint(10, 99)).zfill(2))
                        else:
                            row.append('')
                    grid.append(row)

                # print the grid using tabulate
                print(tabulate(grid, tablefmt='fancy_grid'))
                 
                status = []

              
                for j in range(col_count):
                    percolation_possible = True
                     
                    for i in range(row_count):
                        
                        if grid[i][j] == '':
                            percolation_possible = False
                            break
                     
                    if percolation_possible:
                        status.append('OK')
                    else:
                        status.append('NO')

                # Add the status row to the bottom of the grid
                grid.append(status)

                 
                print(tabulate([status], tablefmt='simple_outline', colalign=("right",)))

                # Get current time to the text file
                now = datetime.datetime.now()
                text_file = 'GRID_TXT_' + now.strftime('%Y-%m-%d_%H-%M') + '.txt'

            
                
                #Displaying the grid in a TXT file
                with open(text_file, "w") as f:
                    f.write(tabulate(grid, tablefmt="txt"))
                    
                #Displaying the grid in a HTML file
                grid = tabulate(grid, tablefmt='html')
                    
                # Create the HTML for the grid
                html = """
                <html>
                <body>
                <style>
                table, th, td {
                border: 0.5px solid black;
                }
                </style>
                """

                
                html += grid

                 
                html += """
                </body>
                </html>
                """

                # write the HTML to a file
                soup = BeautifulSoup(html, 'html.parser')
                with open('GRID_HTML.html', 'w') as f:
                    f.write(soup.prettify())
    
    #
    # 
    # else:
       # print("invalid")

else:
    from default import default_run
    default_run()
    
