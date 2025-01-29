import os
import subprocess
import time
import pyttsx3

class TextToSpeech: # Change the voice options here
    def __init__(self):
        self.engine = pyttsx3.init("sapi5")
        voices = self.engine.getProperty("voices")
        self.engine.setProperty("voice", voices[1].id)
        self.engine.setProperty("rate", 170)

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

class Installers:
    def __init__(self, installer_dir):
        self.installer_dir = installer_dir
        self.installers = [
            'Google Chrome.exe', # Add your installers here, one installer per line the 'exe' extension is needed
            
        ]
        self.tts = TextToSpeech()

    def install_program(self, installer):
        installer_path = os.path.join(self.installer_dir, installer)
        if os.path.exists(installer_path):
            self.tts.speak(f"Installing {installer} please confirm...")
            print(f"Installing {installer}...")
            try:
                subprocess.run([installer_path], check=True)
                self.tts.speak(f"{installer} installed successfully.")
                print(f"{installer} installed successfully.")
            except subprocess.CalledProcessError as e:
                self.tts.speak(f"Failed to install {installer}. Error: {e}")
                print(f"Failed to install {installer}. Error: {e}")
        else:
            self.tts.speak(f"Installer {installer} not found in {self.installer_dir}.")
            print(f"Installer {installer} not found in {self.installer_dir}.")

    def install_all(self):
        for installer in self.installers:
            self.install_program(installer)
            time.sleep(5)  # Time between each installer (seconds)
            
if __name__ == "__main__":
    installer_dir = r'' # add you directory here
    installer = Installers(installer_dir)
    installer.install_all()
