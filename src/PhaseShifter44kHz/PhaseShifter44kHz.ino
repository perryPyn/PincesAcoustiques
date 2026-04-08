// Constantes
const unsigned int angleCste = -2;    // -[1,360]
const unsigned int delayCste = 20;
const float ConvertionCste = 1.1011;  // 182/180
int theta = 0;                        // Angle de déphasage

void AdjustAngle(int& angle, int cste){
  /* Impose à l'angle d'être compris entre 0° et 360° */
  angle += cste;
  if(angle >= 0) angle = (angle)%360;
  else           angle = (360+angle)%360;
}

void AngleToUnit(int angle){
  /* Convertit un angle compris entre 0° et 360° en unité */
  if(angle == 0){
    OCR1A = 1;
    OCR1B = 180;
  }else if(angle < 180){
    OCR1A = angle*ConvertionCste;
    OCR1B = 180;
  }else if(angle > 180){
    OCR1A = 180;
    OCR1B = 180 - (angle-180)*ConvertionCste;
  }
}

void SetPhase(){
  /* Stop le timer, effecture le changement d'angle, puis le restore */
  TCCR1B = 0x18;
  TCCR1A = 0x50;

  // Set OCR1A et OCR1B
  AngleToUnit(theta);
  TCNT1=0x0; //0

  TCCR1A = 0xA0;
  TCCR1C = 0xC0;
  TCCR1A = 0x50;

  TCCR1B |= 1;
}

void setup(){
// Init serial monitor
  Serial.begin(500000);
//Init pin
  // Init pin entrés
  pinMode(A5, INPUT_PULLUP); // +
  pinMode(A4, INPUT_PULLUP); // -
  // Init pin sortie
  pinMode(9, OUTPUT);        // CH1
  pinMode(10, OUTPUT);       // CH2


// Génération du signal
  ICR1  = 182-1;
  SetPhase();
}

void loop(){
  delay(delayCste);

  while (Serial.available() ){
    theta = Serial.parseInt();
    Serial.println(theta);
    Serial.read();
  }

  // Connex
  if (digitalRead(A5) == LOW) AdjustAngle(theta, +angleCste); // Rouge
  if (digitalRead(A4) == LOW) AdjustAngle(theta, -angleCste); // Bleu
  
  // Console
  /*
  Serial.println("");
  Serial.print(theta);
  Serial.print(" || ");
  Serial.print(OCR1A);
  Serial.print(" | ");
  Serial.print(OCR1B);
  */

  //
  SetPhase();
}