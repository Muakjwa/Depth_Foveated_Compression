# Depth Foveated Compression in OpenCV

<table>
  <tr>
    <td align="center">
      <img src="https://github.com/user-attachments/assets/9e6b34cf-7f6a-4510-b449-14677e370a1c" alt="Original Image" width="350px" />
      <br>
      <em>Original Image (113.0KB)</em>
    </td>
    <td align="center">
      <img src="https://github.com/user-attachments/assets/d70930d8-58db-4a38-87fd-44b3612bd3a9" alt="Depth Map" width="350px" />
      <br>
      <em>Depth Map</em>
    </td>
    <td align="center">
      <img src="https://github.com/user-attachments/assets/aba15927-6829-42dc-9da9-1b79e2f647d0" alt="Foveated Compression" width="350px" />
      <br>
      <em>Foveated Compression (82.0KB)</em>
    </td>
  </tr>
</table>

<p align="center">  
    <img src="https://github.com/user-attachments/assets/9e6b34cf-7f6a-4510-b449-14677e370a1c" align="center" width="49.5%">  
    <img src="https://github.com/user-attachments/assets/05014b38-3a01-4bdc-9131-c51e3e05bc2c" align="center" width="49.5%">  
</p>





<p align="center"> 
    <img src="https://github.com/user-attachments/assets/a6093d2d-37b9-479a-9cc6-3c4d69571624" align="center" width="80%">  
</p>

<table>
  <tr>
    <td align="center">
      <img src="https://github.com/user-attachments/assets/55e7f256-4c9c-466b-9551-67e7c6cdbb87" alt="Alpha = 100" width="300px" />
      <br>
      <em>Alpha = 100 (113.0KB)</em>
    </td>
    <td align="center">
      <img src="https://github.com/user-attachments/assets/9c81061c-36fd-43da-b017-f4ee3856052b" alt="Alpha = 300" width="300px" />
      <br>
      <em>Alpha = 300 (90.3KB)</em>
    </td>
    <td align="center">
      <img src="https://github.com/user-attachments/assets/9cb1e03b-8808-457b-a8d4-8b829c60a9f0" alt="Alpha = 500" width="300px" />
      <br>
      <em>Alpha = 500 (64.7KB)</em>
    </td>
    <td align="center">
      <img src="https://github.com/user-attachments/assets/f9b55ae2-7116-4bff-8f6a-4808f6e83d49" alt="Alpha = 700" width="300px" />
      <br>
      <em>Alpha = 700 (48.6KB)</em>
    </td>
    <td align="center">
      <img src="https://github.com/user-attachments/assets/0896eb75-5963-4c70-b03f-4b3c8bfa016a" alt="Alpha = 900" width="300px" />
      <br>
      <em>Alpha = 900 (37.6KB)</em>
    </td>
  </tr>
</table>


<table>
  <tr>
    <td align="center">
      <img src="https://github.com/user-attachments/assets/635d3f5b-13a7-44a7-9888-5b538869cd56" alt="Alpha = 100 with Foveated" width="300px" />
      <br>
      <em>Alpha = 100 (82.0KB) with Foveated</em>
    </td>
    <td align="center">
      <img src="https://github.com/user-attachments/assets/c4c02ba6-933c-4b06-832c-1b3fd2d5bd16" alt="Alpha = 300 with Foveated" width="300px" />
      <br>
      <em>Alpha = 300 (77.2KB) with Foveated</em>
    </td>
    <td align="center">
      <img src="https://github.com/user-attachments/assets/05014b38-3a01-4bdc-9131-c51e3e05bc2c" alt="Alpha = 500 with Foveated" width="300px" />
      <br>
      <em>Alpha = 500 (59.7KB) with Foveated</em>
    </td>
    <td align="center">
      <img src="https://github.com/user-attachments/assets/f701f396-dbb0-438d-8a73-bc5ed118d816" alt="Alpha = 700 with Foveated" width="300px" />
      <br>
      <em>Alpha = 700 (45.1KB) with Foveated</em>
    </td>
    <td align="center">
      <img src="https://github.com/user-attachments/assets/48d868e2-17a8-4a43-80c4-1d6d213a2ea2" alt="Alpha = 900 with Foveated" width="300px" />
      <br>
      <em>Alpha = 900 (34.9KB) with Foveated</em>
    </td>
  </tr>
</table>


## Build OpenCV [ver. WINDOW]

