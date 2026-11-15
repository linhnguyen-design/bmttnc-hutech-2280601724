
from flask import Flask, request, jsonify
from cipher.caesar_cipher import CaesarCipher

app = Flask(__name__)


# Trang chu
@app.route('/')
def home():
    return "Caesar Cipher API is running!"


# Ma hoa Caesar
@app.route('/api/caesar/encrypt', methods=['POST'])
def caesar_encrypt():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "Missing JSON data"}), 400

        text = data.get("plain_text", "")
        key = int(data.get("key"))

        caesar = CaesarCipher()
        encrypted_text = caesar.encrypt_text(text, key)

        return jsonify({
            "encrypted_message": encrypted_text
        }), 200

    except (ValueError, TypeError):
        return jsonify({
            "error": "Key must be an integer"
        }), 400

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


# Giai ma Caesar
@app.route('/api/caesar/decrypt', methods=['POST'])
def caesar_decrypt():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "Missing JSON data"}), 400

        text = data.get("cipher_text", "")
        key = int(data.get("key"))

        caesar = CaesarCipher()
        decrypted_text = caesar.decrypt_text(text, key)

        return jsonify({
            "decrypted_message": decrypted_text
        }), 200

    except (ValueError, TypeError):
        return jsonify({
            "error": "Key must be an integer"
        }), 400

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )
