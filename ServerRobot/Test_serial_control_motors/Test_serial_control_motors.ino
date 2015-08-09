String inputString = "";
boolean stringComplete = false;

const int LEFT_MOTOR_DIR_PIN = 10;
const int LEFT_MOTOR_PWM_PIN = 5;
const int RIGHT_MOTOR_DIR_PIN = 11;
const int RIGHT_MOTOR_PWM_PIN = 6;

void setup(){
  Serial.begin(9600);
  pinMode( LEFT_MOTOR_DIR_PIN, OUTPUT);
  pinMode( LEFT_MOTOR_PWM_PIN, OUTPUT);
  pinMode( RIGHT_MOTOR_DIR_PIN, OUTPUT);
  pinMode( RIGHT_MOTOR_PWM_PIN, OUTPUT);
  
  analogWrite( LEFT_MOTOR_PWM_PIN, 0);
  analogWrite( RIGHT_MOTOR_PWM_PIN, 0);
}

void loop(){
  if(stringComplete){
    Serial.println(inputString);
    
    char leftMotorDir_char = inputString.charAt(0);
    String leftMotorSpeed_string = inputString.substring(1,4);
    
    char rightMotorDir_char = inputString.charAt(4);
    String rightMotorSpeed_string = inputString.substring(5,8);
    
    Serial.println(leftMotorDir_char);
    Serial.println(leftMotorSpeed_string);
    Serial.println(rightMotorDir_char);
    Serial.println(rightMotorSpeed_string);
    
    int leftMotorSpeed = leftMotorSpeed_string.toInt();
    int rightMotorSpeed = rightMotorSpeed_string.toInt();
    
    if (leftMotorDir_char == 'F')
    {
      digitalWrite( LEFT_MOTOR_DIR_PIN, HIGH);
    }
    else
    {
      digitalWrite( LEFT_MOTOR_DIR_PIN, LOW);
    }
        
    if (rightMotorDir_char == 'F')
    {
      digitalWrite( RIGHT_MOTOR_DIR_PIN, HIGH);
    }
    else
    {
      digitalWrite( RIGHT_MOTOR_DIR_PIN, LOW);
    }
    
    analogWrite( LEFT_MOTOR_PWM_PIN, leftMotorSpeed);
    analogWrite( RIGHT_MOTOR_PWM_PIN, rightMotorSpeed);
    
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
