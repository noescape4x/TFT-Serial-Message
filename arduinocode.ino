#include <Adafruit_GFX.h>    
#include <Adafruit_ST7735.h> 
#include <SPI.h>

#define TFT_CS    10
#define TFT_RST   8  
#define TFT_DC    9 

#define TFT_SCLK 13   
#define TFT_MOSI 11   

Adafruit_ST7735 tft = Adafruit_ST7735(TFT_CS, TFT_DC, TFT_MOSI, TFT_SCLK, TFT_RST);

void setup(void) {
  Serial.begin(9600);
  tft.initR(INITR_BLACKTAB);  
  tft.fillScreen(ST7735_BLACK);
  tft.setRotation(3);
 
  tft.setTextColor(ST7735_WHITE);
  tft.setTextSize(1.5);
  tft.setCursor(20, 50);
  tft.println("   Welcome back!");  
}

void loop() {
  if (Serial.available()) {
    String message = Serial.readStringUntil('\n');
    tft.fillScreen(ST7735_BLACK); 
    tft.setTextColor(ST7735_YELLOW);
    tft.setTextSize(2);
    tft.setCursor(10, 40);
    tft.println(message);  
  }
}
