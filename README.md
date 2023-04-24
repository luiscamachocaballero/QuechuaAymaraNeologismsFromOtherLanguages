# Building a massive set of proposed neologisms for the Quechua language fulfilling the demand of coining words for new things and concepts
I keep creating neologisms for Quechua language, now, dealing with the demand instead of the offer how I did the first time

The first step was getting the largest English vocabulary freely available, we found it in the [English Words](https://github.com/dwyl/english-words) repository.



When your code is running in a local development environment, the best option is to use credentials associated with your Google Account.

    Install and initialize the gcloud CLI, if you haven't already.

    Create your credential file:

    gcloud auth application-default login

A login screen is displayed. After you log in, your credentials are stored in the local credential file used by [ADC](https://cloud.google.com/docs/authentication/application-default-credentials). You should be then be allowed to automatically determine credentials.


Then test this going into the terminal and type:

# Linux/Unix
set | grep GOOGLE_APPLICATION_CREDENTIALS 

or

# Windows:
set | Select-String -Pattern GOOGLE_APPLICATION_CREDENTIALS 

This will show you the environment variable and the path where it is located. If this returns nothing then you have not set the variable or you may have the wrong path set
