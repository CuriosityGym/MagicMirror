void setup() {
  pinMode(5, INPUT);

}

void loop() {
   if(digitalRead(5) == HIGH){
     Mouse.begin();
     Mouse.press(MOUSE_LEFT);
     Mouse.move(1, 1, 0);
     
     //Mouse.release(MOUSE_RIGHT);
   } 

   if(digitalRead(5) == LOW){
     Mouse.end();     
     Mouse.release(MOUSE_LEFT);
   } 

}
