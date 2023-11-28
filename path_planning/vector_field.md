# Vector Field Path Following for Small Unmanned Air Vehicles - Trajectory 
Derek R. Nelson D. Blake Barber Timothy W. McLain Randal W. Beard

## Literature Review
- Simple PD controllers


## What 
- This paper presents a new method for unmanned aerial vehicle path following using vector fields to represent desired ground track headings to direct the vehicle onto the desired path.


## How 
- Get the groundtrack heading which is related towards win 
- Check out the algorithm for vector field construction, might be useful to send as desired heading when running MPC, in response to path smoothing 


## Drawbacks or important notes
- Only longitudinal 
- Send a yaw reference command to autopilot system 
- Roll is not accounted for 
- Airspeed is assumed to be constant

- Might use this for improved heading track with MPC? 
