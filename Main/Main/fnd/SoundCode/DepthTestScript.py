import pandas as pd
import serial

results = pd.DataFrame(columns=["actual distance","sensor measurement","object"])

# -------------------------------------copy------------------------

def read_tfluna_data():
    while True:
        counter = ser.in_waiting  # count the number of bytes of the serial port
        if counter > 8:
            bytes_serial = ser.read(9)  # read 9 bytes
            ser.reset_input_buffer()  # reset buffer

            if bytes_serial[0] == 0x59 and bytes_serial[1] == 0x59:  # check first two bytes
                distance = bytes_serial[2] + bytes_serial[3] * 256  # distance in next two bytes
                strength = bytes_serial[4] + bytes_serial[5] * 256  # signal strength in next two bytes
                temperature = bytes_serial[6] + bytes_serial[7] * 256  # temp in next two bytes
                temperature = (temperature / 8.0) - 256.0  # temp scaling and offset
                return distance / 100.0, strength, temperature


# ensures serial only starts on pi
ser = serial.Serial("/dev/serial0", 115200, timeout=0)  # mini UART serial device
if ser.isOpen() == False:
    ser.open()  # open serial port if not open


def get_dist():
    distance, strength, temperature = read_tfluna_data()  # read values
    print('Distance func: {0:2.2f} m, Strength: {1:2.0f} / 65535 (16-bit), Chip Temperature: {2:2.1f} C'. \
          format(distance, strength, temperature))  # print sample data

    return distance



def depth_sensor(target_dis,object):
    for y in range(10):
        dist = get_dist()
        df_len = len(results)
        results.loc[df_len,"actual distance"] = target_dis
        results.loc[df_len, "sensor measurement"] = dist
        results.loc[df_len, "object"] = object

def export_results():
    results.to_csv("results_from_depth_tests.csv")


def script(object):
    for x in range(8):
        print(x+1)
        depth_sensor(x+1,object)
        c = input("Enter an word or letter to read dist @ ",x+1)

if __name__ == "__main__":
    print("Wall Test")
    print("-"*50)
    script("wall")
    print("Bin Test")
    print("-"*50)
    script("bin")
    print("Pillar Test")
    print("-"*50)
    script("pillar")
    print("Stand Alone Whiteboard Test")
    print("-"*50)
    script("Stand Alone Whiteboard")

    export_results()
