# VOCALYZE
Vocalyze is python Machine learning model designed for AI and Audio engineers to easily filter out vocal melodies from background instrumentals. This is incredibly useful in music production for audio sampling. It is further effective for preparing melody datasets used in melody generation AI technology. Other applications include speech denoising, and voice recognition

# How it works
An initial model first identifies the vocal regions(parts containing voice) of the input signal. A second model/algorithm then predicts the various frequencies present in the voice regions hence predicting the vocal melody. See <b>TRAINING DETAILS.ipynb</b> for an indepth explanation. 


# Features
- [x] Key Detection
- [x] Denoising capability
- [x] Voice Detection
- [x] Vocal Melody Extraction
- [x] Piano Melody


# Core Requirements
* Librosa - Requires FFmpeg to run. Simply use ```pip install librosa```  to get librosa
* FFmpeg - Most PCs come with ffmpeg preinstalled. You can install it here if you don't already have it

# Project Setup
- Clone this repo, activate the virtual environment and install the requirements. Make sure you have Python 3.7+ installed 
```git clone git@github.com:logic-ot/vocalyze.git```

- Create and activate a virtual environment for the requirements of your project. 
```
virtualenv myenv
myenv\scripts\activate    
pip install -r requirements.txt
```

- Now you can import Vocalyze from which ever directory it's in and begin <b>Vocalyzing</b>
```from {a directory}.Vocalyze import vocalyze```



