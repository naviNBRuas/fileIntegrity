'''
Integrity Checker
This file contains the IntegrityChecker class which is responsible for scanning and verifying the integrity of system files.
'''
import hashlib
import os
class IntegrityChecker:
    def __init__(self):
        self.database = {
            "file1.txt": "a94a8fe5ccb19ba61c4c0873d391e987982fbbd3",
            "file2.txt": "6dcd4ce23d88e2ee9568ba546c007c63d9131c1b",
            "file3.txt": "d41d8cd98f00b204e9800998ecf8427e"
        }
    def scan_files(self):
        '''
        Scan the system files and compare their hashes with the expected values.
        Return a list of alerts for any discrepancies found.
        '''
        alerts = []
        for filename, expected_hash in self.database.items():
            if not os.path.isfile(filename):
                alerts.append(f"File not found: {filename}")
                continue
            actual_hash = self.calculate_hash(filename)
            if actual_hash != expected_hash:
                alerts.append(f"File modified: {filename}")
        return alerts
    def calculate_hash(self, filename):
        '''
        Calculate the hash of a file using the SHA-1 algorithm.
        '''
        hasher = hashlib.sha1()
        with open(filename, "rb") as file:
            while True:
                data = file.read(4096)
                if not data:
                    break
                hasher.update(data)
        return hasher.hexdigest()