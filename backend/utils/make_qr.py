import qrcode
from io import BytesIO

def make_qr(url: str):
    # QRコードを生成
    qr = qrcode.QRCode(
        version=1,  # QRコードのサイズ（1〜40）
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # 誤り訂正レベル
        box_size=10,  # ボックスのサイズ
        border=4,  # ボーダーの幅
    )   
    qr.add_data(url)
    qr.make(fit=True)

    # 画像の作成（Pillowを使用）
    img = qr.make_image(fill_color="black", back_color="white")
    
    # 画像をメモリ上のバイナリデータとして保存
    img_payload = BytesIO() #これから画像を書き込むための、空のメモリ領域の用意
    img.save(img_payload, format="PNG") #本来ならファイル名を指定する場所に、用意したメモリ領域を指定
    img_payload.seek(0) #カーソルを一番最初まで「巻き戻す」作業
    #普通に保存した場合：サーバー内に temp_qr.png を保存->そのファイルを開いて、中身を読み出す。->フロントエンドに中身を送信する。->送信後に temp_qr.png を手動で削除するとなる
    
    return img_payload


