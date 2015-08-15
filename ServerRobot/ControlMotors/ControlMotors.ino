#include <Servo.h>

String inputString = "";
boolean stringComplete = false;

const int LEFT_MOTOR_DIR_PIN = 10; //Indiquer le numéro des pins pour les moteurs
const int LEFT_MOTOR_PWM_PIN = 5;
const int RIGHT_MOTOR_DIR_PIN = 11;
const int RIGHT_MOTOR_PWM_PIN = 6;

Servo panServo; //Créer un objet par servomoteur
Servo tiltServo;

void setup(){
  Serial.begin(9600);
  pinMode( LEFT_MOTOR_DIR_PIN, OUTPUT);
  pinMode( LEFT_MOTOR_PWM_PIN, OUTPUT);
  pinMode( RIGHT_MOTOR_DIR_PIN, OUTPUT);
  pinMode( RIGHT_MOTOR_PWM_PIN, OUTPUT);
  
  panServo.attach(13);
  tiltServo.attach(12);
  
  analogWrite( LEFT_MOTOR_PWM_PIN, 0);
  analogWrite( RIGHT_MOTOR_PWM_PIN, 0);
  
  panServo.write(90);
  tiltServo.write(20);
}

void loop(){
  if(stringComplete){
    Serial.println(inputString);
    
    // Récupérer chaque information de la chaine recue
    
    char leftMotorDir_char = inputString.charAt(0);
    String leftMotorSpeed_string = inputString.substring(1,4);
    
    char rightMotorDir_char = inputString.charAt(4);
    String rightMotorSpeed_string = inputString.substring(5,8);
    
    String panPosition_string = inputString.substring(8,11);
    String tiltPosition_string = inputString.substring(11,14);
    
    Serial.println(leftMotorDir_char);
    Serial.println(leftMotorSpeed_string);
    Serial.println(rightMotorDir_char);
    Serial.println(rightMotorSpeed_string);
    
    int leftMotorSpeed = leftMotorSpeed_string.toInt();
    int rightMotorSpeed = rightMotorSpeed_string.toInt();
    int panPosition = panPosition_string.toInt();
    int tiltPosition = tiltPosition_string.toInt();
    
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
    
    if (panPosition > 135)
    {
      panPosition = 135;
    }
    
    if (panPosition < 45)
    {
      panPosition = 45;
    }
    
    if (tiltPosition > 90)
    {
      tiltPosition = 90;
    }
    
    if (tiltPosition < 0)
    {
      tiltPosition = 0;
    }
    
    
    panServo.write(panPosition);
    tiltServo.write(tiltPosition);
    
    inputString = "";
    stringComplete = false;
  }
}

void serialEvent(){
  //Tant que Serial recoit quelque chose, construire la chaine avec chaque caractère recu
  
  while (Serial.available()){
    char inChar = (char)Serial.read();
    inputString += inChar;
    
    if (inChar == '\n') {
      stringComplete = true; //Pour lancer les instructions de loop()
    }
  }
}
