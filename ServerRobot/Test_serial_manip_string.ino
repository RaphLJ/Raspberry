String inputString = "";
boolean stringComplete = false;

void setup(){
  Serial.begin(9600);
}

void loop(){
  if(stringComplete){
    Serial.println(inputString);
    String test_substring = "";
    char test_charAt;
    
    test_charAt = inputString.charAt(1); // Attention charAt renvoie un caractère et non une string
    Serial.println(test_charAt);
    
   test_substring = inputString.substring(1,4); //(1,4) prend 123 dans "01234567"
    Serial.println(test_substring);
    
    
    inputString = "";
    stringComplete = false;
  }
}

void serialEvent(){
  while (Serial.available()){
    char inChar = (char)Serial.read();
    inputString += inChar;
    
    if (inChar == '\n') {
      stringComplete = true;
    }
  }
}
