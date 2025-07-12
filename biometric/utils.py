import hashlib

def generate_biometric_hash(face_data, voice_data):
    combined = face_data + voice_data
    return hashlib.sha512(combined.encode()).hexdigest()
