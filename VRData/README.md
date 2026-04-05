# VR Data

Our study consisted of two treatments: 
1.	With Notification: In this treatment the participant is informed by the virtual receptionist that there is a problem with the computer system, therefore providing an explanation of the wait. 
2.	Without Notification: In this treatment, the virtual receptionist does not inform the participant on why there is a delay.   

Each of the 30 folders here represents a single participant. The folder is named with a unique 5-character ID assigned to each participant. Within each of these 30 folders there are two subfolders named ParticipantID_NOTIFICATION and ParticipantID_WITHOUT_NOTIFICATION. Here, ParticipantID is the 5-character ID assigned to each participant and NOTIFICATION and WITHOUT_NOTIFICATION indicates whether the participant was informed by the virtual receptionist on the reason for the delay. Within the NOTIFICATION and WITHOUT_NOTIFICATION sub-subfolders are 4 raw CSV files, for a total of 8 raw CSV files per participant. The names and locations of each of these 8 CSV files are as follows:

| Filename |	Location |
| -------- | -------- |
| EyeGazeLog_NOTIFICATION.csv	| ParticipantID/ParticipantID_NOTIFICATION |
| HeadPositionLog_NOTIFICATION.csv	| ParticipantID/ParticipantID_NOTIFICATION |
| LeftHandLog_NOTIFICATION.csv	| ParticipantID/ParticipantID_NOTIFICATION | 
| RightHandLog_NOTIFICATION.csv	| ParticipantID/ParticipantID_NOTIFICATION |
| EyeGazeLog_WITHOUT_NOTIFICATION.csv	| ParticipantID/ParticipantID_WITHOUT_NOTIFICATION |
| HeadPositionLog_ WITHOUT_NOTIFICATION.csv	| ParticipantID/ParticipantID_WITHOUT_NOTIFICATION |
| LeftHandLog_ WITHOUT_NOTIFICATION.csv	| ParticipantID/ParticipantID_WITHOUT_NOTIFICATION |
| RightHandLog_ WITHOUT_NOTIFICATION.csv	| ParticipantID/ParticipantID_WITHOUT_NOTIFICATION |

The content stored in each of these 8 CSV files per participant are as follows. Position is provided in meters and rotation is provided as Euler angles in degrees. Unity applies Euler angle rotations in Z, X, Y order and the rotations are interpreted as extrinsic rotations. The native Unity coordinate system was used, which is a left-handed system with X pointing to the right, Y pointing up, and Z pointing forward. 

| Filename |	VariableName: Content |
| -------- | -------- |
| EyeGazeLog_NOTIFICATION.csv	| **Timestamp(ns):** System.Diagnostics.Stopwatch time stamp for when the eye gaze event was recorded. Divide by 1E+09 and add to the system and treatment epoch time to get the epoch time stamp for when the eye gaze event was recorded.<br> **GameTime:** Game time stamp for when the eye gaze event was recorded.<br>**ObjectName:** Human readable name for the scene object for the eye gaze.<br> **HitPosition:** x, y, and z location of the eye gaze hit location. |
| HeadPositionLog_NOTIFICATION.csv	| **Timestamp(ns):** System.Diagnostics.Stopwatch time stamp for when the head movement was recorded. Divide by 1E+09 and add to the system and treatment epoch time to get the epoch time stamp for when the head movement was recorded.<br> **GameTime:** Game time stamp for when the head movement was recorded.<br> **HeadPosition:** x, y, z position of the head.<br> **HeadRotation:** X, Y, and Z rotation of the head.|
| LeftHandLog_NOTIFICATION.csv	| **Timestamp(ns):** System.Diagnostics.Stopwatch time stamp for when the left hand movement was recorded. Divide by 1E+09 and add to the system and treatment epoch time to get the epoch time stamp for when the left hand movement was recorded.<br> **GameTime:** Game time stamp for when the left hand movement was recorded.<br> **LeftHandPosition:** x, y, z position of the left hand.<br> **LeftHandRotation:** X, Y, and Z rotation of the left hand.
| RightHandLog_NOTIFICATION.csv	| **Timestamp(ns):** System.Diagnostics.Stopwatch time stamp for when the right hand movement was recorded. Divide by 1E+09 and add to the system and treatment epoch time to get the epoch time stamp for when the right hand movement was recorded.<br> **GameTime:** Game time stamp for when the right hand movement was recorded.<br> **RightHandPosition:** x, y, z position of the right hand.<br> **RightHandRotation:** X, Y, and Z rotation of the right hand.
| EyeGazeLog_WITHOUT_NOTIFICATION.csv	| **Timestamp(ns):** System.Diagnostics.Stopwatch time stamp for when the eye gaze event was recorded. Divide by 1E+09 and add to the system and treatment epoch time to get the epoch time stamp for when the eye gaze event was recorded.<br> **GameTime:** Game time stamp for when the eye gaze event was recorded.<br> **ObjectName:** Human readable name for the scene object for the eye gaze.<br> **HitPosition:** x, y, and z location of the eye gaze hit location.
| HeadPositionLog_WITHOUT_NOTIFICATION.csv	| **Timestamp(ns):** System.Diagnostics.Stopwatch time stamp for when the head movement was recorded. Divide by 1E+09 and add to the system and treatment epoch time to get the epoch time stamp for when the head movement was recorded.<br> **GameTime:** Game time stamp for when the head movement was recorded.<br> **HeadPosition:** x, y, z position of the head.<br> **HeadRotation:** X, Y, and Z rotation of the head. |
| LeftHandLog_WITHOUT_NOTIFICATION.csv	| **Timestamp(ns):** System.Diagnostics.Stopwatch time stamp for when the left hand movement was recorded. Divide by 1E+09 and add to the system and treatment epoch time to get the epoch time stamp for when the left hand movement was recorded.<br> **GameTime:** Game time stamp for when the left hand movement was recorded.<br> **LeftHandPosition:** x, y, z position of the left hand.<br> **LeftHandRotation:** X, Y, and Z rotation of the left hand. |
| RightHandLog_WITHOUT_NOTIFICATION.csv	| **Timestamp(ns):** System.Diagnostics.Stopwatch time stamp for when the right hand movement was recorded. Divide by 1E+09 and add to the system and treatment epoch time to get the epoch time stamp for when the right hand movement was recorded.<br> **GameTime:** Game time stamp for when the right hand movement was recorded.<br> **RightHandPosition:** x, y, z position of the right hand.<br> **RightHandRotation:** X, Y, and Z rotation of the right hand. |

