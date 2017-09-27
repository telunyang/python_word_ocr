# Basic-OCR-testing

## 【說明】
使用 Python、OpenCV、OCR（Tesseract）來取得帶有雜點的驗證圖片文字。

## 【運作方式】
將圖片裁切（此例有邊框），並進行灰階設定，再透過迭代每一個 pixel，走訪過上下左右共 49 個點，來決定原先的點是否為雜點，然後將其去除，最後把圖片膨脹（另一種說法，就是把白色加粗），讓 OCR 好辨識圖片當中的文字，再建立文字檔案，並加以輸出。

![雜點判斷演算法](https://github.com/telunyang/Basic-OCR-testing/blob/master/example/algorithm.png "雜點判斷演算法")

## 【範例圖片】
原先的驗證圖片
![原先的驗證圖片](https://raw.githubusercontent.com/telunyang/Basic-OCR-testing/master/media/sample04.jpg "原先的驗證圖片")

經過處理後的圖片
![經過處理後的圖片](https://raw.githubusercontent.com/telunyang/Basic-OCR-testing/master/media/target04.jpg "經過處理後的圖片")

## 【影片展示】
[![影片展示](http://img.youtube.com/vi/ie89hZptxBg/0.jpg)](https://www.youtube.com/watch?v=ie89hZptxBg)