#include <Servo.h>
#include <ezButton.h>

// servo
Servo tiltDetect;
int servoPos = 0;

// limit switch
const int limitSwitchPin = 12;
ezButton limitSwitch(limitSwitchPin);

// interval to repeat in ms
const int interval = 5000;

const int allowableTrunkInclination = 10;


void setup() {
  Serial.begin(9600); // serial monitor
  // limit switch
  limitSwitch.setDebounceTime(50);

  // servo
  tiltDetect.attach(9);
  tiltDetect.write(0);

}

void loop() {
  limitSwitch.loop();
  // bring servo to base position
  for (servoPos = 0; servoPos <= 90; servoPos += 1) {
    int state = limitSwitch.getState(); // HIGH or LOW for pressed or not pressed

    tiltDetect.write(servoPos);
    Serial.println(servoPos);
    delay (15);

    if (state == HIGH && servoPos <= allowableTrunkInclination) { // test to get correct servoPos value
        // maybe add buzzer
        Serial.println("WARNING");
    }
    else {
        Serial.println("Posture is in check");
    }
  }
  delay(interval);
}
