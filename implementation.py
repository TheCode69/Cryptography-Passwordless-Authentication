import pyotp
import base64
import os

# Generate a random symmetric key
def generate_key():
    return base64.b32encode(os.urandom(10)).decode('utf-8')

# Generate TOTP
def generate_totp(secret_key):
    totp = pyotp.TOTP(secret_key)
    return totp.now()

# Verify TOTP
def verify_totp(secret_key, otp):
    totp = pyotp.TOTP(secret_key)
    return totp.verify(otp)

# Generate symmetric key
key = generate_key()

# Generate TOTP
otp = generate_totp(key)
print("Generated OTP:", otp)

# Verify TOTP
otp_input = input("Enter OTP to verify: ")
if verify_totp(key, otp_input):
    print("OTP Verified Successfully!")
else:
    print("OTP Verification Failed!")
