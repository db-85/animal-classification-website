# Animal classification

Website: http://animalclassification-env.eba-mubqxnvf.eu-central-1.elasticbeanstalk.com/

This website shows a deployed version of the deep learning model on AWS Beanstalk where the user can upload a picture in a standard format and run the classification algorithm.

This toolbox can classify animal pictures among 151 different species of animals.

## Website

The website has been built using the following tech stack (among others):

*Backend:* 
- Flask (to run the web server).
- Tensorflow/keras (to tune the model and compute predicted classes using the model).
- JavaScript (to allow the user to upload pictures and send the uploaded piicture through the prediction model).

*Frontend:*
- HTML/CSS/JavaScript to display the website and let the user interact with it.

*Container*
- Docker

## Deep learning model

The deep learning model is a convolutional neural network (CNN), where the input is the picture resized to be 256x256 pixels, and the output is a vector of probabilities to belong to each of the 151 classes.

## Deployment

The code containing the ML model has been containerized using Docker and deployed on AWS Elastic Beanstalk.

## Further work

As of now, this project can be improved in several directions. Below is a non-exhaustive list of potential additions to this project:

- UI/UX: Improve the overall website design for a better user experience.
- Compatibility: Test the compatibility of the website on different platforms (Windows, Mac, Linux, Android, IOS etc.).
- Prediction: In addition to the class, report the probabilities of he picture belonging to each class.
- ML model: Improve accuracy of the model, and optimize the model hyperparameters.
- Pipeline: More automated testing, reporting and deployment of updates. For instance, allow the model to be periodically updated, fitted to new data and deployed on the website.
- Data collection: Collect feedback from the user and store it in an RDS (relational database system) to assess the needs for updates.
- Data augmentation: In addition to prediction, the user should also be allowed to add their pictures to the dataset, so they can be included in the training/validation datasets.
- Monitoring: Generate reports periodically. Include model accuracy for each class and user feedback (e.g. whether their picture has been correctly identified).
- Classes: Add more classes, and allow the model to be trained with these new classes once sufficiently many pictures are collected.
