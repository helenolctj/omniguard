import ctypes
from ctypes import wintypes
import pycaw.pycaw as pycaw

class OmniGuard:
    def __init__(self):
        self.audio_sessions = pycaw.AudioUtilities.GetAllSessions()
        self.volume_controller = pycaw.AudioUtilities.GetMasterVolumeController()

    def list_applications(self):
        apps = []
        for session in self.audio_sessions:
            app_name = session.Process and session.Process.name() or "Unknown"
            apps.append(app_name)
        return apps

    def set_volume(self, app_name, volume_level):
        for session in self.audio_sessions:
            if session.Process and session.Process.name() == app_name:
                volume = session.SimpleAudioVolume
                volume.SetMasterVolume(volume_level, None)
                print(f"Volume for {app_name} set to {volume_level * 100}%")
                return
        print(f"Application {app_name} not found.")

    def mute_application(self, app_name):
        for session in self.audio_sessions:
            if session.Process and session.Process.name() == app_name:
                volume = session.SimpleAudioVolume
                volume.SetMute(1, None)
                print(f"{app_name} is now muted.")
                return
        print(f"Application {app_name} not found.")

    def unmute_application(self, app_name):
        for session in self.audio_sessions:
            if session.Process and session.Process.name() == app_name:
                volume = session.SimpleAudioVolume
                volume.SetMute(0, None)
                print(f"{app_name} is now unmuted.")
                return
        print(f"Application {app_name} not found.")

if __name__ == "__main__":
    omni_guard = OmniGuard()
    print("Applications with audio sessions:")
    for app in omni_guard.list_applications():
        print(app)

    # Example usage:
    # omni_guard.set_volume("chrome.exe", 0.5)
    # omni_guard.mute_application("chrome.exe")
    # omni_guard.unmute_application("chrome.exe")