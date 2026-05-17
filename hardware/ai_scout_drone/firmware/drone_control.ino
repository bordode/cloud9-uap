// TicTac-1 Drone Control System
// Arduino Mega + MPU9250 (IMU) + GPS

#include <Wire.h>
#include <Adafruit_MPU6050.h>
#include <TinyGPS++.h>

TinyGPSPlus gps;

void setup() {
  Serial.begin(115200);
  Serial1.begin(9600);  // GPS
  pinMode(9, OUTPUT);   // Ion Thruster PWM
  pinMode(8, OUTPUT);   // EM Coil
  Serial.println("TicTac-1 Boot OK");
}

void loop() {
  while (Serial1.available() > 0) gps.encode(Serial1.read());

  if (gps.location.isValid()) {
    Serial.print("Lat: "); Serial.print(gps.location.lat(), 6);
    Serial.print(" Lon: "); Serial.println(gps.location.lng(), 6);
  }

  // IMR simulation: 90% mass reduction theoretical
  float effective_mass = 1000.0;
  float imr_factor = 0.9;
  float reduced_mass = effective_mass * (1 - imr_factor);
  float target_accel = 50 * 9.81;  // 50 Gs
  float required_thrust = reduced_mass * target_accel;

  int throttle = constrain(map(required_thrust, 0, 5000, 0, 255), 0, 255);
  analogWrite(9, throttle);
  digitalWrite(8, HIGH);
  delay(100);
}
