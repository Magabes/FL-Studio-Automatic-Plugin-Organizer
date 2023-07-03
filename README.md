This script is a tool to organize **FL Studio** plugins by vendor name (Eventide, Roland, Korg, Arturia, etc.) It copies the plugin files from the default installation folder to a user-defined folder (or one I made that is easily accessible), creating subfolders for each company/distributor.


**Requirements**

- Python 3.11.4 or higher
- FL Studio (any version, I think) installed on Windows (Tested and made on Windows 10 64-bit)


**TO-DO**: Make sure it's not only compatible for the C: Drive.


organizeEffects.py or organizeGenerators.py

**Default installation** - C:\Users\USERNAME\Documents\Image-Line\FL Studio\Presets\Plugin database\Installed\Effects\New 

**or** 

C:\Users\USERNAME\Documents\Image-Line\FL Studio\Presets\Plugin database\Installed\Generators\New


**USERNAME** in the folder paths _should_ automatically be set to your Windows username. if not, run the **CUSTOM** scripts.

organizeEffectsCUSTOM.py or organizeGeneratorsCUSTOM.py - You choose both paths.

- Results for the default scripts -
C:\Users\USERNAMEl\Documents\Image-Line\FL Studio\Presets\Plugin database\Effects\USER\ [COMPANY] (Such as Waves)

or

C:\Users\USERNAME\Documents\Image-Line\FL Studio\Presets\Plugin database\Generators\USER\ [COMPANY] (Such as Roland)


**BEFORE RUNNING ANY OF THE PYTHON SCRIPTS**

Once you're done with the steps below, you might see some Fruity plugins on the New folder. 
Just delete them. Most of them start with 'Fruity'; should be easy to spot.

![Screenshot_262](https://github.com/Magabes/FL-Studio-Automatic-Plugin-Organizer/assets/90144228/51fcb389-2149-4e71-b40b-65bd48920aa6)

![Image](https://user-images.githubusercontent.com/90144228/250405164-f7ed76cf-6bae-4df3-82e9-17b6d5db599b.png)


**EXAMPLE OF HOW IT'LL LOOK**

![Screenshot_264](https://github.com/Magabes/FL-Studio-Automatic-Plugin-Organizer/assets/90144228/697d62fa-220c-4220-9794-d31b4daa4227)

![Screenshot_265](https://github.com/Magabes/FL-Studio-Automatic-Plugin-Organizer/assets/90144228/7681a2db-1541-4d35-914a-23f341b2c5d8)

![Screenshot_269](https://github.com/Magabes/FL-Studio-Automatic-Plugin-Organizer/assets/90144228/3010a934-c753-48bb-ab1f-891124f453bd)



