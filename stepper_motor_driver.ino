int dirPin =8;
int stepperPin = 7;

void setup() 
{
 pinMode(dirPin, OUTPUT);
 pinMode(stepperPin, OUTPUT);
}

void step(boolean dir,int steps)
 {
 digitalWrite(dirPin,dir);
 delay(50);
 
 for(int i=0;i<steps;i++)
 {
   digitalWrite(stepperPin, HIGH);
   delayMicroseconds(600);//Adjust the speed of motor. Increase the value, motor speed become slower.
   digitalWrite(stepperPin, LOW);
   delayMicroseconds(600);
 }
}

void loop()
{
 //steps per revolution for 200 pulses = 360 degree full cycle rotation
 step(true,1000);//(direction ,steps per revolution). This is clockwise rotation.
 delay(500);
 step(false,1000);//Turn (direction ,steps per revolution). This is anticlockwise rotation.
 delay(500);
}