We provide the directory tree below for one example participant (0GR0B):

```
VRData/
    ├── 0GR0B/
        ├── 0GR0B_NOTIFICATION/
            ├── EyeGazeLog_NOTIFICATION.csv
            ├── HeadPositionLog_NOTIFICATION.csv
            ├── LeftHandLog_NOTIFICATION.csv
            └── RightHandLog_NOTIFICATION.csv
        └── 0GR0B_WITHOUT_NOTIFICATION/
            ├── EyeGazeLog_WITHOUT_NOTIFICATION.csv
            ├── HeadPositionLog_WITHOUT_NOTIFICATION.csv
            ├── LeftHandLog_WITHOUT_NOTIFICATION.csv
            └── RightHandLog_WITHOUT_NOTIFICATION.csv
```
We provide epoch start times for each participant's session and treatment to enable participant to participant comparisions. The table below is provided in ascending order of epoch time. 

| Participant ID | Treatment | Epoch Time |
| ------- | ------- | ------- |
| 874GE | Without_Notification | 	1755029186 | 
| 874GE | With_Notification | 1755029512 | 
| 6FERM | Without_Notification | 1755264991 | 
| 6FERM | With_Notification | 1755265365 | 
| K8VKZ | With_Notification | 1755544705 | 
| K8VKZ | Without_Notification | 1755545079 | 
| GR7GM | Without_Notification | 1755619757 | 
| GR7GM | With_Notification | 1755620302 | 
| D7DLR | Without_Notification | 1755785704 | 
| D7DLR | With_Notification | 1755786022 | 
| 0GR0B | With_Notification | 1755799026 | 
| 0GR0B | Without_Notification | 1755799396 | 
| 57GEO | With_Notification | 1755804011 | 
| 57GEO | Without_Notification | 1755804370 | 
| GFD02 | With_Notification | 1755805519 | 
| GFD02 | Without_Notification | 1755805914 | 
| 7Q5SI | Without_Notification | 1755886247 | 
| 7Q5SI | With_Notification | 1755886677 | 
| C9KBG | Without_Notification | 1755890395 | 
| C9KBG | With_Notification | 1755890912 | 
| H2IIY | Without_Notification | 1755893044 | 
| H2IIY | With_Notification | 1755893553 | 
| 7MEOE | Without_Notification | 1755896254 | 
| 7MEOE | With_Notification | 1755896574 | 
| POPC4 | With_Notification | 1756124030 | 
| POPC4 | Without_Notification | 1756124433 | 
| 1BX2A | With_Notification | 1756130060 | 
| 1BX2A | Without_Notification | 1756130635 | 
| 858OK | Without_Notification | 1756132015 | 
| 858OK | With_Notification | 1756132479 | 
| Z3TFO | With_Notification | 1756134950 | 
| Z3TFO | Without_Notification | 1756135474 | 
| H75VY | With_Notification | 1756137866 | 
| H75VY | Without_Notification | 1756138411 | 
| CHOBY | Without_Notification | 1756145221 | 
| CHOBY | With_Notification | 1756145610 | 
| F483S | Without_Notification | 1756153019 | 
| F483S | With_Notification | 1756153421 | 
| DZDMH | With_Notification | 1756217625 | 
| DZDMH | Without_Notification | 1756217983 | 
| IX4SL | With_Notification | 1756233111 | 
| IX4SL | Without_Notification | 1756233409 | 
| CUZPT | Without_Notification | 1756234400 | 
| CUZPT | With_Notification | 1756234771 | 
| ZU2PA | With_Notification | 1756235905 | 
| ZU2PA | Without_Notification | 1756236298 | 
| OSPOJ | Without_Notification | 1756299798 | 
| OSPOJ | With_Notification | 1756300182 | 
| I7NPK | With_Notification | 1756308831 | 
| I7NPK | Without_Notification | 1756309296 | 
| SN6KG | With_Notification | 1756312122 | 
| SN6KG | Without_Notification | 1756312511 | 
| W44U7 | Without_Notification | 1756314385 | 
| W44U7 | With_Notification | 1756314979 | 
| C2466 | Without_Notification | 1756316449 | 
| C2466 | With_Notification | 1756316849 | 
| 8F4IJ | With_Notification | 1756318492 | 
| 8F4IJ | Without_Notification | 1756318904 | 
| FFB9O | With_Notification | 1756322297 | 
| FFB9O	| Without_Notification | 1756322842 | 
