#!/usr/bin/env python3

'''Compute the number of mblbp features in a given window'''

def compute_nb_of_features(window_w, window_h):
    nb_of_features = 0
    for block_w in range(3, window_w, 3):
        for block_h in range(3, window_h, 3):
            for offset_x in range(window_w - block_w + 1):
                for offset_y in range(window_h - block_h + 1):
                    nb_of_features += 1
    return nb_of_features

def main():

    window_w = 20
    window_h = 20

    print(compute_nb_of_features(window_w, window_h))

if __name__ == '__main__':
    main()
