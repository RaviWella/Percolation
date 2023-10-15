def default_run():
    import random
    from tabulate import tabulate
    from bs4 import BeautifulSoup
    import datetime

     
    grid = []

     
    for i in range(5):
        row = []
        for j in range(5):
             
            if random.random() < 0.9:
                row.append(str(random.randint(10, 99)).zfill(2))
            else:
                row.append('')
        grid.append(row)

     
    print(tabulate(grid, tablefmt='fancy_grid'))
     
    status = []

     
    for j in range(5):
        percolation_possible = True
         
        for i in range(5):
             
            if grid[i][j] == '':
                percolation_possible = False
                break
        # Add the status for the current column to the list
        if percolation_possible:
            status.append(' OK')
        else:
            status.append(' NO')

    # Add the status row to the the grid
    
    grid.append(status)




     # Get current time to the text file
    now = datetime.datetime.now()
 
    text_file = 'GRID_TXT_' + now.strftime('%Y-%m-%d_%H-%M') + '.txt'

    # Displaying the grid as a text file
    with open(text_file, 'w') as f:
      f.write(tabulate(grid,tablefmt='txt'))
     
    print(tabulate([status], tablefmt='simple_outline', colalign=("right",)))
 
 
        
    #Displaying the grid in a HTML file
    # Use the tabulate function to generate a grid of the numbers
    grid = tabulate(grid, tablefmt='html')


        
     
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

     
    soup = BeautifulSoup(html, 'html.parser')
    with open('GRID_HTML.html', 'w') as f:
        f.write(soup.prettify())
              
#default_run()
