# CCS811-HDC1080
Code to read CCS811 and HDC1080 data from CJMCU-8118, print it to serial monitor and save it to .csv file.

Based on [CJMCU-8118_InfluxDB](https://github.com/bfaliszek/CJMCU-8118_InfluxDB) and example sketches from libraries listed below.

## Dependencies
- [Arduino Software](https://www.arduino.cc/en/main/software)
- [Adafruit CCS811 library](https://github.com/adafruit/Adafruit_CCS811)
- [ClosedCube HDC1080 library](https://github.com/closedcube/ClosedCube_HDC1080_Arduino)

## Wiring
### Arduino Uno
CJMCU-8118 | Arduino Uno
---------- | -----------
VCC | 3.3V
GND | GND
SCL | A5
SDA | A4
WAK | GND

### Other
If you are using another board, check your manufacturer's reference for the appropriate I2C pins.

## How to use
- Install the required dependencies
- Set up the CJMCU-8118 with your Arduino (as mentioned above)
- Verify and upload the script to your Arduino, it should run automatically
- To see your readings:
  - Open the Arduino serial monitor, or serial monitor of your choice
- To save your readings:
  - Open TeraTerm, or another serial monitor with file saving capabilities
  - File > Save, and follow the rest of the saving dialog
