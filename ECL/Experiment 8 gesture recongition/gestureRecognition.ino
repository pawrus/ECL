#include <Arduino_LSM9DS1.h>
#include <Experiment1_inferencing.h>
void setup() {
  Serial.begin(115200);
  while (!Serial);
  Serial.println("Started");

  if (!IMU.begin()) {
    Serial.println("Failed to initialize IMU!");
    while (1);
  }

  Serial.print("Accelerometer sample rate = ");
  Serial.print(IMU.accelerationSampleRate());
  Serial.println(" Hz\n");

  Serial.println("Motion Classification Running...");
}

void loop() {
  float x, y, z;

  if (IMU.accelerationAvailable()) {
    IMU.readAcceleration(x, y, z);

    float features[] = {x, y, z}; 
    ei::signal_t signal;
    signal.total_length = EI_CLASSIFIER_DSP_INPUT_FRAME_SIZE;
    signal.get_data = [](size_t index, float *value) {
      *value = features[index];
      return EI_IMPULSE_OK;
    };

    ei_impulse_result_t result;
    EI_IMPULSE_ERROR res = run_classifier(&signal, &result, false);

    if (res != EI_IMPULSE_OK) {
      Serial.print("Error running classifier: ");
      Serial.println(res);
      return;
    }

    Serial.print("Prediction: ");
    for (size_t i = 0; i < EI_CLASSIFIER_LABEL_COUNT; i++) {
      Serial.print(result.classification[i].label);
      Serial.print(": ");
      Serial.print(result.classification[i].value, 2);
      Serial.print("  ");
    }
    Serial.println();
  }
}
