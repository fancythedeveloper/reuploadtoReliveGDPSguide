# This will teach you how to convert and reupload levels from 2.1 to 1.0-1.9 on ReliveGDPS, using [gd-level-scripts](https://github.com/qimiko/gd-level-scripts).

## Step 1 - Install Python 3.8+
You only need at least Python 3.8, you're better off just installing the latest version (currently 3.10.6) of Python over at https://www.python.org/downloads/.
#### You can also skip this step if you already have Python 3.8 or higher installed already.

## Step 2 - Download gd-level-scripts
After installing Python, download the repository by clicking on the green button above the files, then click Download ZIP, or you can just use this [link](https://github.com/qimiko/gd-level-scripts/archive/refs/heads/master.zip).

## Step 3 - Extracting and replacing
After downloading the ZIP file, extract the files of it to a folder.
Once you do, go back to *this* repository, and download the httpRequest.py file by clicking on it, then clicking the Raw button (or use this [link](https://raw.githubusercontent.com/fancythedeveloper/reuploadtoReliveGDPSguide/main/httpRequest.py)), and right-clicking and clicking "Save as".
Now just replace the old httpRequest file from the download with the one you just saved.

## Step 3.5 - Modifying (Optional)
If you wanna set it so it actually reuploads to your user account, open up `levelConverter.py` in a text editor, change `unlisted: bool = True` to `unlisted: bool = False`, and change the "udid" from `S-hi-people` to whatever the UDID of your account is, which is in the CCGameManager.dat file. (You can either extract it using `adb backup -f (filename).ab com.drakonx.relivegdpsua` and extracting the .ab file using [ABE](https://github.com/nelenkov/android-backup-extractor/releases/latest) or by directly copying it from `/data/data/com.drakonx.relivegdpsua` if you have a rooted device, I should mention that in 1.0, the file is in plaintext.)

## Step 4 - Actually using it
Now simply open up a command prompt or terminal in the folder that contains the python files, or simply `cd` to it.
Now type `py levelConverter.py --legacy --max-objects X --url "http://relivegdps.x10.mx/database/uploadGJLevel.php" ID` (replace "X" with the max object ID of that version, Eg: 1.0 is 44, 1.1 is 46, 1.2 is 47, etc., and replace "ID" with the level ID of the level you're trying to reupload) and press Enter.

## If it all works, it should give you the ID to the reuploaded level on the GDPS, and if you did Step 3.5, it should be on your user account.
