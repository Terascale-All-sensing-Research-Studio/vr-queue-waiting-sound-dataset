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

The content stored in each of these 8 CSV files per participant are as follows. Epoch times can be compared to understand the temporal difference between treatments for each participant. Position is provided in meters and rotation is provided as Euler angles in degrees. Euler angle rotations are applied in Z, X, Y order and interpreted as extrinsic rotations. The native Unity coordinate system was used, which is a left-handed system with X pointing to the right, Y pointing up, and Z pointing forward. 

| Filename |	VariableName: Content |
| -------- | -------- |
| EyeGazeLog_NOTIFICATION.csv	| **Timestamp(ns):** Epoch time stamp for when the eye gaze event was recorded.<br> **GameTime:** Game time stamp for when the eye gaze event was recorded.<br>**ObjectName:** Human readable name for the scene object for the eye gaze.<br> **HitPosition:** x, y, and z location of the eye gaze hit location. |
| HeadPositionLog_NOTIFICATION.csv	| **Timestamp(ns):** Epoch time stamp for when the head movement was recorded.<br> **GameTime:** Game time stamp for when the head movement was recorded.<br> **HeadPosition:** x, y, z position of the head.<br> **HeadRotation:** X, Y, and Z rotation of the head.|
| LeftHandLog_NOTIFICATION.csv	| **Timestamp(ns):** Epoch time stamp for when the left hand movement was recorded.<br> **GameTime:** Game time stamp for when the left hand movement was recorded.<br> **LeftHandPosition:** x, y, z position of the left hand.<br> **LeftHandRotation:** X, Y, and Z rotation of the left hand.
| RightHandLog_NOTIFICATION.csv	| **Timestamp(ns):** Epoch time stamp for when the right hand movement was recorded.<br> **GameTime:** Game time stamp for when the right hand movement was recorded.<br> **RightHandPosition:** x, y, z position of the right hand.<br> **RightHandRotation:** X, Y, and Z rotation of the right hand.
| EyeGazeLog_WITHOUT_NOTIFICATION.csv	| **Timestamp(ns):** Epoch time stamp for when the eye gaze event was recorded.<br> **GameTime:** Game time stamp for when the eye gaze event was recorded.<br> **ObjectName:** Human readable name for the scene object for the eye gaze.<br> **HitPosition:** x, y, and z location of the eye gaze hit location.
| HeadPositionLog_WITHOUT_NOTIFICATION.csv	| **Timestamp(ns):** Epoch time stamp for when the head movement was recorded.<br> **GameTime:** Game time stamp for when the head movement was recorded.<br> **HeadPosition:** x, y, z position of the head.<br> **HeadRotation:** X, Y, and Z rotation of the head. |
| LeftHandLog_WITHOUT_NOTIFICATION.csv	| **Timestamp(ns):** Epoch time stamp for when the left hand movement was recorded.<br> **GameTime:** Game time stamp for when the left hand movement was recorded.<br> **LeftHandPosition:** x, y, z position of the left hand.<br> **LeftHandRotation:** X, Y, and Z rotation of the left hand. |
| RightHandLog_WITHOUT_NOTIFICATION.csv	| **Timestamp(ns):** Epoch time stamp for when the right hand movement was recorded.<br> **GameTime:** Game time stamp for when the right hand movement was recorded.<br> **RightHandPosition:** x, y, z position of the right hand.<br> **RightHandRotation:** X, Y, and Z rotation of the right hand. |

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
