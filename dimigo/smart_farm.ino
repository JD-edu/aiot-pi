#include<Servo.h>

float humid;
float temp;
float soil;
float light;

#define fan 2
#define LED 3

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
}

void readDHT(){
  // read sensor
  // get humid temp 
  humid = 30.1;
  temp = 28.4;
}

float getSoil(){
  // read soil sensor
  soil = 45; 
}

float getLight(){
  light = 635;
}

int reportCnt = 0
long lightCnt = 0
void loop() {
  
  reportCnt++;
  if(reportCnt > 60){
    // send data to python 
    // protocol 'a'+temperature +'b' + humidity + 'c'+ soil moisture +'d' + light sensor + 'e'
    Serial.print("a");
    Serial.print(temp);
    Serial.print("b");
    Serial.print(humid);
    Serial.print("c");
    Serial.print(soil);
    Serial.print("d");
    Serial.print(light);
    Serial.println("e");
    reportCnt = 0; 
  }

  if(Serial.available() > 0){
    char cmd = Serial.read();
    if(cmd == 'c'){
      // start fan 
    }else if(cmd == 'f'){
      // stop fan 
    }else if(cmd == 's'){
      // turn on LED 
    }else if(cmd == 't'){
      // stop fan 
    }
  }
 
  delay(1000);
}
