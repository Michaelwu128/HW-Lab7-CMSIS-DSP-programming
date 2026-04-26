import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# --- 設定區 ---
PORT = 'COM4'   # 請改成你的 STM32 COM Port
BAUD = 115200   # 波特率
POINTS = 100    # 畫面上最多顯示幾個點

# 初始化序列埠
try:
    s = serial.Serial(PORT, BAUD, timeout=1)
    print(f"成功連接到 {PORT}")
except Exception as e:
    print(f"連接失敗: {e}")
    exit()

# 準備資料陣列
raw_data = [0] * POINTS
filtered_data = [0] * POINTS

# 設定圖表
fig, ax = plt.subplots()
ax.set_title('STM32 DSP Real-time Filter (LSM6DSL)')
ax.set_ylabel('Z-Axis Acceleration')
line_raw, = ax.plot(raw_data, label='Raw Data', color='blue', alpha=0.4)
line_filtered, = ax.plot(filtered_data, label='Filtered Data (FIR)', color='red', linewidth=2)
ax.legend(loc='upper right')

def update(frame):
    try:
        # 讀取一行字串並解碼
        line = s.readline().decode('utf-8').strip()
        if line:
            # 用逗號分割資料
            r, f = line.split(',')
            
            # 更新陣列 (移除最舊的，加入最新的)
            raw_data.append(float(r))
            raw_data.pop(0)
            
            filtered_data.append(float(f))
            filtered_data.pop(0)

            # 更新圖表線條
            line_raw.set_ydata(raw_data)
            line_filtered.set_ydata(filtered_data)
            
            # 動態調整 Y 軸範圍
            ax.relim()
            ax.autoscale_view()
    except Exception as e:
        pass # 忽略偶爾的傳輸錯誤
    
    return line_raw, line_filtered

# 開始即時動畫
ani = animation.FuncAnimation(fig, update, interval=20, blit=False)
plt.show()

# 關閉視窗後斷開序列埠
s.close()