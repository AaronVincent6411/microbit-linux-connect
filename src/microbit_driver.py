import serial
import time
import os
import sys

DEVICE = "/dev/microbit"
# DEVICE = "/dev/ttyACM0"

def wait_for_microbit():
    print("waiting for micro:bit...")
    while not os.path.exists(DEVICE):
        time.sleep(1)
    print("micro:bit connected!")

def main():
    wait_for_microbit()
    try:
        with serial.Serial(DEVICE, 115200, timeout=1) as ser:
            print("Connected to micro:bit!")
            time.sleep(2)
            ser.write(b'\x03\x04')
            time.sleep(1)
            ser.write(b'print("Hello")\r\n')
            time.sleep(0.5)
            while ser.in_waiting:
                print(ser.readline().decode(errors="ignore").strip())
    except serial.SerialException as e:
        print("Serial connection failed:", e)
        sys.exit(1)

if __name__ == "__main__":
    main()
