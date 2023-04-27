# Building a massive set of proposed neologisms for the Quechua language fulfilling the demand of coining words for new things and concepts
I keep creating neologisms for Quechua language, now, dealing with the demand instead of the offer how I did the first time

The first step was getting the largest English vocabulary freely available, we found it in the [English Words](https://github.com/dwyl/english-words) repository.


First, I tried using **googletrans** app but it didn't work at all. Then I decided use Google Translate API, at beginning I tried running in my local laptop but connection to API was so slow than I calculated processing 370k words would take 28 days! 
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

Being impossible wait for so long, I tried the same in Google Cloud Shell, here the process would take only 20 hours but the process is interrupted as soon s you disconect from Google Cloud Shell. So, I decided, do it with a Google VM

Creating a Google VM is explained [here](https://cloud.google.com/appengine)

Connect to your VM by your local console:

1. gcloud auth login
Your browser will be opened to sign in to continue to Google Cloud SDK

You are now logged in as [GOOGLE_USER].
Your current project is [None].  You can change this setting by running:
  $ gcloud config set project PROJECT_ID
  
2. gcloud config set project PROJECT_ID

3. gcloud compute ssh --zone "YOUR_ZONE" "INSTANCE_NAME" --project "PROJECT_ID"
WARNING: The private SSH key file for gcloud does not exist.
WARNING: The public SSH key file for gcloud does not exist.
WARNING: You do not have an SSH key for gcloud.
WARNING: SSH keygen will be executed to generate a key.
Generating public/private rsa key pair.
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/YOUR LOCAL NAME/.ssh/google_compute_engine
Your public key has been saved in /home/YOUR LOCAL NAME/.ssh/google_compute_engine.pub
The key fingerprint is:
SHA256:*************************************** YOUR-LOCAL-NAME@YOUR-LOCAL-LAPTOP
The key's randomart image is:
+---[RSA 3072]----+
|.     .o++o.     |

|                 |
+----[SHA256]-----+
Updating project ssh metadata...⠼Updated [https://www.googleapis.com/compute/v1/projects/focused-waters-384416].
Updating project ssh metadata...done.                                          
Waiting for SSH key to propagate.
Warning: Permanently added 'compute.5184505298729410928' (ED25519) to the list of known hosts.
Welcome to Ubuntu 22.04.2 LTS (GNU/Linux 5.15.0-1030-gcp x86_64)

Your GOOGLE_USER is your gmail account, then you must create a project in [Google Cloud](https://cloud.google.com) to get a PROJECT_ID, YOUR_ZONE and   
INSTANCE_NAME are assigned when you create the virtual machine

4. gcloud compute scp LOCAL_FILE INSTANCE_NAME:~/ , use this to move LOCAL_FILE from your desktop to home folder in your virtual machine

5. Environment setup

Before you can begin using the Translation API, run the following command in Cloud Shell to enable the API:

gcloud services enable translate.googleapis.com

You should see something like this:

Operation "operations/..." finished successfully.

Now, you can use the Translation API!

Set the following environment variable (to be used in your application):

export PROJECT_ID=$(gcloud config get-value core/project)

echo "→ PROJECT_ID: $PROJECT_ID"

Note: This environment variable only applies to your current shell session. Therefore, if you open a new session, set this variable again.

Navigate to your home directory:

cd ~

Create a Python virtual environment to isolate the dependencies:

virtualenv venv-translate

Activate the virtual environment:

source venv-translate/bin/activate

Note: To stop using the virtual environment and go back to your system Python version, you can use the deactivate command.

Install IPython and the Translation API client library:

pip install google-cloud-translate

Now, you're ready to use the Translation API client library!

Note: If you're setting up your own Python development environment outside of Cloud Shell, you can follow these [guidelines](https://cloud.google.com/python/setup).

Transfer the python script and the english vocabulary to the VM 
gcloud compute scp /LOCAL/DIRECTORY/Translate.py INSTANCE_NAME:~/

Reversely, to get files from the VM to your laptop, run
gcloud compute scp INSTANCE_NAME:~/FILES /LOCAL/DIRECTORY/
