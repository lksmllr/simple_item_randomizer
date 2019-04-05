################################################################
#                                                              #
#      author:                                                 #
#          Lukas Mueller                                       #
#               https://github.com/lksmllr                     #
#                                                              #
################################################################

import numpy as np
import pprint as pp
import random
import csv

class ivonnes_perm:

    # path to file (incl filename)
    PATH = None
    # items per category
    ITEMS_PER_CAT = None
    # how many times
    ITEM_REP = None
    # num categories
    NUM_CAT = None
    # list of finished perm lists
    PERM_LISTS = None
    # list of category lists
    categories = None

    # init stuff
    def __init__(self, path, items, rep):
        self.PERM_LISTS = []
        self.PATH = path
        self.ITEMS_PER_CAT = items
        self.ITEM_REP = rep
        self.categories = self.read_items()
        self.NUM_CAT = len(self.categories)

    # read ORDERED lines from .csv and seperate to categories
    def read_items(self):
        # list of lists, each containing each category item times ITEM_NUM_REP
        categories = []
        # preprocessing .csv
        with open(self.PATH, 'r') as file:
            lines = file.readlines()
            # simplify the category breakdown
            # SUGGESTION maybe additional column (int) indicating category ?
            items = []
            counter = 0
            # for each item in file do ...
            for line in lines:
                # seperate
                line = line.split(';')
                #print(line)
                # append item times ITEM_NUM_REP to category list (items)
                #items.append(line[0])
                items.append(line)
                if counter < self.ITEMS_PER_CAT-1:
                    # increment to get all 8 of any category
                    counter += 1
                else:
                    # if all in, add category to list
                    counter = 0
                    categories.append(items)
                    items = []
        return categories

    # so proud of myself because of this lil beauty here
    # @Ivonne THIS IS WHERE MAGIC STUFF HAPPENS
    def get_perm_indices(self):
        check = np.zeros(8)
        arr = np.zeros(shape=(self.ITEMS_PER_CAT, self.ITEM_REP))
        for i in range(0,len(arr)):
            for j in range(0, len(arr[0])):
                val = (i + j) % len(arr)
                arr[i][j] = val
                check[val] += 1
        for row in arr:
            np.random.shuffle(row)
        np.random.shuffle(arr)
        return arr

    # create how_many lists
    def get_list(self, how_many):

        # for how many u d like to create
        for i in range(0, how_many):
            tmp_list = []
            category_indices = []

            # get indice matrix for each category
            for c in range(0, self.NUM_CAT):
                category_indices.append(self.get_perm_indices())

            # create phase
            for phase in range(0, self.ITEMS_PER_CAT):
                phase_items = []
                for category in range(0, self.NUM_CAT):

                    for index in category_indices[category][phase]:
                        phase_items.append(self.categories[category][int(index)])
                # @Ivonne shuffle finished phase (?)
                random.shuffle(phase_items)
                # append to list of phases
                tmp_list.append(phase_items)

            # flatten / finish list
            flat_list = []
            for phase in tmp_list:
                for item in phase:
                    flat_list.append(item)
            self.PERM_LISTS.append(flat_list)

    def write_to_file(self):
        for i in range(0, len(self.PERM_LISTS)):
            with open('perms/list_{}.csv'.format(i+1), 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(self.PERM_LISTS[i])

def main():
    perm = ivonnes_perm('items/items.csv', 8, 5)
    perm.get_list(4)
    perm.write_to_file()

if __name__ == '__main__':
    main()
