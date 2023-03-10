import time

dict_of_sounds_ttl = {}

def sound_played(o):
    dict_of_sounds_ttl[o.get_name()] = time.time()
    return True

class Frame:

    def __init__(self):
        self.dict_of_sounds = {}
        # do we want to have a time to live as well as a weighting

    def add_sign(self,o):
        self.dict_of_sounds[o.get_name()] = o

    def check_frame(self):
        flgd = []

        if len(self.dict_of_sounds) >=2:
        #     find the time last played for each of them
            for elt in self.dict_of_sounds.keys():
                for y in dict_of_sounds_ttl.keys():
                    if y == elt:
                        match = (elt,dict_of_sounds_ttl[y])
                        flgd.append(match)
                    #     is in the list and should move to next one in frame
                    else:
                        return self.dict_of_sounds[elt]

            #     find min of flgd
            minin = flgd[0][1]
            min_name = flgd[0]
            for y in range(len(flgd)):
                if flgd[y][1] < minin:
                    minin = flgd[y][1]
                    min_name = flgd[0]

            return self.dict_of_sounds[min_name]

        elif len(self.dict_of_sounds) ==1:
            x = next(iter(self.dict_of_sounds.items()))
            # print(x)
            return x

        else:
            return None