[reference : https://www.youtube.com/watch?v=9xFTXSDw_9U]


## Build Method Summary

1. Cloning this repository in 'C:/opencv_sources/'
(like 'C:/opencv_sources/opencv-4.x' folder format)

2. Make 'build' folder in 'opencv_sources' folder & Make 'C:/opencv-4.x/build/' folder

3. By using CMake Program in Window, [Configure & Generate]</br>
    a. Set source code location : 'C:/opencv_sources/opencv-4.x'</br>
    b. Set build location : 'C:/opencv_sources/build'</br>
    c. configure</br>
    d. Uncheck 'BUILD_PERF_TESTS', 'BUILD_TEST', 'BUILD_JAVA', 'BUILD_PACKAGE', 'WITH_1394', 'WITH_GSTREAMER', 'WITH_LAPACK', 'WITH_VTK'</br>
    e. Check 'OPENCV_ENABLE_NONFREE'</br>
    f. Set 'OPENCV_EXTRA_MODULES_PATH' value : 'C:/opencv-sources/opencv_contrib-4.x/modules'</br>
    g. Set 'CMAKE_INSTALL_PREFIX' value : 'C:/opencv_4.x/build'</br>
    h. configure</br>
    i. Check BUILD_opencv_world & Just Search python</br>
    j. Configure & Generate</br>

4. Open project & Set Debug -> Release & 'CMakeTargets/INSTALL' 우클릭 후 build 선택

If this instruction is confused, you can follow reference video [https://www.youtube.com/watch?v=9xFTXSDw_9U]

After This process, We can apply custom-built opencv to python

Now, We can build opencv in this process

1. Run 'Developer command prompt' in Window

2. Go to the folder path 'C:/opencv_sources'

3. Run below command in prompt.

``` cmake -B"C:/opencv_sources/build" -H"C:/opencv_sources/opencv-4.x" -G"Visual Studio 17 2022" -DCMAKE_BUILD_TYPE=Release ^
-DOPENCV_EXTRA_MODULES_PATH="C:/opencv_sources/opencv_contrib-4.x/modules" -DCMAKE_INSTALL_PREFIX="C:/opencv-4.x/build" ^
-DINSTALL_TESTS=ON -DINSTALL_C_EXAMPLES=ON -DBUILD_EXAMPLES=OFF -DBUILD_opencv_world=ON ^
-DWITH_CUDA=ON -DCUDA_TOOLKIT_ROOT_DIR="C:/Program Files/NVIDIA GPU Computing Toolkit/CUDA/v10.1" ^
-DCUDA_FAST_MATH=ON -DWITH_CUBLAS=ON -DCUDA_ARCH_PTX=7.5 -DWITH_NVCUVID=ON ^
-DWITH_OPENGL=OFF -DWITH_MFX=OFF -DBUILD_PACKAGE=OFF -DWITH_MATLAB=OFF -DBUILD_PREF_TESTS=OFF -DBUILD_TESTS=OFF ^
-DBUILD_opencv_python3=ON -DBUILD_opencv_python2=OFF -DOPENCV_SKIP_PYTHON_LOADER=ON ^
-DBUILD_JAVA=OFF -DWITH_LAPACK=OFF -DWITH_VTK=OFF -DWITH_1394=OFF -DWITH_GSTREAMER=OFF ^
-DWITH_TBB=OFF -DWITH_EIGN=OFF -DMKL_WITH_TBB=OFF -DBUILD_WITH_STATIC_CRT=OFF ^
-DOPENCV_ENABLE_NONFREE=ON -DBUILD_opencv_rgbd=OFF 
```

4. Open 'C:/opencv_sources/build/OpenCV.sln' file & Debug -> Release & 'CMakeTargets/INSTALL' 우클릭 후 build 선택

5. Copy three dll file in 'C:/opencv-4.x/build/bin/' & paste to 'python312/Lib/site-packages'</br>
(%%% python site-packages folder location can vary by user %%%)</br>
(%%% In my case folder path is 'C:\Users\username\AppData\Local\Programs\Python\Python312\Lib\site-packages' %%%)</br>


-> After this Process, We can use opencv with custom-built version



## OpenCV File Structure
```
├─ opencv-4.x
|  ├─ ...
|  ├─ 3rdparty
|  |  ├─ ...
|  |  └─ libjpeg-turbo
|  |     ├─ ...
|  |     ├─ jcdctmgr.c (func. forward_DCT - DCT 변환하여 넘겨주는 함수)
|  |     └─ (이 함수에서 quantization level을 결정해 Low Pass Filter를 적용해주는 방식으로 Foveated Compression 적용)
|  └─ modules
|     ├─ ...
|     └─ imgcodecs
|        ├─ ...
|        └─ src
|           ├─ ...
|           ├─ loadsave.cpp (func. imencode - cv2.imencode에 호출되는 함수 (Foveation 정보를 이용한 image compression))
|           |               (func. imencode_D - cv2.imencode_D에 호출되는 함수 (Depth 정보를 이용한 image compression))
|           |                   (source code 상 jcdctmgr.c 코드의 alpha 변수에 의해 compression level이 결정됨.)
|           └─ grfmt_jpeg.cpp (func. JpegEncoder::write - 이미지를 jpeg으로 encode하는 함수)
|
└─ opencv_contrib-4.x
```

## Test Method
```
import cv2

cv2.imencode('.jpg', image) # 일반 jpeg encoding
cv2.imencode('.jpg', image, [cv2.IMWRITE_JPEG_FOVEATION_DISTANCE, 62]) # foveated compression encoding
cv2.imencode_D('.jpg', image, depth_map) # Depth Foveated Compression encoding 
```
