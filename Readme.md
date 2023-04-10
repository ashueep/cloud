# ReadMe
-----
This repository contains the work implemented as part of course assignment for **CS 466 Cloud Computing**
</br> The work in this repository is inspired from </br> ***Energy Optimal Partial Computation Offloading Framework for Mobile Devices in Multi-access Edge Computing***
by **Sonali Chouhan** of Department of Electronics and Electrical Engineering of Indian Institute of Technology Guwahati.
</br> This repository is the work of : 
* Aditya Sriram (191EE209)
* Ashutosh Anand (191CS111)
* Sudarshan Sundarrajan (191CS255)
* Sushanth Satesh Rao (191EE156)

</br> The work in this repository is organised as shown below (file structure) :

*  Compression.py
*  Data.py 
* LocalCompute.py
* MobileDevice.py
* Transmission.py
* energy.dat
* energy.plot
* energy.png
* Parameters_For_Simulations.PNG


## Energy Plot 
### ![alt text](https://github.com/ashueep/cloud/blob/main/energy.png?raw=true)

## Simulation Parameters Table
### ![alt text](https://github.com/ashueep/cloud/blob/main/Parameters_For_Simulations.PNG?raw=true)

## To run code

`python3 MobileDevice.py > energy.dat`

To obtain graph run

`gnuplot -c energy.plot`

Graph Output is stored in `./energy.png` 

<src img="./energy.png">
