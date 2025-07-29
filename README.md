# You_can_write_what_you_want
Instructions and script to create texture-text

This instruction will allow you to create a text texture on a white background. Created to work with 3D models, in particular https://skfb.ly/pyOJC

Windows
1) download the script gen_text_texture(jpeg).py
2) Install Python from https://www.python.org/downloads/windows/
3) in the command line (Win+R, cmd - you may have to open it with administrator rights) with the command "where python" find out the path to the installed version. The path should contain the Python folder
4) Enter the following commands: "path/python.exe" -m pip install --upgrade pip

"path/python.exe" -m pip install Pillow
6) Create a label.txt file in the folder with the script and write the text for the texture. It can be in several lines.
7) Open the command line in the same folder and enter:
"path/python.exe" gen_text_texture(jpeg).py
8) Replace the old texture in the required model with the resulting text_tex.jpg texture.

Note: If the model was imported into the editor or game engine BEFORE updating the texture, the model must be imported again.
