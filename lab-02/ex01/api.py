import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from cipher.transposition import TranspositionCipher
from cipher.playfair import PlayfairCipher
from cipher.vigenere import VigenereCipher
from flask import Flask, request, jsonify
from cipher.caesar_cipher import CaesarCipher
app = Flask(__name__)

#
transposition_cipher = TranspositionCipher()
#
playfair_cipher = PlayfairCipher()
#
vigenere_cipher = VigenereCipher()
# CAESAR CIPHER ALGORITHM
caesar_cipher = CaesarCipher()

@app.route("/api/transposition/encrypt", methods=["POST"])
def transposition_encrypt():
    data = request.get.json()
    plain_text = data.get["plain_text"]
    key = int(data.get["key"])
    encrypted_text = transposition_cipher.encrypt(plain_text,key )
    return jsonify({ "encrypted_text": encrypted_text})

@app.route("/api/transposition/decrypt", methods=["POST"])
def transposition_decrypt():
    data = request.get.json()
    plain_text = data.get["cipher_text"]
    key = int(data.get['key'])
    decrypted_text = transposition_cipher.decrypt(plain_text,key )
    return jsonify({'decrypted_text': decrypted_text})

@app.route("/api/playfair/creatematrix", methods=["POST"])
def playfair_creatematrix():
    data = request.json
    key = data["key"]
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    return jsonify({ "playfair_matrix": playfair_matrix})


@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    try:
        data = request.get_json()

        plain_text = data.get("plain_text", "")
        key = data.get("key")

        if key is None:
            return jsonify({"error": "Key không được để trống"}), 400

        key = int(key)

        encrypted_text = caesar_cipher.encrypt_text(
            plain_text, key
        )

        return jsonify({
            "encrypted_message": encrypted_text
        })

    except (ValueError, TypeError):
        return jsonify({
            "error": "Vui lòng nhập Key là số nguyên!"
        }), 400


@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    try:
        data = request.get_json()

        cipher_text = data.get("cipher_text", "")
        key = data.get("key")

        if key is None:
            return jsonify({"error": "Key không được để trống"}), 400

        key = int(key)

        decrypted_text = caesar_cipher.decrypt_text(
            cipher_text, key
        )

        return jsonify({
            "decrypted_message": decrypted_text
        })

    except (ValueError, TypeError):
        return jsonify({
            "error": "Vui lòng nhập Key là số nguyên!"
        }), 400

@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    data = request.json

    plain_text = data['plain_text']
    key = data['key']

    encrypted_text = vigenere_cipher.vigenere_encrypt(
        plain_text,
        key
    )

    return jsonify({
        'encrypted_text': encrypted_text
    })
    
@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    data = request.json

    cipher_text = data['cipher_text']
    key = data['key']

    decrypted_text = vigenere_cipher.vigenere_decrypt(
        cipher_text,
        key
    )

    return jsonify({
        'decrypted_text': decrypted_text
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)