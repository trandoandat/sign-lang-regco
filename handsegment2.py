import numpy as np
import cv2
#boundaries = [
 #   ([140, 100, 88], [180, 120, 100]),
  #  ([25, 0, 75], [180, 143, 255])
#]


def handsegment(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #lower, upper = boundaries[0]
    #lower = np.array(lower, dtype="uint8")
    #upper = np.array(upper, dtype="uint8")
    lower = np.array([0, 48, 82], dtype="uint8")
    upper = np.array([20, 255, 255], dtype="uint8")
    mask1 = cv2.inRange(hsv, lower, upper)

    #lower, upper = boundaries[1]
    lower = np.array([240,48,82], dtype="uint8")
    upper = np.array([250,255,255], dtype="uint8")
    mask2 = cv2.inRange(hsv, lower, upper)
    mask1 = mask1+mask2
    
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3,3),np.uint8),iterations=2)
    mask1 = cv2.dilate(mask1,np.ones((3,3),np.uint8),iterations = 2)
    mask2 = cv2.bitwise_not(mask1)


    # for i,(lower, upper) in enumerate(boundaries):
    # 	# create NumPy arrays from the boundaries
    # 	lower = np.array(lower, dtype = "uint8")
    # 	upper = np.array(upper, dtype = "uint8")

    # 	# find the colors within the specified boundaries and apply
    # 	# the mask
    # 	if(i==0):
    # 		print "Harish"
    # 		mask1 = cv2.inRange(frame, lower, upper)
    # 	else:
    # 		print "Aadi"
    # 		mask2 = cv2.inRange(frame, lower, upper)
    #mask = cv2.bitwise_or(mask1, mask2)
    output = cv2.bitwise_and(frame, frame, mask=mask1)
    # show the images
    # cv2.imshow("images", mask)
    # cv2.imshow("images", output)
    return output

if __name__ == '__main__':
    frame = cv2.imread("test.jpeg")
    out = handsegment(frame)
    cv2.imshow('test',out)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
