import numpy as np
import cv2
import sys
import os
import eq2cm

if __name__ == '__main__':
    args = sys.argv
    img_path = args[1]
    out_dir = args[2]
    eqimg = cv2.imread(img_path)

    for i in range(-4, 4):
        print('processing...')
        pers = eq2cm.eq_to_pers(eqimg, np.pi/2, i * np.pi/4, 0, 480, 480)
        cv2.imwrite(os.path.join(out_dir, 'angle' + str(i + 4) + '.JPG'), pers)
