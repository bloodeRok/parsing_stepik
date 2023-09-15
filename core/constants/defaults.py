import os

from dotenv import load_dotenv

load_dotenv()

STEPIK_CLIENT_ID = os.environ.get("STEPIK_CLIENT_ID", "")
STEPIK_CLIENT_SECRET = os.environ.get("STEPIK_CLIENT_SECRET", "")
AUTH_DATA = {"grant_type": "client_credentials"}
GOOGLE_SHEET_CREDENTIALS = {
    "type": "service_account",
    "project_id": "sharp-cosmos-331417",
    "private_key_id": "656786bf7792b9f61899ce27373cf04992515589",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDMlcu2TtTfvP5T\nbCyUPUhz80NCHxrO2sQ4ndwb6HngzBf1aA3iY7xtVD8m6LYyALwO1wCxnhjkh4c4\nA0fo3XQCTPWgDU5RzavsCmQJrua3Bv6IVEZaRqUdlJwmwMw6cDhj+wka3npJaGln\nDKLaw5KJsJ9oKrit+TTeIbcM15xIjtpAwXOl7scaxLtYKZ6mPKhJKUNOzD3RBwBT\nBe7wCeqb0yXQ6E+7/w06DhmkIFq5TqzxvNprQPZnJgbxB03M4CuHsR9Yv1RvzJra\nreuaHMNqF8ce8yD0nc3pBf2vPXwkryqnkX0zytwKMnYBrO9qdRN2RiMoPt3MpdBc\nr2UrnXYpAgMBAAECggEAE8gBGjfNl/OVcLoDJnM1e/afwHcy96DJ+8Jxu6YTEMQT\nJfihbQwhNj4A3DGAml2dUV8DE2l6tTAQiD8y9wZglu9biZX3xmuZTbmkehY1+yj7\nN/HUGpr9kJpjrdCS/qyGm040z2sHDm2A0YS0g2wJEXSpOSB2WmX/8WF3qk93rkEr\nUjK1PU+mqlzBUJCRy6A34p++E9/2Vk9e73tqM3HRadzTczhF3YboX0HKIbJ22Kj8\ndUo4ImOH0YWBvMdXeiQ3PmYOO58PCYJZrbe5M/n3MsFdArzzpENMFcaq20BpMYjW\n34t+h4I4zDqt0YlqBkzF69SknS08e1VAsBov3bJFAQKBgQD65qrTPhjw7BwdY1ET\njGb3mk2IW58cNdGXe/AxAMhOj7XZrSe7c6hSn88xip5CsdolOpzTfRNlZRzKbHYg\nTrj7wXD3Ai71xcpaqc0NDXD8Ih5RerRTzDcCkzbge3gpGjlbHQyuKRGXR2Je93Xs\n2ajHbdIFJknEwlQ8rAnoy0ccqQKBgQDQviqQ7pI9Ui7TiHrDG0neLdFj2ChdnlTH\nnNhokQjLMjDwZB6VuY6I0vCGx0LytI12OK2o6rzF/+RSOyNkehM2vRki/PoWls2x\nnoQOJFAa/+t9qCAKzvrxytXivNhDhQe8juCNbvGxqL8E9m4XiMbf496U48ZuJg2q\nN+2rpe39gQKBgCUZ1OrVxORjVaj21bdZTKSSeaKPQdDvGGYZGqR0ZCpRz+c3Vqe+\na4aEQSQnRk3AdOyKZURUu3iD4iUAstsGKQ55RVYRSZZoQAr2Du8+LJXsCaWsyluV\n2BCWakf5mgQh75dMjWJ3ijVfhelbGGIEsZOD5smCJuhkgAZUvkZhQMu5AoGBAKX1\nCtJ/WjT2idQTxcYog+noc3j1+eG0Z6LryAIajOs/1DjK4KYZCIEvc5s0AL4FXhKH\nrUmGlt60O0pFSjYv9+alIL74cbxT2OVGKac0p5tPrGISsKbnOAvUP4gsq6PCuAvp\nbA4GDpI4nuXLJmv/il2mROgKz0/zYRnbrVGyciwBAoGBALUGC1DFXf0YvuH5EOSv\nRce+s7iFKTMkN0G0k4Ec8Nu83++pJtdq7Ytf6ycHlUBjZcX4yw+c2n2LGS+PRAI5\nREjVA3wsV/lNyoj6v4QEFHeW2nIr5h9Ccm7KsC69AgKSxKFpQMu1c5asIxju+5FV\n7JWlSnihoDSx0FOmiFLeHF0e\n-----END PRIVATE KEY-----\n",
    "client_email": "get-payments-math-for-ds@sharp-cosmos-331417.iam.gserviceaccount.com",
    "client_id": "114838966484273942088",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/get-payments-math-for-ds%40sharp-cosmos-331417.iam.gserviceaccount.com"
}
GOOGLE_SHEET_ID = "1h3yYSz8Xc3Mfgx6NLaLVDmk8tke18DWUfsu9eiZ2KR0"
