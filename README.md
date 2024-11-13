# Foveated Rendering in OpenCV

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