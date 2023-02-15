import subprocess
import dotenv
import os

from src.analyze_packet import packet_capture;

def main():
    dotenv.load_dotenv()
    print("Firefox起動 with SSLKEYLOGFILE")
    open_firefox()
    packet_capture()

def open_firefox():
    command = f".\\firefox.exe {os.getenv('TENHOU_URL')}"
    os.environ["SSLKEYLOGFILE"] = os.path.abspath(os.getenv("SSLKEYLOGFILE"))
    subprocess.Popen(command, cwd=os.path.abspath(os.getenv('FIREFOXEXE_PATH')), shell=True)


if __name__=="__main__":
    main()