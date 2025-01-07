# Leaf_Disease_Detection
 Plant disease detection plays a crucial role in agriculture, helping farmers manage crop health and prevent the spread of diseases. To address this, we developed an advanced system using deep learning techniques, specifically a Convolutional Neural Network (CNN), to classify leaf images into 39 different categories of plant diseases. The model is built using the PyTorch framework, which allows for efficient training and fine-tuning of the neural network.

For training the model, we used the PlantVillage dataset, which contains a large collection of labeled images representing various plant diseases. The dataset provides a diverse range of leaf images from different plants, making it ideal for building a robust model capable of recognizing a wide array of diseases. By leveraging the power of CNNs, the system can accurately classify images and assist farmers in early disease detection, thereby improving crop management practices and reducing the risk of widespread plant infections. The model's performance can be further enhanced through continual training and fine-tuning using new data, ensuring that it remains relevant and accurate over time.
# Run Project in your Machine
1. You must have Python3.8 installed in your machine.
2. Install all the dependencies by running the following command:
   ```bash
   pip install -r requirements.txt
3. Navigate to the Flask Deployed App folder.
4. Download the pre-trained model file model.pt from [here](https://drive.google.com/file/d/1CAFW-rcJ5V2KRQdYu34UPMajPNFIFuQ7/view?usp=sharing).
5. Place the downloaded model.pt file in the Flask Deployed App folder.
6. Run the Flask app using the following command:
   ```bash
   python app.py
7. You can also use the downloaded model file in the Model Section and experiment with it using Jupyter Notebook.
# Testing Images
1. If you do not have leaf images then you can use test images located in test_images folder
2. Each image has its corresponding disease name, so you can verify whether the model is working perfectly or not
# Website Deployed Images
### Main Page

![Website Image](Website%20Image/Image_9.jpeg)
![Website Image](Website%20Image/Image_8.jpeg)
