/***************************************************************************
This is a library for the CCS811 air

This sketch reads the sensor

Designed specifically to work with the Adafruit CCS811 breakout
----> http://www.adafruit.com/products/3566

These sensors use I2C to communicate. The device's I2C address is 0x5A

Adafruit invests time and resources providing this open source code,
please support Adafruit andopen-source hardware by purchasing products
from Adafruit!

Written by Dean Miller for Adafruit Industries.
BSD license, all text above must be included in any redistribution
***************************************************************************/

#include "Adafruit_CCS811.h"
#include "ClosedCube_HDC1080.h"

Adafruit_CCS811 ccs;
ClosedCube_HDC1080 hdc1080;

// Setup function
void setup()
{
  Serial.begin(9600);
  hdc1080.begin(0x40);

  // Check if CCS811 started succesfully
  if (!ccs.begin())
  {
    Serial.println("Failed to start sensor! Please check your wiring.");
    while (1)
      ;
  }

  // Wait for the sensor to be ready
  while (!ccs.available())
    ;
}

// Loop function, repeated every 500 milliseconds
void loop()
{
  // Set temperature and humidity variables according to HDC1080
  float temp = hdc1080.readTemperature();
  float humid = hdc1080.readHumidity();
  // Print temperature and humidity
  Serial.print(temp);
  Serial.print(",");
  Serial.print(humid);
  Serial.print(",");

  // Check if CCS811 is available
  if (ccs.available())
  {
    // Set environmental data to HDC1080 readings
    ccs.setEnvironmentalData(float(humid), float(temp));

    // Check if there is no error reading data
    if (!ccs.readData())
    {
      // Print eCO2 and TVOC
      Serial.print(ccs.geteCO2());
      Serial.print(",");
      Serial.println(ccs.getTVOC());
    }
    else
    {
      // Data could not be read, so print "-" for eCO2 and TVOC
      Serial.print("-");
      Serial.print(",");
      Serial.println("-");
      while (1)
        ;
    }
  }
  else
  {
    // CCS811 is not available, so print "-" for eCO2 and TVOC
    Serial.print("-");
    Serial.print(",");
    Serial.println("-");
  }
  // Delay next loop iteration by 500 ms
  delay(500);
}
