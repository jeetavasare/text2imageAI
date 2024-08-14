# text2imageAI
A text to image generator with Open-AI's glide model allows users to generate their thumbnails and other media assets without any technical requirements and worrying about infringing copyright's

## Requirements
  - CPU
      - Minimum: Intel i3 or equivalent
      - Reccomended: i5 or higher
  - Memory
    - Minimum: 8GB + virtual memory enabled
    - Reccomended: 16GB or higher
  - GPU
    - Minimum: Not mandatory
    - Reccomended: Nvidia 20XX series or higher with CUDA compute capabilities and VRAM higher than 6gb
  - Storage
     - 3.5 GB free space (SSD reccomended)
  - Internet
      - 3GB to download the model

## Installation
1. **Clone the repository:**  
  ```
  git clone https://github.com/jeetavasare/text2imageAI.git
  ```
2. **Setup environment and install dependencies**  
  ```
  pip install -r requirements.txt
  ```
3. **Other dependencies**
   1. Jupyter Notebook
  
4. **Run the `text2im.ipynb`**  
  - Open Jupyter notebook locate the file `text2im.ipynb` and run it
    - Alternatively you can install Visual Studio Code with Jupyter Notebook extension connect to the notebook kernel and run it from there
  - In the output content locate the link `http://127.0.0.1:5000` and open it in a browser (most mordern browsers are supported)

## Usage
1. **Register**
    - Assuming a first time usage Click on the profile icon and click on **Register** Instead
    - Set your username and password
2. **Generate Image**
   - In the Prompt field give a clear description of the image you want
   - In the quality field give the quality if the image
  > [!IMPORTANT]
  >    - The quality field does not represent the quality of the image file iteself rather a model parameter that controls not only quality but also the accuracy of the generated image.  
  >    - You can pass values of above 100 to get even sharper images but above 100 the image quality has little to no difference. MAX VALUE is 1000  
  >    - By default the output of the image will be a 64x64 image  
  >    - Check the `Load 256x256` image to generate a higher resolution image (This can take upto 3 times as long on the same quality)

<br>  

> [!NOTE]
> If the model is run for the first time it needs to download 3GB of model file, this could take a very long time(2hrs+)
> This issue is not related to the user but the server hosting the model. So even if you have good internet connection it will take quite a long time
