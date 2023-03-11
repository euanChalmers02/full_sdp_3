import time

dict_of_sounds_ttl = {}


def sound_played(o):
    dict_of_sounds_ttl[o] = time.time()
    return True


class Frame:

    def __init__(self):
        self.dict_of_sounds = {}
        # do we want to have a time to live as well as a weighting

    def add_sign(self, o):
        self.dict_of_sounds[o.get_name()] = o

    def check_frame(self):
        flgd = []

        if len(self.dict_of_sounds) >= 2:

            for elt in self.dict_of_sounds.keys():
                match = False
                for y in dict_of_sounds_ttl.keys():
                    if y == elt:
                        match = True
                        match = (elt, dict_of_sounds_ttl[y])
                        flgd.append(match)

                if not match:
                    return self.dict_of_sounds[elt]

                    #     is in the list and should move to next one in frame

            if len(list(dict_of_sounds_ttl.keys())) == 0:
                return self.dict_of_sounds[elt]

            #     find min of flgd (fix the min of the multiple -----------------------------------------
            # print("flgs", flgd)
            minin = flgd[0][1]
            min_name = flgd[0]
            # print("min_name ",min_name)
            for y in range(len(flgd)):
                if flgd[y][1] < minin:
                    minin = flgd[y][1]
                    min_name = flgd[y]

            # print("selected",min_name)
            return self.dict_of_sounds[min_name[0]]

        elif len(self.dict_of_sounds) == 1:
            x = next(iter(self.dict_of_sounds.items()))
            print(x[1])
            return x[1]

        else:
            return None
