Lab7-Basic: CMSIS-DSP 程式設計

## 專案概述
本專案的目標是使用 STM32CubeIDE，在 STM32L475E IOT Node 開發板上實作數位訊號處理 (DSP) 程式。

## 實作功能
* **硬體設備：** STM32L475E IOT Node (B-L475E-IOT01A1)
* **感測器整合：** 成功透過 I2C 讀取板載 LSM6DSL 感測器（加速度計/陀螺儀）的即時數據。
* **DSP 演算法：** 使用 CMSIS-DSP 函式庫實作「有限脈衝響應 (FIR) 低通濾波器」，以處理原始的感測器雜訊數據。
* **驗證機制：** 在正式處理即時感測器數據之前，已先使用已知的測試訊號陣列來驗證 DSP 濾波器，確保演算法的正確性與濾波效果。
* **裸機架構 (Bare-metal)：** 基本題的實作採用純粹的硬體輪詢 (Polling) 與延遲 (Delay) 方式，不依賴 RTOS 作業系統。

## 如何使用 `plot_dsp.py` 進行即時繪圖
本專案附帶了一個 Python 腳本 `plot_dsp.py`，可以透過電腦的序列埠 (Serial Port / UART) 接收開發板傳來的數據，並即時畫出原始雜訊 (Raw Data) 與濾波後 (Filtered Data) 的波形對比圖。

### 執行步驟：

**1. 安裝必備套件** 請確保你的電腦已安裝 Python 環境。打開終端機 (Terminal / 命令提示字元)，輸入以下指令安裝所需的序列埠通訊與繪圖套件：
```bash
pip install pyserial matplotlib
