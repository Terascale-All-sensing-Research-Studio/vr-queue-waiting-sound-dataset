## Dataset of Perceptions of Waiting in a Virtual Reality (VR) Doctor's Office Receptionist Queue With and Without Notifications on the Reason for a Delay 

## Contents
[Description](#description)

[Contributors](#contributors)

[Overview of Dataset](#overview-of-dataset)

[Directory Tree](#directory-tree)

[Data Dictionary](#data-dictionary)

[Dataset Frame Rate Summary](#dataset-frame-rate-summary)

## Description
The dataset consists of 30 participants standing in queue in a virtual doctor’s office receptionist area designed using Unity 2022.3.9 f1. Each participant stands in the queue for 3-minutes before approaching the virtual receptionist to confirm their doctor’s appointment. Each participant provides data across two treatments, once when the virtual receptionist informs them on why there is a delay and once when the receptionist does not. The reason for the delay is stated as a problem with the virtual receptionist’s computer system. Participants complete both treatments, however, the order of assignment of treatments is randomized. Data is collected from within the VR environment using a Meta Quest Pro. Prior to immersion into the VR environment, participants complete a demographics form and the Frustration Discomfort Scale. After each treatment, participants answer a 3-question survey on the length of delay, their frustration at the delay measured on a 5-point Likert scale, and their likelihood to exit due to the delay, also measured on a 5-point Likert scale. After both treatments, participants complete a second Frustration Discomfort Scale as well as the NASA Task Load Index, System Usability Scale, and Virtual Reality Sickness Questionnaire. Each participant provides data in a single session lasting 1-hour. For each participant we recorded: eye gaze hit locations, objects viewed per timestamp based on the gaze ray intersections with scene objects, headset position and orientation, and left and right hand position and orientation.   

## Contributors
Elza Ibragimov, Natasha Kholgade Banerjee, Sean Banerjee, Ashutosh Shivakumar

[Terascale All-sensing Research Studio](https://tars-home.github.io)

## Overview of Dataset
The dataset is organized into the following folders:

| FolderName |	SubFolders |	DataType |	Contents |
| ------------- | ------------- | ------------- | ------------- |
| [Assets](https://github.com/Terascale-All-sensing-Research-Studio/vr-queue-waiting-sound-dataset/blob/main/Assets/) | Yes | MP3 | Contains two subfolders, namely [No_Sound_Audio_Files](https://github.com/Terascale-All-sensing-Research-Studio/vr-queue-waiting-sound-dataset/blob/main/Assets/No_Sound_Audio_Files) and [Sound_Audio_Files](https://github.com/Terascale-All-sensing-Research-Studio/vr-queue-waiting-sound-dataset/blob/main/Assets/Sound_Audio_Files). The folder [Sound_Audio_Files](https://github.com/Terascale-All-sensing-Research-Studio/vr-queue-waiting-sound-dataset/blob/main/Assets/Sound_Audio_Files) contains all the audio assets in MP3 format for the With Notification treatment. The folder [No_Sound_Audio_Files](https://github.com/Terascale-All-sensing-Research-Studio/vr-queue-waiting-sound-dataset/blob/main/Assets/No_Sound_Audio_Files) contains all the audio assets in MP3 format for the Without Notification treatment. The audio files are generated using [ElevenLabs](https://elevenlabs.io/). 
| [Cybersickness](https://github.com/Terascale-All-sensing-Research-Studio/vr-queue-waiting-sound-dataset/blob/main/Cybersickness/) |	None |	CSV	| Participant responses to the standard Virtual Reality Sickness Questionnaire (VRSQ) are stored in a single CSV file called [cybersickness.csv](https://github.com/Terascale-All-sensing-Research-Studio/vr-queue-waiting-sound-dataset/blob/main/Cybersickness/cybersickness.csv). Each participant is assigned a unique 5-character ID. |
| [Demographics](https://github.com/Terascale-All-sensing-Research-Studio/vr-queue-waiting-sound-dataset/blob/main/Demographics/) |	None |	CSV	| Participant demographics consisting of: age, ethnicity, race, self-identified gender, education level, whether they wear glasses, if the glasses are worn for reading, if they wear contacts, how frequently they play video games, what type of video games they play, how frequently they use VR, if they own a VR device, what type of VR devices they use, how frequently they use telehealth services, and what telehealth services they use are stored in a single CSV file called [demographics.csv](https://github.com/Terascale-All-sensing-Research-Studio/vr-queue-waiting-sound-dataset/blob/main/Demographics/demographics.csv). Each participant is assigned a unique 5-character ID. |
| [FDS](https://github.com/Terascale-All-sensing-Research-Studio/vr-queue-waiting-sound-dataset/blob/main/FDS/)	| None |	CSV |	Participant responses to the standard Frustration Discomfort Scale (FDS). The CSV files are called [pre_fds.csv](https://github.com/Terascale-All-sensing-Research-Studio/vr-queue-waiting-sound-dataset/blob/main/FDS/pre_fds.csv) and [post_fds.csv](https://github.com/Terascale-All-sensing-Research-Studio/vr-queue-waiting-sound-dataset/blob/main/FDS/post_fds.csv) to indicate that they were administered prior to and after the immersion. Each participant is assigned a unique 5-character ID. |
| [NASA_TLX](https://github.com/Terascale-All-sensing-Research-Studio/vr-queue-waiting-sound-dataset/blob/main/NASA_TLX/) |	None |	CSV	| Participant responses to the standard 21-tick NASA Task Load Index (TLX) are stored in a single CSV file called [nasatlx.csv](https://github.com/Terascale-All-sensing-Research-Studio/vr-queue-waiting-sound-dataset/blob/main/NASA_TLX/nasatlx.csv). Each participant is assigned a unique 5-character ID. |
| [SUS](https://github.com/Terascale-All-sensing-Research-Studio/vr-queue-waiting-sound-dataset/blob/main/SUS/)	| None |	CSV	| Participant responses to the standard System Usability Scale (SUS) are stored in a single CSV file called [sus.csv](https://github.com/Terascale-All-sensing-Research-Studio/vr-queue-waiting-sound-dataset/blob/main/SUS/sus.csv). Each participant is assigned a unique 5-character ID. |
| [TreatmentResponses](https://github.com/Terascale-All-sensing-Research-Studio/vr-queue-waiting-sound-dataset/blob/main/TreatmentResponses/) |	None |	CSV	| Participant responses to each treatment, i.e., being notified about the reason for the wait (With_Notification) or not being notified about the reason (Without_Notification). Participant responses include their time estimate for the wait in minutes, their frustration level on a 5-point Likert scale (1 being lowest and 5 highest), and their likelihood to exit on a 5-point Likert scale and are stored in a single CSV file called [TreatmentResponses.csv](https://github.com/Terascale-All-sensing-Research-Studio/vr-queue-waiting-sound-dataset/blob/main/TreatmentResponses/TreatmentResponses.csv). Each participant is assigned a unique 5-character ID.
| [VRData](https://github.com/Terascale-All-sensing-Research-Studio/vr-queue-waiting-sound-dataset/blob/main/VRData/)	| Yes	| CSV	| Contains 30 subfolders that represents each participant. Each subfolder is named with the unique 5-character ID. Within each participant subfolder there are two additional subfolders named ParticipantID_NOFICATION and ParticipantID_WITHOUT_NOTIFICATION. Here Participant_ID is the unique 5-character ID and NOTIFICATION and WITHOUT_NOTIFICATION indicates that the participant was and was not informed about the reason for the delay respectively. Within the ParticipantID_NOFICATION and ParticipantID_WITHOUT_NOTIFICATION subfolders are four CSV files for Eye Gaze (EyeGazeLog), Head Position and Orientation (HeadPosition), Left Hand (LeftHandLog), and Right Hand (RightHandLog). Thus, each participant has 8 CSV files. |

## Directory Tree
We provide the directory tree below for the entire repository and the tree for one example participant (0GR0B) in the VRData folder:

```
├── Assets/
│   ├── No_Sound_Audio_Files/
│   │   ├── Keyboard.mp3
│   │   ├── MaleNPC_Mhhm.mp3
│   │   ├── MaleNPC_Ok.mp3
│   │   ├── Recep_CheckedInOnline.mp3
│   │   ├── Recep_Hello.mp3
│   │   └── Recep_IWillBeHelpingYou.mp3
│   ├── Sound_Audio_Files/
│   │   ├── Keyboard.mp3
│   │   ├── MaleNPC_Mhhm.mp3
│   │   ├── MaleNPC_Ok.mp3
│   │   ├── Recep_CheckedInOnline.mp3
│   │   ├── Recep_Hello.mp3
│   │   ├── Recep_IWillBeHelpingYou.mp3
│   │   ├── Recep_OneMoment.mp3
│   │   ├── Recep_SystemIsSlow.mp3
│   │   └── Recep_WithYouShortly.mp3
│   └── README.md
├── Cybersickness/
│   ├── cybersickness.csv
│   └── README.md
├── Demographics/
│   ├── demographics.csv
│   └── README.md
├── FDS/
│   ├── post_fds.csv
│   ├── pre_fds.csv
│   └── README.md
├── NASA_TLX/
│   ├── nasatlx.csv
│   └── README.md
├── SUS/
│   ├── README.md
│   └── sus.csv
├── TreatmentResponses/
│   ├── README.md
│   └── TreatmentResponses.csv
├── VRData/
│   ├── 0GR0B/
│   │   ├── 0GR0B_NOTIFICATION/
│   │   │   ├── EyeGazeLog_NOTIFICATION.csv
│   │   │   ├── HeadPositionLog_NOTIFICATION.csv
│   │   │   ├── LeftHandLog_NOTIFICATION.csv
│   │   │   └── RightHandLog_NOTIFICATION.csv
│   │   └── 0GR0B_WITHOUT_NOTIFICATION/
│   │       ├── EyeGazeLog_WITHOUT_NOTIFICATION.csv
│   │       ├── HeadPositionLog_WITHOUT_NOTIFICATION.csv
│   │       ├── LeftHandLog_WITHOUT_NOTIFICATION.csv
│   │       └── RightHandLog_WITHOUT_NOTIFICATION.csv
│   └── README.md
├── dictionary.csv
├── LICENSE
├── README.md
└── vrdata_frame_summary.py
```
## Data Dictionary
The file [dictionary.csv](https://github.com/Terascale-All-sensing-Research-Studio/vr-queue-waiting-sound-dataset/blob/main/dictionary.csv) provides a summary of the data found in the following CSV files in our dataset: 
* [Cybersickess/cybersickness.csv](https://github.com/Terascale-All-sensing-Research-Studio/vr-queue-waiting-sound-dataset/blob/main/Cybersickness/cybersickness.csv)
* [Demographics/demographics.csv](https://github.com/Terascale-All-sensing-Research-Studio/vr-queue-waiting-sound-dataset/blob/main/Demographics/demographics.csv)
* [FDS/pre_fds.csv](https://github.com/Terascale-All-sensing-Research-Studio/vr-queue-waiting-sound-dataset/blob/main/FDS/pre_fds.csv)
* [FDS/post_fds.csv](https://github.com/Terascale-All-sensing-Research-Studio/vr-queue-waiting-sound-dataset/blob/main/FDS/post_fds.csv)
* [NASA_TLX/nasatlx.csv](https://github.com/Terascale-All-sensing-Research-Studio/vr-queue-waiting-sound-dataset/blob/main/NASA_TLX/nasatlx.csv)
* [SUS/sus.csv](https://github.com/Terascale-All-sensing-Research-Studio/vr-queue-waiting-sound-dataset/blob/main/SUS/sus.csv)
* [TreatmentResponses/TreatmentResponses.csv](https://github.com/Terascale-All-sensing-Research-Studio/vr-queue-waiting-sound-dataset/blob/main/TreatmentResponses/TreatmentResponses.csv)

The file contains the following information:

| Column | Description |
| ------ | ----------- |
| Directory/FileName | Provides the directory and filename, e.g., Demographics/demographics.csv |
| ColumnName | Provides the column name in the file being referenced in Directory/FileName, e.g., Participant ID |
| Value | Provides detailed information of the value stored in ColumnName, e.g., Unique 5-character ID assigned to each participant |

## Dataset Frame Rate Summary
The minimum (Min), maximum (Max), and average (Mean) frame rate, as frames per second, for the head, eye gaze, right hand, and left hand for our dataset are provided below. The table below is generated by running the Python script [vrdata_frame_summary.py](https://github.com/Terascale-All-sensing-Research-Studio/vr-queue-waiting-sound-dataset/blob/main/waitSummary.py) over the [VRData](https://github.com/Terascale-All-sensing-Research-Studio/vr-queue-waiting-sound-dataset/blob/main/VRData) folder. 

| Treatment | Type of Data | Min | Max | Mean | SD |
| ----- | ----- | ----- | ----- | ----- | ----- |
| With Notification |	Head | 67.54 | 73.87 | 71.11 | 0.96 |
| |	Eye Gaze | 66.32 | 73.14 | 70.59 | 1.2 |
| | Right Hand | 67.54 | 73.87 | 71.12 | 0.97 | 
| | Left Hand | 67.54 | 73.87 | 71.12 | 0.97 |
| Without Notification	| Head | 70.07 | 72.50 | 71.08 | 0.43
| | Eye Gaze | 68.96 | 71.37 | 70.56 | 0.62 | 
| | Right Hand | 70.06 | 72.50 | 71.10 | 0.43 | 
| |	Left Hand | 70.06 | 72.50 | 71.10 | 0.43 | 
