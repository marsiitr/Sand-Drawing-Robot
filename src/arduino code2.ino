char data[10];
int ledPin =13;
void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
pinMode(ledPin,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
while(Serial.available()>0);
for(int i=0;i<10;i++)
{data[i]=Serial.read()-'0';}

for(int j=0;j<10;j++)
{ if(data[j]==0)
   {Serial.println("led is on");
    digitalWrite(ledPin,HIGH)}
    else if(data[j]==1)
    {Serial.println("led is off");
    digitalWrite(ledPin,LOW)}}
}
