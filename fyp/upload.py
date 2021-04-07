from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
drive = GoogleDrive(gauth)


def upload_file(file_name):
    gfile = drive.CreateFile(
        {
            "parents": [
                {
                    "id": "1R59F10zZ09rjchcuqSlEZgzFLsLamIN9",
                }
            ]
        }
    )
    # Read file and set it as the content of this instance.
    gfile.SetContentFile(f"{file_name}.png")
    gfile.Upload(param={"supportsTeamDrives": True})  # Upload the file.


files = [
    "a",
]
for file in files:
    upload_file(file)