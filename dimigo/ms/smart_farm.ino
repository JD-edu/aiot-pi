#include "DHT.h"
#include<SoftwareSerial.h>
#include <U8x8lib.h>

#define DHTPIN      2
#define CDS_A0      A0
#define CDS_D0      4        
#define DHTTYPE     DHT11
#define SOIL_A0     A1
#define SOIL_D0     6
#define FAN_OUT     9
#define PUMP_OUT    5
#define LED_ON      8


DHT dht(DHTPIN, DHTTYPE);

void setup(){
    Serial.begin(115200);
    Serial.println("JD Edu Smart Farm Start ... ");



    pinMode(CDS_A0, INPUT);
    pinMode(CDS_D0, INPUT);
    pinMode(FAN_OUT, OUTPUT);
    pinMode(PUMP_OUT, OUTPUT);
    pinMode(LED_ON, OUTPUT);

    dht.begin();
    mySerial.begin(38400);
    delay(3000);

      u8x8.begin();
  u8x8.setPowerSave(0);
    
}

int cool = 0;
int coolDTH11 = 0;
float humid;
float temp;
void loop(){

    if(Serial.available()>0){
        char c = Serial.read();
        if (c == 'c'){
            Serial.println("FAN ON");
            digitalWrite(FAN_OUT, HIGH);
        }else if(c == 'f'){
            Serial.println("FAN OFF");
            digitalWrite(FAN_OUT, LOW);
        }else if(c == 'i'){
            Serial.println("PUMP ON");
            digitalWrite(PUMP_OUT, HIGH);
        }else if(c == 'k'){
            Serial.println("PUMP OFF");
            digitalWrite(PUMP_OUT, LOW);
        }else if(c == 't'){
            Serial.println("LED ON");
            digitalWrite(LED_ON, HIGH);
        }else if(c == 's'){
            Serial.println("LED OFF");
            digitalWrite(LED_ON, LOW);
        }
    }

    coolDTH11++;
    if(coolDTH11 > 10){
        humid = dht.readHumidity();
        temp = dht.readTemperature();

        if(isnan(humid) || isnan (temp)){
            Serial.println("Failed to read DHT");
            humid = 0;
            temp = 0;
        }
        coolDTH11 = 0;
    }
    
    int cds_a0 = analogRead(CDS_A0);
    int cds_d0 = digitalRead(CDS_D0);
    int soil_a0 = analogRead(SOIL_A0);
    int soil_d0 = digitalRead(SOIL_D0);

    String tempStr = String(temp);
    String humidStr = String(humid);
    String cds_a0Str = String(cds_a0);
    String soil_a0Str = String(soil_a0);
    cool++;
    if(cool > 10){
        String packet = 'a'+ tempStr + 'b' + humidStr + 'c' + cds_a0Str + 'd' +soil_a0Str +'e';
        Serial.println(packet);
        cool = 0;
    }

    
     
    u8x8.setFont(u8x8_font_chroma48medium8_r);
    u8x8.drawString(0,0,tempStr.c_str());
    u8x8.drawString(0,1,humidStr.c_str());
    u8x8.drawString(0,2,cds_a0Str.c_str());
    u8x8.drawString(0,3,soil_a0Str.c_str());
    delay(100);
}
