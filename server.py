from flask import Flask, request, jsonify
import bcrypt

app = Flask(__name__)

correct_password = b"qwerty"
correct_password_hash = bcrypt.hashpw(correct_password, bcrypt.gensalt())

@app.route('/check-password', methods=['POST'])
def check_password():
    try:
        data = request.get_json()
        if not data or 'password' not in data:
            return jsonify({'success': False, "message": "Password not provided"}), 400
        
        input_password = data['password'].encode('utf-8')
        is_valid = bcrypt.checkpw(input_password, correct_password_hash)
        return jsonify({"success": is_valid})
    
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500
    
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)