import os
from os.path import exists


def cleanup() -> int:
    """Deletes all temporary assets in assets/temp

    Returns:
        int: How many files were deleted
    """
    if not exists("./assets/temp"):
        return 0
    files = [f for f in os.listdir(".") if f.endswith(".mp4") and "temp" in f.lower()]
    count = 0 + len(files)
    for f in files:
        os.remove(f)
    try:
        for file in os.listdir("./assets/temp/mp4"):
            count += 1
            os.remove(f"./assets/temp/mp4/{file}")
    except FileNotFoundError:
        pass
    for file in os.listdir("./assets/temp/mp3"):
        count += 1
        os.remove(f"./assets/temp/mp3/{file}")
    return count
