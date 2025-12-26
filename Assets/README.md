# Assets

Our study consisted of two treatments: 
1.	With Notification: In this treatment the participant is informed by the virtual receptionist that there is a problem with the computer system, therefore providing an explanation of the wait. The folder [Sound_Audio_Files](https://github.com/Terascale-All-sensing-Research-Studio/vr-queue-waiting-sound-dataset/blob/main/Assets/Sound_Audio_Files) contains all the audio assets in MP3 format for the With Notification treatment.
2.	Without Notification: In this treatment, the virtual receptionist does not inform the participant on why there is a delay. The folder [No_Sound_Audio_Files](https://github.com/Terascale-All-sensing-Research-Studio/vr-queue-waiting-sound-dataset/blob/main/Assets/No_Sound_Audio_Files) contains all the audio assets in MP3 format for the Without Notification treatment.  

We provide the differences in the audio assets used in each treatment below. **Present** indicates that the audio asset is used in the treatment and **Absent** indicates that the audio asset is not used in the treatment. 

| Audio Asset Name            | With Notification |	Without Notification  |	
| ----------------------------| ----------------- | --------------------- |
| Keyboard.mp3                | Present           | Present               |
| Recep_CheckedInOnline.mp3   | Present           | Present               |
| Recep_Hello.mp3             | Present           | Present               |
| Recep_IWillBeHelpingYou.mp3 | Present           | Present               |
| Recep_OneMoment.mp3         | Present           | Absent                |
| Recep_SystemIsSlow.mp3      | Present           | Absent                |
| Recep_WithYouShortly.mp3    | Present           | Absent                |
| MaleNPC_Mhhm.mp3            | Present           | Absent               |
| MaleNPC_Ok.mp3              | Present           | Absent               |

We provide the timing of when each audio asset is used in each treatment. We provide the time as Minute:Second format. **Absent** indicates that the audio asset is not used in the treatment. **(variable)** indicates that the event can occur at different time instances depending on when the participant approaches the receptionist NPC desk. **N/A** indicates that an audio asset is not used as it represents a specific event such as the start of the simulation, NPC customer in the queue leaving, or end of the simulation. 
 
| Time (Minute:Second) |	Event |	Audio Asset Name With Notification	| Audio Asset Name Without Notification |
| -------------------- | ----- | ---------------------------------- | ------------------------------------- |
| 0:00	| Participant spawned into simulation	| N/A	| N/A | 
| 0:01	| NPC receptionist says: "Hello, do you have an appointment today?"	| Recep_Hello.mp3	| Recep_Hello.mp3 | 
| 0:09	| NPC customer in queue says: "Uh-huh"	| MaleNPC_Mhhm.mp3	| Absent | 
| 0:13 |	Keyboard noise	| Keyboard.mp3	| Keyboard.mp3 | 
| 1:09	| NPC receptionist says: "'One moment, I will be with you."	| Recep_OneMoment.mp3	| Absent | 
| 1:13	| NPC customer in queue says: "Ok"	| MaleNPC_Ok.mp3	| Absent | 
| 1:15	| Keyboard noise	| Keyboard.mp3	| Keyboard.mp3 | 
| 1:41	| NPC receptionist says: "Sorry, system is still a bit slow, it might take some time."	| Recep_SystemIsSlow.mp3	| Absent | 
| 1:47	| NPC customer in queue says: "Ok"	| MaleNPC_Ok.mp3	| Absent | 
| 1:49	| Keyboard noise	| Keyboard.mp3	| Keyboard.mp3 | 
| 2:15	| NPC receptionist says: "I will be with you shortly."	| Recep_WithYouShortly.mp3	| Absent | 
| 2:18	| NPC customer in queue says: "Ok"	| MaleNPC_Ok.mp3	| Absent | 
| 2:20	| Keyboard noise	| Keyboard.mp3	| Keyboard.mp3 | 
| 3:08	| NPC customer in queue leaves	| N/A |	N/A | 
| 3:13	| NPC receptionist says: "I will be helping you." to participant	| Recep_IWillBeHelpingYou.mp3 | Recep_IWillBeHelpingYou.mp3 | 
| (variable) When participant reaches NPC receptionist	| NPC receptionist says: "'Hello, do you have an appointment today?" | Recep_Hello.mp3	| Recep_Hello.mp3 | 
| (variable) Upon selecting "Yes"	| NPC receptionist says: "I see you’ve checked in online. Can you please confirm the time?"	| Recep_CheckedInOnline.mp3	| Recep_CheckedInOnline.mp3 | 
| (variable) Upon selecting a time	| End of simulation | 	N/A	| N/A | 
