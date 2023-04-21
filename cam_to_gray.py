import cv2

# 웹캠 캡처 객체 생성
cap = cv2.VideoCapture(0)

# 프레임 크기 설정
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# 비디오 루프
while True:
    # 현재 프레임 읽기
    ret, frame = cap.read()

    # 프레임이 제대로 읽혔으면 흑백으로 변환
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    

    # 흑백으로 변환된 프레임 보여주기
    cv2.imshow('Black and White Video', gray_frame)

    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) == ord('q'):
        break

# 자원 해제
cap.release()
cv2.destroyAllWindows()