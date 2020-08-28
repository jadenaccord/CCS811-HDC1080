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

void setup() {
  Serial.begin(9600);

  Serial.println("\n\n\nCCS811 & HDC1080 test");

  hdc1080.begin(0x40);
  Serial.print("Manufacturer ID=0x");
  Serial.println(hdc1080.readManufacturerId(), HEX); // 0x5449 ID of Texas Instruments
  Serial.print("Device ID=0x");
  Serial.print(hdc1080.readDeviceId(), HEX); // 0x1050 ID of the device

  if(!ccs.begin()){
    Serial.println("Failed to start sensor! Please check your wiring.");
    while(1);
  }

  // Wait for the sensor to be ready
  while(!ccs.available());
}

void loop() {
  float temp = hdc1080.readTemperature();
  float humid = hdc1080.readHumidity();
  Serial.print("\n\ntemperature: ");
  Serial.print(temp);
  Serial.print(" C");

  Serial.print("\nhumidity: ");
  Serial.print(humid);
  Serial.print(" %");
  
  if(ccs.available()){

    ccs.setEnvironmentalData(float(humid), float(temp));
    
    if(!ccs.readData()){
      Serial.print("\nCO2: ");
      Serial.print(ccs.geteCO2());
      Serial.print("ppm, TVOC: ");
      Serial.print(ccs.getTVOC());
    }
    else{
      Serial.println("ERROR!");
      while(1);
    }
  }
  delay(500);
}
