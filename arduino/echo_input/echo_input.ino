char incomingByte = 0;   // for incoming serial data
int value = 0;

void setup() {
        Serial.begin(9600);     // opens serial port, sets data rate to 9600 bps
}

void loop() {

        // send data only when you receive data:
        if (Serial.available() > 0) {
                // read the incoming byte:
                incomingByte = Serial.read();
                if (incomingByte != ';' && incomingByte != ',')
                {
                  value = value*10;
                  value += (int)incomingByte - 48;
                }
                else if (incomingByte == ';' || incomingByte == ',')
                {
                  Serial.println(value, DEC);
                  value = 0;
                }        
        }
}
