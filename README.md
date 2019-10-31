# equirectangular-to-cubemap

全方位画像を透視投影画像に変換するプログラム．

使用するときはプログラムの最初に，

```
import eq2cm
```

と書く．次に各種パラメータを決める．

```
fov = np.pi / 2 # 画角
u   = np.pi / 3 # 水平方向の角度
v   = np.pi / 6 # 垂直方向の角度
out_h = 800     # 出力画像の縦の長さ
out_w = 800     # 出力画像の横の長さ
```

上で決めたパラメータを引数に入れて実行する．

```
eqimg = cv2.imread('xxx.jpg')
pers = eq2cm.eq_to_pers(eqimg, fov, u, v, out_h, out_w)
cv2.imwrite('out.jpg', pers)
```

これで透視投影画像が出力される．ちなみに`sample.py`は，

```
python3 sample.py images/589271383.507201.JPG output/
```

で実行できる．
