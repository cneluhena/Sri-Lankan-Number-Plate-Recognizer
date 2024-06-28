contours, hieracrchy = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
# for contour in contours:
#         x, y, w, h = cv2.boundingRect(contour)
#         cv2.rectangle(img_g, (x, y), (x+w, y+h), (0, 255, 0), 2)
#         cv2.waitKey(0)
# cv2.imshow("Image", img_g)
# cv2.waitKey(0)