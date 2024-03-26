import pyotp 


def otpToken():
    totp = pyotp.TOTP(pyotp.random_base32(), digits=6, interval=60)

    otp = totp.now()

    print(f"The OTP is : {otp}")

    return otp 
