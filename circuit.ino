
int triggerPin = 2;
int hPin = A0;
int vPin = A1;
int H = 0;
float V = 0;

void setup() {
  // put your setup code here, to run once:
  pinMode(13, OUTPUT);
  pinMode(triggerPin, OUTPUT);
  Serial.begin(9600);

}

int Random() {
  // Pulse the laser
  digitalWrite(triggerPin, HIGH);
  delay(300);
  digitalWrite(triggerPin, LOW);

  // Read the photoresistors
  H = analogRead(hPin);
  V = analogRead(vPin);

  // delay(500);
  return H;

  // Determine random bit
  if(H > V) { // More photons in the H mode, return 0
    return 0;
  }
  if(H < V) { // More photons in the V mode, return 1
    return 1;
  }
  else { 
    /* The same number of photons are in both modes!
        This is actually not an uncommon occurrence, for our
        purposes we will simply run the function recursively until
        a random bit can be generated.
     */
    Random();
  }
}
 
void loop() {
  // The main program
  // Run our program and print the random bit to serial
  Serial.println(Random());
}
