import secrets
from fastapi import APIRouter, Response
from utils.make_qr import make_qr

# このルーターを "/invites" という道（パス）の担当にする
router = APIRouter(prefix="/invites", tags=["invites"])

#urlのコミュニティーごとの特殊文字列生成
@router.post("/")
async def create_invite(community_id: str):
    # 12文字のランダムな文字列を生成
    invite_code = secrets.token_urlsafe(12)
    
    # DBにこのコードを保存する処理を書いてもらう
    # save_invite_to_db(community_id, invite_code)
    
    # フロントエンドが「参加ページ」へ飛ばすためのURLを返す
    return {
        "invite_code": invite_code,
        "invite_url": f"https://opencal-app.com/join/{invite_code}"
    }

#発行された特殊文字列を読み取り、QRコード画像にして返す窓口(make_qr.pyの関数を呼び出す)
@router.get("/{invite_code}/qr")
async def get_qr(invite_code: str):
    # ユーザーがQRをスキャンした時に飛ぶ先のURL
    full_url = f"https://opencal-app.com/join/{invite_code}"
    
    # make_qr.py で作った関数で画像データ（BytesIO）を取得
    img_payload = make_qr(full_url)
    
    # Responseを使って、中身が画像であることを伝えて返却する
    return Response(content=img_payload.getvalue(), media_type="image/png")