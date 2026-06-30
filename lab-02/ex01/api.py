import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from cipher.playfair import PlayfairCipher
from cipher.vigenere import VigenereCipher
from flask import Flask, request, jsonify
from cipher.caesar_cipher import CaesarCipher
app = Flask(__name__)

playfair_cipher = PlayfairCipher()
#
vigenere_cipher = VigenereCipher()
# CAESAR CIPHER ALGORITHM
caesar_cipher = CaesarCipher()

@app.route("/api/playfair/creatematrix", methods=["POST"])
def playfair_creatematrix():
    data = request.json
    key = data["key"]
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    return jsonify({ "playfair_matrix": playfair_matrix})




@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    data = request.json
    plain_text = data["plain_text"]
    key = int(data["key"])
    encrypted_text = caesar_cipher.encrypt_text(plain_text,key )
    return jsonify({ "encrypted_message": encrypted_text})

@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    data = request.json
    cipher_text = data["cipher_text"]
    key = int(data["key"])
    decrypted_text = caesar_cipher.decrypt_text(cipher_text,key )
    return jsonify({"decrypted_message": decrypted_text })

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