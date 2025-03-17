# Integrity Checker User Manual

## Introduction
The Integrity Checker is a security tool designed to ensure the integrity and security of system files in an operating system. It verifies the integrity of system files by comparing their hashes or checksums against a trusted database. The tool regularly scans the operating system files and provides real-time alerts and notifications for any unauthorized modifications or tampering detected.

## Installation
To use the Integrity Checker, you need to have Python installed on your system. Follow the steps below to install the necessary dependencies and set up the environment:

1. Open a terminal or command prompt.
2. Navigate to the directory where the Integrity Checker code is located.
3. Run the following command to install the required dependencies:

```
pip install -r requirements.txt
```

## Usage
Once you have installed the necessary dependencies, you can use the Integrity Checker by following these steps:

1. Open a terminal or command prompt.
2. Navigate to the directory where the Integrity Checker code is located.
3. Run the following command to start the application:

```
python main.py
```

4. The Integrity Checker application window will open.
5. Click on the "Scan" button to initiate the file scanning process.
6. The application will compare the hashes of the system files with the expected values in the trusted database.
7. Any discrepancies or unauthorized modifications will be displayed in the alert text box.
8. Take immediate action based on the alerts to ensure the integrity and security of the system files.

## Customization
The Integrity Checker currently uses a predefined database of file hashes for demonstration purposes. If you want to customize the trusted database, you can modify the `integrity_checker.py` file and update the `self.database` dictionary with your own file names and hashes.

## Conclusion
The Integrity Checker provides a simple and effective way to ensure the integrity and security of system files in an operating system. By regularly scanning the files and comparing their hashes with a trusted database, the tool helps detect any unauthorized modifications or tampering. The real-time alerts and notifications enable administrators or users to take immediate action to maintain the integrity of the system.