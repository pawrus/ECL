#include <EdgeImpulseModel.h>
export
#include <Arduino_LSM9DS1.h>
void setup() {
Serial.begin(115200);
if (!IMU.begin()) {
Serial.println("Failed to initialize IMU!");
while (1);
}
}
void loop() {
float buffer[EI_CLASSIFIER_DSP_INPUT_FRAME_SIZE];
for (int i = 0; i < EI_CLASSIFIER_DSP_INPUT_FRAME_SIZE; i++) {
buffer[i] = analogRead(A0);
}
ei_impulse_result_t result = { 0 };
signal_t signal;
numpy::signal_from_buffer(buffer, EI_CLASSIFIER_DSP_INPUT_FRAME_SIZE,
&signal);
EI_IMPULSE_ERROR res = run_classifier(&signal, &result, false);
if (res != EI_IMPULSE_OK) {
Serial.print("ERR: Failed to run classifier ");
Serial.println(res);
return;
}
for (size_t ix = 0; ix < EI_CLASSIFIER_LABEL_COUNT; ix++) {
Serial.print(result.classification[ix].label);
Serial.print(": ");
Serial.println(result.classification[ix].value);
}
delay(1000);
}