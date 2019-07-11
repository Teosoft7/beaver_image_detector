## Business Understanding
Wildlife cameras are a great way to monitor animals remotely, however, because they are usually motion-activated, they produce large quantities of image data that needs to be processed, which is a time consuming task. To decrease the amount of time needed for image processing from wildlife cameras, I built an object detection algorithm for species identification. To create my model I used data from the Eastside Audubon Society Beaver Project as a case study for beaver identification in images.

## Data Understanding
In partnership with other stakeholders, the Eastside Audubon Society is setting up wildife cameras to better understand the beaver population around Lake Sammamish in Washington State. Currently two cameras are set up near a beaver lodge on Lake Sammamish. The dataset consists of over 2,000 photos, of which approximately 70% contain beavers. The remaining images contain birds, raccoons, roof rats, squirrels, frogs, or no animals. 

## Data Preparation
Data was downloaded from a shared Dropbox account as a zip file. Images were uploaded to Mac Photos to correct dates and renamed with ExifRenamer by camera, site, and date to elimate any duplicate names. 

Photos were annotated with bounding boxes for each animal instance using LabelImg. Annotations were output as xml files. Annotation files and images were split into train and test sets for images with beaver instances and for the whole dataset. Data was converted to Tensorflow Records for modeling. All data was stored in a Google cloud bucket.

## Modeling
Models were trained on the data using transfer learning with the Tensorflow Object Detection API. Models were trained until total loss was less than two. Three different models are be tested, they are as follows:
* ssd_

## Evaluation
I will report both the mean average precision score and cross entropy loss, on training and test data. I don't want to miss any beaver photos so I will choose classification thresholds that maximize recall for beavers.

## Deployment
The model will be deployed as a Flask app where someone can upload a picture and see if there are any beavers present. There will also be a feature to upload a zipfile of photos and return a file with predicted annotations. Users of this app will be able to quickly sort through their photos or check if a photo has any beavers.

