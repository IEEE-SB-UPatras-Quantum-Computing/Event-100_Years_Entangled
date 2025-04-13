/* Annotated QRNGv1 Firmware V1.2
 * Author: Noah G. Wood (Modified for stability)
 * 
 * Copyright (c) 2019 Spooky Manufacturing, LLC
 * License: GPLv3.0
 */

int triggerPin = 2;  // Pin to pulse the laser diode
int hPin = A0;       // Pin to read horizontal polarization
int vPin = A1;       // Pin to read vertical polarization
float H = 0;         // Variable for horizontal light intensity
float V = 0;         // Variable for vertical light intensity

void setup() {
  pinMode(triggerPin, OUTPUT);
  Serial.begin(9600);
}

int getRandomBit() {
  while (true) {  // Loop until a valid bit is generated
    // Pulse the laser
    digitalWrite(triggerPin, HIGH);
    delay(3);
    digitalWrite(triggerPin, LOW);

    // Read photoresistor values
    H = analogRead(hPin);
    V = analogRead(vPin);

    // Determine the random bit
    if (H > V) return 0;
    if (H < V) return 1;

    // If equal, introduce a slight random bias to prevent infinite loops
    return random(0, 2);
  }
}

void loop() {
  int bit = getRandomBit();
  Serial.println(bit);  // Output the generated bit
  delay(10);  // Small delay to avoid excessive looping
}
