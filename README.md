# OmniGuard

OmniGuard is a Python application designed to dynamically control audio volumes across various applications on Windows. It allows users to list active audio sessions, set specific volumes for applications, and mute/unmute applications.

## Features

- List all applications currently having an audio session.
- Set volume levels for specific applications.
- Mute and unmute applications.

## Prerequisites

- Python 3.x
- Windows Operating System
- `pycaw` library

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/omniguard.git
    ```

2. Navigate into the directory:
    ```bash
    cd omniguard
    ```

3. Install the required package:
    ```bash
    pip install pycaw
    ```

## Usage

1. Run the `omniguard.py` script:
    ```bash
    python omniguard.py
    ```

2. The script will list all the applications currently having an audio session.

3. Example usage within the script:
    ```python
    omni_guard.set_volume("chrome.exe", 0.5)  # Sets the volume of Chrome to 50%
    omni_guard.mute_application("chrome.exe")  # Mutes Chrome
    omni_guard.unmute_application("chrome.exe")  # Unmutes Chrome
    ```

## Notes

- The application names are case-sensitive and should match the process names as they appear in the task manager.
- Ensure you have the appropriate permissions to control audio sessions.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This tool leverages the `pycaw` library for interacting with the Windows Core Audio APIs.