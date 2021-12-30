from detect_faces import *
from caculate_depth import *

face_model = get_face_detector()
landmark_model = get_landmark_model()

cap_left = cv2.VideoCapture(1)
cap_right = cv2.VideoCapture(0)
ret, img = cap_left.read()
h, w = img.shape[:2]
color = (0, 0, 255)

while (True):
    ret, img_left = cap_left.read()
    ret, img_right = cap_right.read()
    rects_left = find_faces(img_left, face_model)
    rects_right = find_faces(img_right, face_model)
    amount_faces_left = len(rects_left)
    amount_faces_right = len(rects_right)

    if amount_faces_left == 0 or amount_faces_right == 0:
        pass
    elif amount_faces_left != amount_faces_right:
        pass
    else:
        rect_left = rects_left[0]
        rect_right = rects_right[0]

        x_left = rect_left[0] + (rect_left[2] - rect_left[0]) / 2
        y_left = rect_left[1] + (rect_left[3] - rect_left[1]) / 2
        center_point_left = (x_left, y_left)

        x_right = rect_right[0] + (rect_right[2] - rect_right[0]) / 2
        y_right = rect_right[1] + (rect_right[3] - rect_right[1]) / 2
        center_point_right = (x_right, y_right)

        depth = calc_depth(center_point_right, center_point_left, img_right, img_left)

        marks_left = detect_marks(img_left, landmark_model, rect_left)
        draw_marks(img_left, marks_left)

        marks_right = detect_marks(img_right, landmark_model, rect_right)
        draw_marks(img_right, marks_right)

        cv2.putText(img_right, "Distance: " + str(round(depth, 1)), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)



        # depths = [None] * amount_faces_left
        # for index in range(amount_faces_left):
        #     rect_left = rects_left[index]
        #     x_left = rect_left[0] + (rect_left[2] - rect_left[0]) / 2
        #     y_left = rect_left[1] + (rect_left[3] - rect_left[1]) / 2
        #     center_point_left = (x_left, y_left)
        #
        #     rect_right = rects_right[index]
        #     x_right = rect_right[0] + (rect_right[2] - rect_right[0]) / 2
        #     y_right = rect_right[1] + (rect_right[3] - rect_right[1]) / 2
        #     center_point_right = (x_right, y_right)
        #
        #     depths[index] = calc_depth(center_point_right, center_point_left, img_right, img_left)
        #
        # closest = min(depths)
        # min_index = depths.index(closest)
        #
        # marks_left = detect_marks(img_left, landmark_model, rects_left[min_index])
        # draw_marks(img_left, marks_left)
        # marks_right = detect_marks(img_right, landmark_model, rects_right[min_index])
        # draw_marks(img_right, marks_right)



        # for rect in rects_left:
        #     mid_x = int(rect[0] + (rect[2] - rect[0]) / 2)
        #     mid_y = int(rect[1] + (rect[3] - rect[1]) / 2)
        #     center_point_left = (mid_x, mid_y)
        # for rect in rects_right:
        #     mid_x = int(rect[0] + (rect[2] - rect[0]) / 2)
        #     mid_y = int(rect[1] + (rect[3] - rect[1]) / 2)
        #     center_point_right = (mid_x, mid_y)
        # depth = calc_depth(center_point_right, center_point_left, img_right, img_left)
        # print(depth)
        #
        # for rect in rects_left:
        #     mid_x = int(rect[0] + (rect[2] - rect[0]) / 2)
        #     mid_y = int(rect[1] + (rect[3] - rect[1]) / 2)
        # calc_depth()
        # # cv2.circle(img, (mid_x, mid_y), 2, color, -1, cv2.LINE_AA)
        # marks = detect_marks(img_left, landmark_model, rect)
        # draw_marks(img_left, marks)
    cv2.imshow("img_left", img_left)
    cv2.imshow("img_right", img_right)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap_left .release()
cap_right .release()
cv2.destroyAllWindows()