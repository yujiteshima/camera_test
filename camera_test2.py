import cv2

cap = cv2.VideoCapture(0, cv2.CAP_V4L2)

# MJPEGフォーマットを指定（これが重要）
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
cap.set(cv2.CAP_PROP_FOURCC, fourcc)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
cap.set(cv2.CAP_PROP_FPS, 30)

# 実際の設定を確認
print(f"解像度: {int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))}x{int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))}")
print(f"FPS: {cap.get(cv2.CAP_PROP_FPS)}")
print(f"FOURCC: {int(cap.get(cv2.CAP_PROP_FOURCC))}")

while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow("Test", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
