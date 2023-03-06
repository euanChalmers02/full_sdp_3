class ThreadingState:

    # how to refine into one sys variable
    # how to have super states
    def __init__(self):
        self.stop = False
        self.read_out = False
        self.no_beeps = 3
        self.pause_length = 1
        self.quit = False
        self.all_objects = []
        self.voice = False
        self.ocr = False
        self.dist = False

    def str_print(self):
        print('Stop', self.stop)
        print('Read out', self.read_out)
        print('Quit', self.quit)



state = ThreadingState()
