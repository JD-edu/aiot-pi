#include<Servo.h>

Servo sv;
#define 2 IR
#define 4 MOTOR_A
#define 5 MOTOR_B

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  pinMode(IR,INPUT) // IR sensor  
  sv.attach(3);
}

void motor_stop(){
  digitaWrite(MOTOR_A, LOW);
  digitaWrite(MOTOR_B, LOW);
}

void motor_on(){
  digitaWrite(MOTOR_A, HIGH);
  digitaWrite(MOTOR_B, LOW);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(digitalRead(IR) == 1) // can contected 
  {
     motor_stop()
     Srial.write("s\r\n");
     string cmd = Serial.readStringUntil('\n');
      if (cmd == "can"){
        delay(3000);
        sv.write(180); // can
        delay(3000);
        motor_on()
      }else if(cmd == "pet"){
        delay(1000);
        sv.write(0);
        delay(3000);
        motor_on()
      }
  }else{
     motor_on();
 ;
    }
  }
}
