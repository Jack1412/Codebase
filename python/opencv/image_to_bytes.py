# -------------------图片转字节，方法一-----------------------------
# 编码
image_in_bytes = cv2.imencode('.jpg', frame)[1].tobytes()
# 解码
frame = cv2.imdecode(np.frombuffer(car_img.img, np.uint8), 1)

# -------------------图片转字节，方法二-----------------------------
# Base64是网络上最常见的用于传输8Bit字节码的编码方式之一，Base64就是一种基于64个可打印字符来表示二进制数据的方法。
import base64
# 编码
encoded, buffer = cv2.imencode('.jpg', frame) # frame：640*480
footage_socket.send_string(base64.b64encode(buffer)) # 因为用的是send_string，要把字节流转化为字符形式
# 解码
frame = footage_socket.recv_string()
img = base64.b64decode(frame)
npimg = np.fromstring(img, dtype=np.uint8)