# OHTS_Assignment_SLmail_Buffer_Overflow
This repository contains the python codes that will be used in the buffer overflow exploitation of SLmail and the complete guide of conducting the exploit. 

SLmail_Buffer_Overfloe.pdf file contains the guide for the exploit.

Other files in this repository will be used in the exploitation process as below.

      * fuzzer.py is the first file to use. That files helps in to get the approximate value where the buffer overflow is happening in SLmail.
      * poc.py is the second file to use. By this file we are going to understand the exact offset of the value where the SLmail gets crash with buffer overflow.
      * poc2.py is the third file to use. By this file we are going to check whether we can gain the control of EIP.
      * Next, we can use poc3.py, poc4.py and poc5.py files to identify the bad characters according to SLmail.
      * slmailsploit.py is the final and most important file of the exploit. This file will helps in getting the reverse shell of the victim machine and gaining the system access of the victim machcine. 

