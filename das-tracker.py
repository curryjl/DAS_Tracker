import PySimpleGUI as sg                        # Part 1 - The import
import helpers as h

previousDasCounter = 1
dasCounter = 1
dasMax = 16

dasCounterText = sg.Text(f'DAS Counter: {dasCounter}', 
                            key='das_counter_text')
progressBar = sg.ProgressBar(max_value=dasMax, 
                            orientation='horizontal', 
                            size=(20, 40), 
                            bar_color=('green', 'white'),
                            style='winnative',
                            key='das_progress_bar')

# Define the window's contents
layout = [  [dasCounterText], [progressBar]  ]

# Create the window
window = sg.Window('Tetris Mod', layout)      # Part 3 - Window Defintion

# clicking a button will fire off an event, causing read to return.. (My suspicion)       
# read blocks unless given a timeout value                                        
while True:
    event, values = window.read(1)                   # Part 4 - Event loop or Window.read call (waits 1 millisecond)
    
    if event == sg.WIN_CLOSED:
        break
    dasCounter = h.read_file(r"C:\Users\Curry\source\repos\DasReader\DasReader\dascounter.txt")
    h.update_counter_text(dasCounter, previousDasCounter, dasCounterText)
    h.update_progress_bar(dasCounter, dasMax, progressBar)

# Finish up by removing from the screen
window.close()