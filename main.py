#!/usr/bin/env python3
"""
Quantum Quirk Forensic Analyzer
Main Entry Point

Team Quantum Quirk — SIH 2026
"""

import sys
import os

def main():
    print("""
    ╔═══════════════════════════════════════════════════════════╗
    ║         🔍 Quantum Quirk Forensic Analyzer               ║
    ║                                                          ║
    ║   Unlocking Digital Evidence — One Frame at a Time      ║
    ║                                                          ║
    ║   Precision. Integrity. Justice.                         ║
    ╚═══════════════════════════════════════════════════════════╝
    """)
    
    print("Loading Quantum Quirk Forensic Analyzer...")
    
    try:
        # Import GUI module
        from src.gui.main_window import MainWindow
        from PyQt5.QtWidgets import QApplication
        
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())
        
    except ImportError as e:
        print(f"Error: Missing dependencies: {e}")
        print("\nPlease install required packages:")
        print("pip install -r requirements.txt")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
