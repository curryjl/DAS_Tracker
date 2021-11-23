def read_file(path):
    with open(path, 'r', encoding='UTF-8') as reader:
        return reader.read()

def update_counter_text(dasCounter, previousDasCounter, dasCounterText):
    # BUG: It appears python is reading from the file while it's being truncated and returning ''
    if dasCounter != '':
        # only update ui for number if the previous value was different
        if dasCounter != previousDasCounter:
            previousDasCounter = dasCounter
            dasCounterText.update(f'DAS Counter: {dasCounter}')

def update_progress_bar(dasCounter, dasMax, progressBar):
    if dasCounter != '':
        if int(dasCounter) < 10:
            progressBar.update(dasCounter, dasMax, bar_color=('red', 'white'))
        else:
            progressBar.update(dasCounter, dasMax, bar_color=('green', 'white'))
