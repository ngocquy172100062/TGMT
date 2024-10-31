import cv2
import time
# Đọc video từ file
camera = cv2.VideoCapture(0)
# Tạo cửa sổ để hiển thị
cv2.namedWindow('Video Player', cv2.WINDOW_NORMAL)
# 
interval = 20
count = 0
# Ghi text trên hình ảnh
font = cv2.FONT_HERSHEY_SIMPLEX
font_color = (255, 255, 255)
font_scale = 1
font_thicknes = 2
# Hiển thị từng khung ảnh
while True:
    # Thời gian trước khi đọc
    start_time = time.time()
    # Đọc 1 frame
    ret, frame = camera.read()
    # Thoát khi không thể đọc được frame
    if not ret:
        break
    # Tăng count + 1
    count = count + 1
    # Định kỳ lưu ảnh xuống
    if(count%interval==0):
        cv2.imwrite(f'C:\\Users\\Admin\\Pictures\\Data\\image_{count}.jpg', frame)
        
    # Thời gian trước khi đọc
    end_time = time.time()    
    # Tình FPS:
    fps = 1/(end_time-start_time)
    # Ghi số lượng fps
    cv2.putText(frame, f'FPS: {fps:.2f}', (100, 100), font, font_scale, font_color , font_thicknes)
    # Hiển thị
    cv2.imshow('Video Player', frame)
    if(cv2.waitKey(10)==ord('q')):
        break

# Hủy bỏ player
camera.release()
cv2.destroyAllWindows()