from GPIOEmulator.EmulatorGUI import GPIO
import time

# Cấu hình các chân GPIO cho 8 LED
LED_PINS = [4, 17, 18, 21, 22, 23, 24, 25]

def setup():
    """Thiết lập chế độ cho các chân GPIO"""
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    
    # Cấu hình các chân LED là output
    for pin in LED_PINS:
        GPIO.setup(pin, GPIO.OUT)

def main():
    """Hàm chính điều khiển bật tắt LED"""
    setup()
    
    try:
        while True:
            # Bật từng LED lên lần lượt
            for pin in LED_PINS:
                GPIO.output(pin, GPIO.HIGH)  # Bật LED
                time.sleep(0.5)  # Giữ trạng thái trong 0.5 giây
                GPIO.output(pin, GPIO.LOW)   # Tắt LED sau khi bật xong
    except KeyboardInterrupt:
        print("Dừng chương trình")
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()
