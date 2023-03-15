#include <Wire.h>
#include <string.h>
//#include <wiring.h>
#include <LIDARLite.h>

// Globals
LIDARLite lidarLite;
int cal_cnt = 0;
int  blueLight = 4;
int  redLight = 5;

void setup()
{
  Serial.begin(9600); // Initialize serial connection to display distance readings

  lidarLite.begin(0, true); // Set configuration to default and I2C to 400 kHz
  lidarLite.configure(0); // Change this number to try out alternate configurations

  pinMode (blueLight, OUTPUT );
  pinMode (redLight, OUTPUT );

}

void loop()
{
  int dist;

  // At the beginning of every 100 readings,
  // take a measurement with receiver bias correction
  if ( cal_cnt == 0 ) {
    dist = lidarLite.distance();      // With bias correction
  } else {
    dist = lidarLite.distance(false); // Without bias correction
  }
  changeColor(120, 120);
  if (dist < 15 ){
    changeColor(0, 250);
  }
  else{
    changeColor(250, 0);
  }
  

  // Increment reading counter
  cal_cnt++;
  cal_cnt = cal_cnt % 100;

  // Display distance
  Serial.println(dist);
  //Serial.println(" cm");

  delay(1);
}

void changeColor(int bl, int rl){
  analogWrite(blueLight, bl);
  analogWrite(redLight, rl);
}