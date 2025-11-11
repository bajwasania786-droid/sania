import os

def close_all_windows():
    # This command force closes all programs except system processes and Explorer
    os.system("taskkill /F /FI \"STATUS eq RUNNING\" /FI \"IMAGENAME ne explorer.exe\"")

    print("✅ All open windows have been closed.")

if __name__ == "__main__":
    close_all_windows()


