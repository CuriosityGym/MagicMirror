#include <Mouse.h>
void setup() {
  pinMode(5, INPUT);

}

void loop() {
   if(digitalRead(5) == HIGH)
   {
     Mouse.begin();     
     Mouse.move(1, 1, 0);
     Mouse.end();
     delay(1000);  
   }  

}
